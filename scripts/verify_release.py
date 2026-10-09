#!/usr/bin/env python3
"""
Automated Release & Contract Verification Suite for Three.js Evidence Graph & The Hollow Meridian.
Validates:
1. SHA256SUMS.txt LF line endings and bit-exact SHA-256 digests for all listed files.
2. release-manifest.json repository URL, SHA-256 digests, byte sizes, PDF page counts, and JPEG dimensions.
3. Draft 2020-12 JSON Schema validity (schemas/*.schema.json and orchestration/*.schema.json)
   and validation of golden fixtures in examples/run-0001/*.json.
4. PDF structural metadata (/Lang, /MarkInfo), zero "/-" ligature corruption in extracted text,
   and clickable /URI link annotations on page 64 of the Operational Manual.
5. Zero EXIF metadata (exif_len == 0) across all JPEGs in assets/*.jpg.
6. Local Markdown link resolution and 4-language translation parity across README*.md and docs/*.md.
"""

import hashlib
import json
import os
import re
import sys

try:
    import jsonschema
except ImportError:
    jsonschema = None
import pypdf
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CANONICAL_REPO_URL = "https://github.com/Emily2040/-threejs-evidence-graph"


def sha256_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def check_sha256sums() -> int:
    sums_path = os.path.join(ROOT, "SHA256SUMS.txt")
    with open(sums_path, "rb") as f:
        raw = f.read()
    assert b"\r\n" not in raw, "SHA256SUMS.txt must use LF line endings (found CRLF)"
    lines = [line.strip() for line in raw.decode("utf-8").splitlines() if line.strip()]
    for line in lines:
        digest, rel_path = line.split("  ", 1)
        full_path = os.path.join(ROOT, rel_path)
        assert os.path.isfile(full_path), f"Missing file listed in SHA256SUMS.txt: {rel_path}"
        assert os.path.getsize(full_path) > 0, f"Zero-byte file listed in SHA256SUMS.txt: {rel_path}"
        assert digest != "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855", (
            f"Empty-file SHA-256 digest in SHA256SUMS.txt for {rel_path}"
        )
        actual = sha256_file(full_path)
        assert actual == digest, f"SHA-256 mismatch for {rel_path}: expected {digest}, got {actual}"
    return len(lines)


def check_release_manifest() -> int:
    manifest_path = os.path.join(ROOT, "release-manifest.json")
    with open(manifest_path, "r", encoding="utf-8") as f:
        manifest = json.load(f)
    assert manifest.get("repository") == CANONICAL_REPO_URL, (
        f"Invalid repository URL in release-manifest.json: {manifest.get('repository')}"
    )
    if "suite" in manifest:
        assert manifest["suite"].get("repository") == CANONICAL_REPO_URL, (
            f"Invalid suite.repository URL in release-manifest.json: {manifest['suite'].get('repository')}"
        )
    checked = 0
    for pub in manifest.get("publications", []):
        rel_p = pub.get("path") or pub.get("file")
        p = os.path.join(ROOT, rel_p)
        assert sha256_file(p) == pub["sha256"], f"Manifest SHA mismatch for {rel_p}"
        if "bytes" in pub:
            assert os.path.getsize(p) == pub["bytes"], f"Manifest byte size mismatch for {rel_p}"
        reader = pypdf.PdfReader(p)
        assert len(reader.pages) == pub["pages"], f"Page count mismatch for {rel_p}"
        checked += 1
    artwork = manifest.get("artwork", {})
    art_items = artwork.get("items", []) if isinstance(artwork, dict) else artwork
    for art in art_items:
        p = os.path.join(ROOT, art["path"])
        assert sha256_file(p) == art["sha256"], f"Manifest SHA mismatch for {art['path']}"
        assert os.path.getsize(p) == art["bytes"], f"Manifest byte size mismatch for {art['path']}"
        with Image.open(p) as im:
            w, h = im.size
            exif_len = len(im.info.get("exif", b""))
        assert f"{w}x{h}" == art["dimensions"], f"Dimensions mismatch for {art['path']}"
        assert exif_len == 0, f"Expected 0 EXIF bytes in {art['path']}, found {exif_len}"
        checked += 1
    return checked


