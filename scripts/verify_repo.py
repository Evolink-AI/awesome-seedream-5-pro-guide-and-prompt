#!/usr/bin/env python3
"""Local structural verifier for the Seedream 5.0 Pro guide/prompt repo."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
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


def fail(message: str, failures: list[str]) -> None:
    failures.append(message)


def heading_index(text: str, heading: str) -> int:
    return text.find(heading)


def main() -> int:
    failures: list[str] = []
    readme = README.read_text(encoding="utf-8")
    first_screen = "\n".join(readme.splitlines()[:120])

    required_files = [
        "README.md",
        "LICENSE",
        ".gitignore",
        "data/ingested_tweets.json",
        "docs/update-log.md",
        "docs/maintenance.md",
        "docs/source-notes.md",
    ]
    for rel in required_files:
        if not (ROOT / rel).is_file():
            fail(f"Missing required file: {rel}", failures)
    for rel in LOCALIZED_READMES:
        if not (ROOT / rel).is_file():
            fail(f"Missing localized README file: {rel}", failures)
    if (ROOT / "README_en.md").exists():
        fail("README_en.md must not exist; English source is README.md.", failures)

    if "{{" in readme or "}}" in readme or "Placeholder" in readme or "post-link" in readme:
        fail("README contains scaffold placeholder text.", failures)

    for snippet in [
        "Seedream 5.0 Pro",
        "guide and prompt",
        "utm_source=github",
        "utm_content=",
        "https://evolink.ai/dashboard/keys",
        "current repository does not claim that an EvoLink Seedream 5.0 Pro first-run API route has been verified",
    ]:
        if snippet not in readme:
            fail(f"README missing required snippet: {snippet}", failures)

    if not re.search(r"<img\s+[^>]*src=[\"']assets/(?:banner\.png|media/002-performance\.jpg)[\"']", first_screen):
        fail("First screen does not reference the banner/media image.", failures)

    ordered = [
        "## 🍌 Introduction",
        "## 📰 News",
        "## 📑 Menu",
        "## 🎛️ Controlled Editing Prompt Patterns",
        "## 🙏 Acknowledge",
    ]
    positions = [heading_index(readme, item) for item in ordered]
    for item, position in zip(ordered, positions):
        if position < 0:
            fail(f"Missing required heading: {item}", failures)
    if positions != sorted(positions):
        fail("Required headings are not in the expected order.", failures)
    if "Quick start:" not in readme or "Get your EvoLink API key" not in readme:
        fail("README does not show a visible conversion path before the first case section.", failures)

    case_heading_re = re.compile(r"^### Case ([0-9]+): \[.+\]\(.+\) \(by \[@.+\]\(.+\)\)$", re.MULTILINE)
    case_numbers = [int(match[0]) for match in case_heading_re.findall(readme)]
    if case_numbers != list(range(1, len(case_numbers) + 1)) or len(case_numbers) < 3:
        fail(f"Case headings are not template-compliant or case numbers are not contiguous: {case_numbers}", failures)
    for number in case_numbers:
        anchor = f'<a id="case-{number}"></a>'
        if anchor not in readme:
            fail(f"Missing explicit case anchor: {anchor}", failures)

    prompt_blocks = re.findall(r"\*\*Prompt:\*\*\n\n```\n.+?\n```", readme, flags=re.DOTALL)
    if len(prompt_blocks) != len(case_numbers):
        fail("Every case must have one visible text prompt block.", failures)
    if readme.count("Source: 官方.") != len(case_numbers):
        fail("Official-source cases must use the public source label `Source: 官方.`.", failures)
    if "## 🎬 Visual Capability Gallery" in readme:
        gallery = readme.split("## 🎬 Visual Capability Gallery", 1)[1].split("## 🧩 Model Notes", 1)[0]
        if gallery.count("<table>") != 1:
            fail("Gallery must use one HTML table.", failures)
        if '<td width="50%" valign="top">' not in gallery:
            fail("Gallery cells must use width=\"50%\" valign=\"top\".", failures)
        if "**Prompt:**" in gallery or "Source:" in gallery or "---" in gallery:
            fail("Gallery must not contain prompt blocks, Source lines, or separators.", failures)

    media_refs = re.findall(r"\]\((assets/media/[^)]+)\)", readme)
    media_refs.extend(re.findall(r"<img\s+[^>]*src=[\"'](assets/[^\"']+)[\"']", readme))
    for rel in media_refs:
        if not (ROOT / rel).is_file():
            fail(f"Missing media file referenced by README: {rel}", failures)

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

    source_headings = [line for line in readme.splitlines() if line.startswith("## ")]
    source_case_count = len(case_numbers)
    for rel in LOCALIZED_READMES[1:]:
        localized = (ROOT / rel).read_text(encoding="utf-8")
        localized_headings = [line for line in localized.splitlines() if line.startswith("## ")]
        if len(localized_headings) != len(source_headings):
            fail(f"{rel} top-level heading count differs from README.md.", failures)
        localized_case_count = len(re.findall(r"^### Case [0-9]+:", localized, flags=re.MULTILINE))
        if localized_case_count != source_case_count:
            fail(f"{rel} case count differs from README.md.", failures)
        for media_ref in re.findall(r"(?:src=|\]\()(?:\"|')?(assets/[^\"')]+)", localized):
            if not (ROOT / media_ref).is_file():
                fail(f"{rel} references missing media file: {media_ref}", failures)

    print("# Local Repo Verification")
    print()
    print(f"- Repository: `{ROOT}`")
    print(f"- README cases: {len(case_numbers)}")
    print(f"- README media refs: {len(media_refs)}")
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
