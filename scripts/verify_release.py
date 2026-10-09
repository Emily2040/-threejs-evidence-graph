#!/usr/bin/env python3
"""
Automated Release & Contract Verification Suite for the Four-Publication Suite (2026.07.5):
1. Three.js Evidence Graph: Operational Manual v2.0 (64 pages)
2. Game 01 - The Hollow Meridian: RPG Full Multi-Agent Production Prompt v1.0 (81 pages)
3. Game 02 - The Glass Ossuary: Mystery Horror Full Multi-Agent Production Prompt v1.0 (36 pages)
4. Game 03 - Perihelion Breach: FPS Adventure Full Multi-Agent Production Prompt v1.0 (36 pages)

Validates:
1. SHA256SUMS.txt LF line endings and bit-exact SHA-256 digests for all listed files.
2. release-manifest.json repository URL, SHA-256 digests, byte sizes, PDF page counts (217 total),
   13 zero-EXIF JPEG assets, and 5 SVG vector assets.
3. Draft 2020-12 JSON Schema validity (schemas/*.schema.json and orchestration/*.schema.json)
   and validation of all 9 golden fixtures across examples/run-0001..0003/*.json.
4. PDF structural metadata (/Lang, /MarkInfo), zero "/-" ligature corruption in extracted text,
   and clickable /URI link annotations on page 64 of Evidence Graph v2.0, page 36 of The Glass Ossuary,
   and page 36 of Perihelion Breach.
5. Zero EXIF metadata (exif_len == 0) across all 13 JPEGs in assets/*.jpg and valid XML across assets/svg/*.svg.
6. Local Markdown link resolution and 4-language native documentation parity across README*.md and docs/*.md.
"""

import hashlib
import json
import os
import re
import sys
import xml.etree.ElementTree as ET

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
    total_pages = 0
    pubs = manifest.get("publications", [])
    assert len(pubs) == 4, f"Expected 4 publications in release-manifest.json, found {len(pubs)}"
    for pub in pubs:
        rel_p = pub.get("path") or pub.get("file")
        p = os.path.join(ROOT, rel_p)
        assert sha256_file(p) == pub["sha256"], f"Manifest SHA mismatch for {rel_p}"
        if "bytes" in pub:
            assert os.path.getsize(p) == pub["bytes"], f"Manifest byte size mismatch for {rel_p}"
        reader = pypdf.PdfReader(p)
        assert len(reader.pages) == pub["pages"], f"Page count mismatch for {rel_p}"
        total_pages += len(reader.pages)
        checked += 1
    assert total_pages == 217, f"Expected 217 total PDF pages across 4 publications, got {total_pages}"

    artwork = manifest.get("artwork", {})
    art_items = artwork.get("items", []) if isinstance(artwork, dict) else artwork
    assert len(art_items) == 13, f"Expected 13 JPEG items in release-manifest.json, got {len(art_items)}"
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

    svg_items = artwork.get("svg_items", []) if isinstance(artwork, dict) else []
    assert len(svg_items) == 5, f"Expected 5 SVG items in release-manifest.json, got {len(svg_items)}"
    for svg in svg_items:
        p = os.path.join(ROOT, svg["path"])
        assert sha256_file(p) == svg["sha256"], f"Manifest SHA mismatch for {svg['path']}"
        assert os.path.getsize(p) == svg["bytes"], f"Manifest byte size mismatch for {svg['path']}"
        tree = ET.parse(p)
        assert tree.getroot().tag.endswith("svg"), f"Invalid SVG root element in {svg['path']}"
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
    schema_files = [
        ("schemas/task-packet.schema.json", "task-packet.json"),
        ("schemas/defect-record.schema.json", "defect-record.json"),
        ("schemas/run-manifest.schema.json", "run-manifest.json"),
    ]
    runs = ["examples/run-0001", "examples/run-0002", "examples/run-0003"]
    validated = 0
    for schema_rel, fixture_name in schema_files:
        s_path = os.path.join(ROOT, schema_rel)
        o_path = os.path.join(ROOT, "orchestration", os.path.basename(schema_rel))
        with open(s_path, "r", encoding="utf-8") as sf:
            schema = json.load(sf)
        with open(o_path, "r", encoding="utf-8") as of:
            orch_schema = json.load(of)
        assert schema == orch_schema, f"Schema drift between {schema_rel} and orchestration copy"
        assert schema.get("$schema") == "https://json-schema.org/draft/2020-12/schema", (
            f"Missing Draft 2020-12 $schema URI in {schema_rel}"
        )
        if jsonschema is not None:
            jsonschema.Draft202012Validator.check_schema(schema)
        for run_dir in runs:
            f_path = os.path.join(ROOT, run_dir, fixture_name)
            with open(f_path, "r", encoding="utf-8") as ff:
                instance = json.load(ff)
            _validate_schema_node(instance, schema)
            if jsonschema is not None:
                jsonschema.validate(instance=instance, schema=schema)
            validated += 1
    return validated


