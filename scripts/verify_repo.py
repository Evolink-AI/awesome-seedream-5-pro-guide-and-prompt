#!/usr/bin/env python3
"""Local structural verifier for the Seedream 5.0 Pro guide/prompt repo."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"


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
        "## ⚡ Quick Start",
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

    case_numbers = [int(match) for match in re.findall(r"^### Case ([0-9]+):", readme, flags=re.MULTILINE)]
    if case_numbers != list(range(1, len(case_numbers) + 1)) or len(case_numbers) < 3:
        fail(f"Case numbers are not contiguous from 1 or too few cases: {case_numbers}", failures)

    prompt_blocks = re.findall(r"\*\*Prompt:\*\*\n\n```\n.+?\n```", readme, flags=re.DOTALL)
    if len(prompt_blocks) != len(case_numbers):
        fail("Every case must have one visible text prompt block.", failures)

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