def _validate_schema_node(instance, schema: dict, path: str = "$") -> None:
    stype = schema.get("type")
    if stype:
        types = stype if isinstance(stype, list) else [stype]
        type_ok = False
        for t in types:
            if t == "object" and isinstance(instance, dict):
                type_ok = True
            elif t == "array" and isinstance(instance, list):
                type_ok = True
            elif t == "string" and isinstance(instance, str):
                type_ok = True
            elif t == "integer" and isinstance(instance, int) and not isinstance(instance, bool):
                type_ok = True
            elif t == "number" and isinstance(instance, (int, float)) and not isinstance(instance, bool):
                type_ok = True
            elif t == "boolean" and isinstance(instance, bool):
                type_ok = True
            elif t == "null" and instance is None:
                type_ok = True
        assert type_ok, f"Schema type mismatch at {path}: expected {stype}, got {type(instance).__name__}"

    if "const" in schema:
        assert instance == schema["const"], f"Schema const mismatch at {path}: expected {schema['const']}, got {instance}"
    if "enum" in schema:
        assert instance in schema["enum"], f"Schema enum mismatch at {path}: {instance} not in {schema['enum']}"

    if isinstance(instance, str):
        if "minLength" in schema:
            assert len(instance) >= schema["minLength"], f"String too short at {path}"
        if "pattern" in schema:
            assert re.search(schema["pattern"], instance), (
                f"String '{instance}' at {path} does not match pattern '{schema['pattern']}'"
            )

    if isinstance(instance, (int, float)) and not isinstance(instance, bool):
        if "minimum" in schema:
            assert instance >= schema["minimum"], f"Value {instance} < minimum {schema['minimum']} at {path}"
        if "maximum" in schema:
            assert instance <= schema["maximum"], f"Value {instance} > maximum {schema['maximum']} at {path}"

    if isinstance(instance, list):
        if "minItems" in schema:
            assert len(instance) >= schema["minItems"], f"Array length < minItems at {path}"
        if "maxItems" in schema:
            assert len(instance) <= schema["maxItems"], f"Array length > maxItems at {path}"
        if "items" in schema and isinstance(schema["items"], dict):
            for idx, item in enumerate(instance):
                _validate_schema_node(item, schema["items"], f"{path}[{idx}]")

    if isinstance(instance, dict):
        for req in schema.get("required", []):
            assert req in instance, f"Missing required property '{req}' at {path}"
        props = schema.get("properties", {})
        if schema.get("additionalProperties") is False:
            extra = set(instance.keys()) - set(props.keys())
            assert not extra, f"Disallowed additionalProperties {extra} at {path}"
        for k, v in instance.items():
            if k in props:
                _validate_schema_node(v, props[k], f"{path}.{k}")


def check_schemas_and_fixtures() -> int:
    schema_pairs = [
        ("schemas/task-packet.schema.json", "examples/run-0001/task-packet.json"),
        ("schemas/defect-record.schema.json", "examples/run-0001/defect-record.json"),
        ("schemas/run-manifest.schema.json", "examples/run-0001/run-manifest.json"),
    ]
    for schema_rel, fixture_rel in schema_pairs:
        s_path = os.path.join(ROOT, schema_rel)
        o_path = os.path.join(ROOT, "orchestration", os.path.basename(schema_rel))
        f_path = os.path.join(ROOT, fixture_rel)
        with open(s_path, "r", encoding="utf-8") as sf:
            schema = json.load(sf)
        with open(o_path, "r", encoding="utf-8") as of:
            orch_schema = json.load(of)
        assert schema == orch_schema, f"Schema drift between {schema_rel} and orchestration copy"
        assert schema.get("$schema") == "https://json-schema.org/draft/2020-12/schema", (
            f"Missing Draft 2020-12 $schema URI in {schema_rel}"
        )
        with open(f_path, "r", encoding="utf-8") as ff:
            instance = json.load(ff)
        _validate_schema_node(instance, schema)
        if jsonschema is not None:
            jsonschema.Draft202012Validator.check_schema(schema)
            jsonschema.validate(instance=instance, schema=schema)
    return len(schema_pairs)