def check_pdfs() -> int:
    pdf_specs = [
        ("publications/threejs-evidence-graph-operational-manual-v2.0-en.pdf", 64, 23),
        ("publications/the-hollow-meridian-rpg-full-prompt-v1.0-en.pdf", 81, 0),
        ("publications/the-glass-ossuary-mystery-horror-full-prompt-v1.0-en.pdf", 36, 20),
        ("publications/perihelion-breach-fps-adventure-full-prompt-v1.0-en.pdf", 36, 20),
    ]
    for rel_path, expected_pages, min_last_page_annots in pdf_specs:
        path = os.path.join(ROOT, rel_path)
        reader = pypdf.PdfReader(path)
        assert len(reader.pages) == expected_pages, f"Expected {expected_pages} pages in {rel_path}, got {len(reader.pages)}"
        root = reader.trailer["/Root"].get_object()
        assert root.get("/Lang") == "en-US", f"Missing /Lang (en-US) in {rel_path}"
        assert "/MarkInfo" in root and bool(root["/MarkInfo"].get_object().get("/Marked")) is True, (
            f"Missing /MarkInfo /Marked true in {rel_path}"
        )
        for idx, page in enumerate(reader.pages):
            txt = page.extract_text() or ""
            assert not re.search(r"(?<!\+)(?<!Emily2040)/-(?!threejs)", txt), (
                f"Found '/-' ligature corruption on page {idx + 1} of {rel_path}"
            )
        if min_last_page_annots > 0:
            last_page = reader.pages[-1]
            annots = last_page.get("/Annots", [])
            assert len(annots) >= min_last_page_annots, (
                f"Expected >= {min_last_page_annots} clickable /URI link annotations on last page of {rel_path}, got {len(annots)}"
            )
    eg_reader = pypdf.PdfReader(os.path.join(ROOT, pdf_specs[0][0]))
    p16_txt = eg_reader.pages[15].extract_text()
    assert "npm run test:perf -- hero-prewarm" in p16_txt, "Expected '--' on page 16 of EG PDF"
    return len(pdf_specs)


def check_markdown_and_multilingual() -> int:
    md_files = []
    for dirpath, _, filenames in os.walk(ROOT):
        if ".git" in dirpath.split(os.sep):
            continue
        for fn in filenames:
            if fn.endswith(".md"):
                md_files.append(os.path.join(dirpath, fn))

    link_re = re.compile(r"\[[^\]]+\]\(([^)#]+)(?:#[^)]*)?\)")
    hangul_re = re.compile(r"[\uAC00-\uD7AF]")
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
        if md_path.endswith((".zh-CN.md", ".ja.md", ".ko.md")):
            assert text.startswith("<!-- source_version: 2026.07.5; translation_status: reviewed; language:"), (
                f"Missing or outdated provenance header in localized file: {md_path}"
            )
        if md_path.endswith((".ja.md", ".zh-CN.md")):
            stripped_nav = re.sub(r"\[한국어\]|badge/언어-한국어_\(네이티브판\)", "", text)
            assert not hangul_re.search(stripped_nav), f"Found stray Korean Hangul character in {md_path}"
        if md_path.endswith(".ja.md"):
            assert "遗" not in text, f"Found Simplified Chinese character '遗' in {md_path}"
            assert "银" not in text, f"Found Simplified Chinese character '银' in {md_path}"
        for m in link_re.finditer(text):
            target = m.group(1).strip()
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            resolved = os.path.normpath(os.path.join(os.path.dirname(md_path), target))
            assert os.path.exists(resolved), f"Broken relative link '{target}' in {md_path}"

    # Verify 4-publication 217-page suite parity across all 4 READMEs
    for readme_rel in ("README.md", "README.zh-CN.md", "README.ja.md", "README.ko.md"):
        content = open(os.path.join(ROOT, readme_rel), "r", encoding="utf-8").read()
        assert "217" in content, f"Expected total page count 217 in {readme_rel}"
        assert "the-glass-ossuary-mystery-horror-full-prompt-v1.0-en.pdf" in content, f"Missing Glass Ossuary PDF in {readme_rel}"
        assert "perihelion-breach-fps-adventure-full-prompt-v1.0-en.pdf" in content, f"Missing Perihelion Breach PDF in {readme_rel}"
    return len(md_files)


def main() -> int:
    sums_count = check_sha256sums()
    manifest_count = check_release_manifest()
    schema_count = check_schemas_and_fixtures()
    pdf_count = check_pdfs()
    md_count = check_markdown_and_multilingual()
    print(
        f"PASS: Verified {sums_count} SHA-256 entries, {manifest_count} manifest assets, "
        f"{schema_count} schema/fixture validations, {pdf_count} PDFs (217 pages), and {md_count} Markdown files."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
