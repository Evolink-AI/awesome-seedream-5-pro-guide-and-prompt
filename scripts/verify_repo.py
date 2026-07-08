#!/usr/bin/env python3
"""Local structural verifier for the Seedream 5.0 Pro guide/prompt repo."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
INVENTORY = ROOT / "data" / "official_case_inventory.json"
REMOVED_SOURCE_NOTE_TOKEN = "source" + "-notes"
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
    "layer-separation": 3,
    "multi-image-fusion-editing": 1,
    "visual-quality-narrative": 5,
    "multilingual-text-rendering": 5,
}
EXPECTED_PROMPT_CASES = {2, 13, 17}
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


def media_refs(text: str) -> list[str]:
    refs = re.findall(r"<img\s+[^>]*src=[\"']([^\"']+)[\"']", text)
    refs.extend(re.findall(r"!\[[^\]]*\]\(([^)]+)\)", text))
    return [ref for ref in refs if not ref.startswith("http")]


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
    if len(numbers) != 27:
        fail(f"{rel} must contain exactly 27 public cases, found {len(numbers)}.", failures)

    forbidden = [
        "**Source mapping:**",
        REMOVED_SOURCE_NOTE_TOKEN,
        "docs/" + REMOVED_SOURCE_NOTE_TOKEN + ".md",
        "@官方",
        "(by [@",
        "owner-provided launch export, section",
        "official section 3.1.1",
        "official section 3.1.3",
        "related different-case media",
    ]
    for token in forbidden:
        if token in text:
            fail(f"{rel} contains forbidden public provenance/source-mapping token: {token}", failures)

    prompt_count = text.count("**Prompt:**")
    if prompt_count != len(EXPECTED_PROMPT_CASES):
        fail(f"{rel} must contain {len(EXPECTED_PROMPT_CASES)} official prompt blocks, found {prompt_count}.", failures)
    for number in source_case_numbers:
        if f'<a id="case-{number}"></a>' not in text:
            fail(f"{rel} is missing explicit anchor for case {number}.", failures)

    refs = set(media_refs(text))
    if rel != "README.md" and refs != source_media_refs:
        missing = sorted(source_media_refs - refs)
        extra = sorted(refs - source_media_refs)
        if missing or extra:
            fail(f"{rel} media refs differ from README.md. Missing={missing}; extra={extra}", failures)
    for ref in refs:
        if not (ROOT / ref).is_file():
            fail(f"{rel} references missing media file: {ref}", failures)
    for stem in EXPECTED_GIF_STEMS:
        gif = f"assets/media/{stem}.gif"
        png = f"assets/media/{stem}.png"
        if gif not in text:
            fail(f"{rel} must reference collected GIF media: {gif}", failures)
        if png in text:
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
    if source_numbers != list(range(1, 28)):
        fail(f"README case numbers must be contiguous 1..27: {source_numbers}", failures)
    if readme.count("**Prompt:**") != len(EXPECTED_PROMPT_CASES):
        fail("README prompt block count must match official prompt-bearing cases only.")

    categories = inventory.get("case_categories", [])
    cases = inventory.get("cases", [])
    actual_counts = {item.get("id"): len(item.get("case_numbers", [])) for item in categories}
    if actual_counts != EXPECTED_CATEGORY_COUNTS:
        fail(f"Inventory category counts do not match expected menu: {actual_counts}", failures)
    if len(cases) != 27:
        fail(f"Inventory must list 27 public cases, found {len(cases)}.", failures)
    prompt_cases = {item.get("case") for item in cases if item.get("has_prompt")}
    if prompt_cases != EXPECTED_PROMPT_CASES:
        fail(f"Inventory prompt-bearing cases must be {sorted(EXPECTED_PROMPT_CASES)}, found {sorted(prompt_cases)}.", failures)

    for cat_id, expected in EXPECTED_CATEGORY_COUNTS.items():
        if f'<a id="{cat_id}"></a>' not in readme:
            fail(f"README missing category anchor: {cat_id}", failures)
        if f"Case count: **{expected}**." not in readme:
            fail(f"README missing visible case count for {cat_id}: {expected}", failures)

    if '<td width="50%" valign="top">' not in readme.split('### Case 13:', 1)[1].split('---', 1)[0]:
        fail("Case 13 before/after comparison must display both images in one row.")
    if "assets/media/014-Feishu-Docs-Image.gif" not in readme:
        fail("Material editing GIF must be represented as its own layer-editing case.")
    if "Multi-image Fusion Editing" not in readme or "paired public output image" not in readme:
        fail("Multi-image fusion must remain prompt-only when no paired public output image is available.")

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