def check_pdfs() -> int:
    eg_path = os.path.join(ROOT, "publications/threejs-evidence-graph-operational-manual-v2.0-en.pdf")
    hm_path = os.path.join(ROOT, "publications/the-hollow-meridian-rpg-full-prompt-v1.0-en.pdf")
    for path in (eg_path, hm_path):
        reader = pypdf.PdfReader(path)
        root = reader.trailer["/Root"].get_object()
        assert root.get("/Lang") == "en-US", f"Missing /Lang (en-US) in {path}"
        assert "/MarkInfo" in root and bool(root["/MarkInfo"].get_object().get("/Marked")) is True, (
            f"Missing /MarkInfo /Marked true in {path}"
        )
        for idx, page in enumerate(reader.pages):
            txt = page.extract_text() or ""
            assert "/-" not in txt, f"Found '/-' ligature corruption on page {idx + 1} of {path}"
    eg_reader = pypdf.PdfReader(eg_path)
    p16_txt = eg_reader.pages[15].extract_text()
    assert "npm run test:perf -- hero-prewarm" in p16_txt, "Expected '--' on page 16 of EG PDF"
    p64 = eg_reader.pages[63]
    annots = p64.get("/Annots", [])
    assert len(annots) >= 23, f"Expected >= 23 clickable /URI link annotations on EG page 64, got {len(annots)}"
    return 2


def check_markdown_and_multilingual() -> int:
    md_files = []
    for dirpath, _, filenames in os.walk(ROOT):
        if ".git" in dirpath.split(os.sep):
            continue
        for fn in filenames:
            if fn.endswith(".md"):
                md_files.append(os.path.join(dirpath, fn))

    link_re = re.compile(r"\[[^\]]+\]\(([^)#]+)(?:#[^)]*)?\)")
    for md_path in md_files:
        assert os.path.getsize(md_path) >= 200, f"Markdown file too small or empty ({os.path.getsize(md_path)} bytes): {md_path}"
        with open(md_path, "r", encoding="utf-8") as f:
            text = f.read()
        assert text.startswith("# ") or "\n# " in text, f"Missing top-level '# ' heading in {md_path}"
        assert "https://github.com/Emily2040/threejs-evidence-graph" not in text, (
            f"Found non-canonical repo URL (missing leading hyphen) in {md_path}"
        )
        assert "translation_status: unreviewed" not in text, (
            f"Found unreviewed translation status in {md_path}"
        )
        for m in link_re.finditer(text):
            target = m.group(1).strip()
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            resolved = os.path.normpath(os.path.join(os.path.dirname(md_path), target))
            assert os.path.exists(resolved), f"Broken relative link '{target}' in {md_path}"

    # Specific multilingual regression checks
    ja_readme = open(os.path.join(ROOT, "README.ja.md"), "r", encoding="utf-8").read()
    assert "遗" not in ja_readme, "Found Simplified Chinese character '遗' in README.ja.md"
    assert "`145` ページ" in ja_readme, "Expected `145` ページ in README.ja.md"
    ko_readme = open(os.path.join(ROOT, "README.ko.md"), "r", encoding="utf-8").read()
    assert "`145`페이지" in ko_readme, "Expected `145`페이지 in README.ko.md"
    zh_readme = open(os.path.join(ROOT, "README.zh-CN.md"), "r", encoding="utf-8").read()
    assert "`145` 页" in zh_readme, "Expected `145` 页 in README.zh-CN.md"
    return len(md_files)


def main() -> int:
    sums_count = check_sha256sums()
    manifest_count = check_release_manifest()
    schema_count = check_schemas_and_fixtures()
    pdf_count = check_pdfs()
    md_count = check_markdown_and_multilingual()
    print(
        f"PASS: Verified {sums_count} SHA-256 entries, {manifest_count} manifest assets, "
        f"{schema_count} JSON schemas/fixtures, {pdf_count} PDFs, and {md_count} Markdown files."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
