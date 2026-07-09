#!/usr/bin/env python3
"""Local structural verifier for the Seedream 5.0 Pro guide/prompt repo."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
INVENTORY = ROOT / "data" / "official_case_inventory.json"
REMOVED_SOURCE_NOTE_TOKEN = "source" + "-notes"
COMMUNITY_R2_PREFIX = (
    "https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/"
    "github-repo-media/awesome-seedream-5-pro-guide-and-prompt/downloaded-media/media/"
)
LOCALIZED_READMES = [
    "README.md",
    "README_es.md",
    "README_pt.md",
    "README_ja.md",
    "README_ko.md",
    "README_de.md",
    "README_fr.md",
    "README_tr.md",
    "README_zh-TW.md",
    "README_zh-CN.md",
    "README_ru.md",
]
EXPECTED_CATEGORY_COUNTS = {
    "interaction-control": 2,
    "sketch-editing": 4,
    "layer-editing": 6,
    "anchor-position-editing": 1,
    "layer-separation": 1,
    "multi-image-fusion-editing": 1,
    "visual-quality-narrative": 5,
    "multilingual-text-rendering": 5,
}
EXPECTED_COMMUNITY_CATEGORY_COUNTS = {
    "community-editing-control": 3,
    "community-product-interface-design": 4,
    "community-technical-structured-visuals": 4,
    "community-cinematic-character-visuals": 10,
    "community-concept-environment-worldbuilding": 3,
    "community-model-comparisons": 11,
}
EXPECTED_PROMPT_CASES = {2, 13, 15}
EXPECTED_GIF_STEMS = {
    "003-arrows-annotation-boxes",
    "004-Red-box-A-huge-blue-furred-head-with-a-ferocious-squished-ex",
    "005-doodles",
    "006-color-block",
    "007-lines",
    "008-simple-sketches",
    "009-Feishu-Docs-Image",
    "010-Feishu-Docs-Image",
    "011-Feishu-Docs-Image",
    "012-Feishu-Docs-Image",
    "013-Feishu-Docs-Image",
    "014-Feishu-Docs-Image",
}


def fail(message: str, failures: list[str]) -> None:
    failures.append(message)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def case_numbers(text: str) -> list[int]:
    return [int(match) for match in re.findall(r"^### Case ([0-9]+):", text, re.MULTILINE)]


def community_case_numbers(text: str) -> list[int]:
    return [int(match) for match in re.findall(r"^### Community Use Case ([0-9]+):", text, re.MULTILINE)]


def media_refs(text: str, *, local_only: bool = True) -> list[str]:
    refs = re.findall(r"<img\s+[^>]*src=[\"']([^\"']+)[\"']", text)
    refs.extend(re.findall(r"!\[[^\]]*\]\(([^)]+)\)", text))
    if local_only:
        return [ref for ref in refs if not ref.startswith("http")]
    return refs


def ref_mentions_path(ref: str, rel: str) -> bool:
    if ref == rel:
        return True
    if ref.startswith("http://") or ref.startswith("https://"):
        path = unquote(urlparse(ref).path.lstrip("/"))
        return path.endswith(rel) or f"/{rel}" in f"/{path}"
    return False


def text_mentions_media(text: str, rel: str) -> bool:
    return any(ref_mentions_path(ref, rel) for ref in media_refs(text, local_only=False))


def load_inventory(failures: list[str]) -> dict:
    try:
        data = json.loads(read_text(INVENTORY))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"Cannot read valid inventory JSON: {exc}", failures)
        return {"case_categories": [], "cases": []}
    return data


def verify_readme(rel: str, source_case_numbers: list[int], source_media_refs: set[str], failures: list[str]) -> None:
    path = ROOT / rel
    if not path.is_file():
        fail(f"Missing localized README: {rel}", failures)
        return

    text = read_text(path)
    numbers = case_numbers(text)
    if numbers != source_case_numbers:
        fail(f"{rel} case numbers differ from README.md: {numbers}", failures)
    if len(numbers) != 25:
        fail(f"{rel} must contain exactly 25 public cases, found {len(numbers)}.", failures)

    public_official_text = text.split('<a id="community-use-cases"></a>', 1)[0]
    forbidden = [
        "**Source mapping:**",
        REMOVED_SOURCE_NOTE_TOKEN,
        "docs/" + REMOVED_SOURCE_NOTE_TOKEN + ".md",
        "@官方",
        "owner-provided launch export, section",
        "official section 3.1.1",
        "official section 3.1.3",
        "related different-case media",
    ]
    for token in forbidden:
        if token in text:
            fail(f"{rel} contains forbidden public provenance/source-mapping token: {token}", failures)
    if "(by [@" in public_official_text:
        fail(f"{rel} official gallery contains community-style author attribution.", failures)

    prompt_count = text.count("**Prompt:**")
    if prompt_count != len(EXPECTED_PROMPT_CASES):
        fail(f"{rel} must contain {len(EXPECTED_PROMPT_CASES)} official prompt blocks, found {prompt_count}.", failures)
    for number in source_case_numbers:
        if f'<a id="case-{number}"></a>' not in text:
            fail(f"{rel} is missing explicit anchor for case {number}.", failures)
    community_numbers = community_case_numbers(text)
    if community_numbers != list(range(1, 36)):
        fail(f"{rel} community use case numbers must be contiguous 1..35: {community_numbers}", failures)
    if '<a id="community-use-cases"></a>' not in text:
        fail(f"{rel} is missing Community Use Cases section.", failures)
    community_text = text.split('<a id="community-use-cases"></a>', 1)[1]
    if 'src="downloaded-media/' in community_text or "src='downloaded-media/" in community_text:
        fail(f"{rel} community use cases must reference R2 media URLs, not downloaded-media local paths.", failures)
    for slug in EXPECTED_COMMUNITY_CATEGORY_COUNTS:
        if f'<a id="{slug}"></a>' not in text:
            fail(f"{rel} is missing community category anchor: {slug}", failures)

    refs = set(media_refs(text))
    all_refs = set(media_refs(text, local_only=False))
    all_source_refs = set(media_refs(read_text(ROOT / "README.md"), local_only=False))
    if rel != "README.md" and refs != source_media_refs:
        missing = sorted(source_media_refs - refs)
        extra = sorted(refs - source_media_refs)
        if missing or extra:
            fail(f"{rel} media refs differ from README.md. Missing={missing}; extra={extra}", failures)
    if rel != "README.md" and all_refs != all_source_refs:
        missing = sorted(all_source_refs - all_refs)
        extra = sorted(all_refs - all_source_refs)
        if missing or extra:
            fail(f"{rel} all media refs differ from README.md. Missing={missing}; extra={extra}", failures)
    for ref in refs:
        if not (ROOT / ref).is_file():
            fail(f"{rel} references missing media file: {ref}", failures)
    for stem in EXPECTED_GIF_STEMS:
        gif = f"assets/media/{stem}.gif"
        png = f"assets/media/{stem}.png"
        if not text_mentions_media(text, gif):
            fail(f"{rel} must reference collected GIF media: {gif}", failures)
        if text_mentions_media(text, png):
            fail(f"{rel} must not use static PNG fallback for collected GIF media: {png}", failures)


def main() -> int:
    failures: list[str] = []
    readme = read_text(README)
    inventory = load_inventory(failures)
    first_screen = "\n".join(readme.splitlines()[:120])

    for rel in [
        "README.md",
        "LICENSE",
        ".gitignore",
        "CONTRIBUTING.md",
        "CODE_OF_CONDUCT.md",
        "SECURITY.md",
        "docs/update-log.md",
        "docs/maintenance.md",
        "data/ingested_tweets.json",
        "data/official_case_inventory.json",
    ]:
        if not (ROOT / rel).is_file():
            fail(f"Missing required file: {rel}", failures)
    if (ROOT / "README_en.md").exists():
        fail("README_en.md must not exist; English source is README.md.", failures)

    required_snippets = [
        "Seedream 5.0 Pro",
        "utm_source=github",
        "https://evolink.ai/seedream-5-0-pro",
        "https://evolink.ai/dashboard/keys",
        "does not claim that an EvoLink Seedream 5.0 Pro first-run API route has been verified",
        "Source policy: official",
    ]
    for snippet in required_snippets:
        if snippet not in readme:
            fail(f"README missing required snippet: {snippet}", failures)
    if "guide and prompt" not in readme.lower():
        fail("README missing required repository role phrase: guide and prompt", failures)
    if 'src="assets/banner.png"' not in first_screen:
        fail("First screen must reference the owner-provided banner image.", failures)

    source_numbers = case_numbers(readme)
    if source_numbers != list(range(1, 26)):
        fail(f"README case numbers must be contiguous 1..25: {source_numbers}", failures)
    if readme.count("**Prompt:**") != len(EXPECTED_PROMPT_CASES):
        fail("README prompt block count must match official prompt-bearing cases only.", failures)

    categories = inventory.get("case_categories", [])
    cases = inventory.get("cases", [])
    actual_counts = {item.get("id"): len(item.get("case_numbers", [])) for item in categories}
    if actual_counts != EXPECTED_CATEGORY_COUNTS:
        fail(f"Inventory category counts do not match expected menu: {actual_counts}", failures)
    if len(cases) != 25:
        fail(f"Inventory must list 25 public cases, found {len(cases)}.", failures)
    prompt_cases = {item.get("case") for item in cases if item.get("has_prompt")}
    if prompt_cases != EXPECTED_PROMPT_CASES:
        fail(f"Inventory prompt-bearing cases must be {sorted(EXPECTED_PROMPT_CASES)}, found {sorted(prompt_cases)}.", failures)

    for cat_id, expected in EXPECTED_CATEGORY_COUNTS.items():
        if f'<a id="{cat_id}"></a>' not in readme:
            fail(f"README missing category anchor: {cat_id}", failures)

    use_cases_path = ROOT / "data" / "use-cases.json"
    try:
        use_cases = json.loads(read_text(use_cases_path))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"Cannot read valid use case JSON: {exc}", failures)
        use_cases = {"items": []}
    if use_cases.get("official_case_count") != 25:
        fail("data/use-cases.json must record official_case_count=25.", failures)
    if use_cases.get("community_usecase_count") != 35:
        fail("data/use-cases.json must record community_usecase_count=35.", failures)
    community_items = use_cases.get("items", [])
    if len(community_items) != 35:
        fail(f"data/use-cases.json must contain 35 community items, found {len(community_items)}.", failures)
    for item in community_items:
        for key in ["source_url", "author_url", "title", "date", "type", "category", "category_label", "tags", "takeaway", "dedup_key", "local_media_files", "r2_media_urls", "prompt_text"]:
            if key not in item:
                fail(f"Community use case item missing key {key}: {item.get('number')}", failures)
        local_media_files = item.get("local_media_files", [])
        r2_media_urls = item.get("r2_media_urls", [])
        if len(r2_media_urls) != len(local_media_files):
            fail(f"Community use case item {item.get('number')} must have one R2 URL per local media file.", failures)
        for rel_media, r2_url in zip(local_media_files, r2_media_urls):
            if not (ROOT / rel_media).is_file():
                fail(f"Community use case media file is missing: {rel_media}", failures)
            expected_url = COMMUNITY_R2_PREFIX + rel_media.rsplit("downloaded-media/media/", 1)[-1]
            if r2_url != expected_url:
                fail(f"Community use case item {item.get('number')} has unexpected R2 media URL: {r2_url}", failures)
            if not text_mentions_media(readme, rel_media):
                fail(f"README does not reference uploaded community media: {rel_media}", failures)

    if '<td width="50%" valign="top">' not in readme.split('### Case 13:', 1)[1].split('---', 1)[0]:
        fail("Case 13 before/after comparison must display both images in one row.", failures)
    layer_section = readme.split('<a id="layer-separation"></a>', 1)[1].split('<a id="multi-image-fusion-editing"></a>', 1)[0]
    if "#case-15" in layer_section or '<a id="case-15"></a>' in layer_section or "assets/media/018-Feishu-Docs-Image.png" in layer_section or "assets/media/019-Feishu-Docs-Image.png" in layer_section:
        fail("Layer Separation must not list Case 15 or media 018/019; those form the Multi-image Fusion input-output case.", failures)
    case15 = readme.split("### Case 15:", 1)[1].split("---", 1)[0] if "### Case 15:" in readme else ""
    if not text_mentions_media(case15, "assets/media/018-Feishu-Docs-Image.png") or not text_mentions_media(case15, "assets/media/019-Feishu-Docs-Image.png"):
        fail("Case 15 must merge former media 018/019 as one Multi-image Fusion input-output pair.", failures)
    if "**Prompt:**" not in case15:
        fail("Case 15 must keep the official seven-reference prompt with the input-output media pair.", failures)
    if not text_mentions_media(readme, "assets/media/014-Feishu-Docs-Image.gif"):
        fail("Material editing GIF must be represented as its own layer-editing case.", failures)
    multi_section = readme.split('<a id="multi-image-fusion-editing"></a>', 1)[1].split('<a id="visual-quality-narrative"></a>', 1)[0]
    if "### Case 15:" not in multi_section:
        fail("Multi-image Fusion must contain exactly Case 15 after merging former cases 15/16.", failures)

    source_refs = set(media_refs(readme))
    for rel in LOCALIZED_READMES:
        verify_readme(rel, source_numbers, source_refs, failures)

    oversized = [
        str(path.relative_to(ROOT))
        for path in (ROOT / "assets").rglob("*")
        if path.is_file() and path.stat().st_size > 25 * 1024 * 1024
    ]
    if oversized:
        fail("Media files exceed 25 MB without approval: " + ", ".join(oversized), failures)

    accidental = []
    for pattern in [".DS_Store", "__pycache__", "*.pyc"]:
        accidental.extend(str(path.relative_to(ROOT)) for path in ROOT.rglob(pattern))
    if accidental:
        fail("Accidental generated/system files found: " + ", ".join(sorted(accidental)), failures)

    print("# Local Repo Verification")
    print()
    print(f"- Repository: `{ROOT}`")
    print(f"- README cases: {len(source_numbers)}")
    print(f"- Official prompt blocks: {readme.count('**Prompt:**')}")
    print(f"- Category counts: {EXPECTED_CATEGORY_COUNTS}")
    print(f"- README media refs: {len(source_refs)}")
    print(f"- Oversized media files: {len(oversized)}")
    print(f"- Result: {'FAIL' if failures else 'PASS'}")
    if failures:
        print()
        print("## Failures")
        for item in failures:
            print(f"- {item}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
