#!/usr/bin/env python3
"""Fail-fast audit for localized README translation completeness."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_CASES = 25

GLOBAL_BAD = [
    "Awesome Seedream 5.0 Pro Guide and Prompt",
    "Source-backed guide, prompt patterns, and visual examples",
    "[![Use on EvoLink]",
    "[![Get API Key]",
    "Introduction",
    "News",
    "Model Notes",
    "Acknowledge",
    "Source policy",
    "source pages",
    "source page",
    "source URL",
    "audit evidence",
    "Audit-Evidenz",
    "launch material",
    "case inventory",
    "owner",
    "Owner",
    "Source-URLs",
    "Runtime evidence",
    "runtime evidence",
    "API-run",
    "visible case",
    "visible cases",
]

LOCALIZED = {
    "README_es.md": {
        "lang": "Spanish",
        "bad": ["Schnellstart", "Nutze ", "Pfeile "],
    },
    "README_pt.md": {
        "lang": "Portuguese",
        "bad": ["Guía", "El material", "Esta guía", "Usa este repositorio", "Prueba el", "Novedades", "Edición"],
    },
    "README_ja.md": {
        "lang": "Japanese",
        "bad": ["Schnellstart", "Nutze ", "公開 source", "ケース inventory"],
    },
    "README_ko.md": {
        "lang": "Korean",
        "bad": ["編集前", "公式資料", "このリポジトリ", "모델入口", "source page", "source URL"],
    },
    "README_de.md": {
        "lang": "German",
        "bad": [],
    },
    "README_fr.md": {
        "lang": "French",
        "bad": ["Im offiziellen", "Dieser Leitfaden", "Nutze ", "Schnellstart", "Pfeile ", "Objektbeschreibung"],
    },
    "README_tr.md": {
        "lang": "Turkish",
        "bad": ["Im offiziellen", "Dieser Leitfaden", "Nutze ", "Schnellstart", "Pfeile ", "Objektbeschreibung"],
    },
    "README_zh-TW.md": {
        "lang": "Traditional Chinese",
        "bad": ["Source policy"],
    },
    "README_zh-CN.md": {
        "lang": "Simplified Chinese",
        "bad": ["Source policy"],
    },
    "README_ru.md": {
        "lang": "Russian",
        "bad": ["Im offiziellen", "Dieser Leitfaden", "Nutze ", "Schnellstart", "Pfeile ", "Objektbeschreibung"],
    },
}

STRUCTURAL_ALLOWED = {"Case", "Prompt", "Seedream", "Seedance", "EvoLink", "ModelArk", "API", "README", "Lark", "Feishu"}


def case_count(text: str) -> int:
    return len(re.findall(r"^### Case [0-9]+:", text, re.MULTILINE))


def prompt_block_count(text: str) -> int:
    return len(re.findall(r"^\*\*Prompt:\*\*$", text, re.MULTILINE))


def main() -> int:
    failures: list[str] = []
    for rel, cfg in LOCALIZED.items():
        path = ROOT / rel
        if not path.is_file():
            failures.append(f"{rel}: missing localized README")
            continue
        text = path.read_text(encoding="utf-8")
        if case_count(text) != EXPECTED_CASES:
            failures.append(f"{rel}: expected {EXPECTED_CASES} cases, found {case_count(text)}")
        if prompt_block_count(text) != 3:
            failures.append(f"{rel}: expected 3 official prompt text blocks, found {prompt_block_count(text)}")
        for token in [*GLOBAL_BAD, *cfg["bad"]]:
            if token in text:
                failures.append(f"{rel}: {cfg['lang']} translation contains stale or wrong-language token: {token!r}")
        if "Case 16: Recombined" in text or "Case count: **3**." in text:
            failures.append(f"{rel}: stale former Case 16 / Layer Separation count remains")

    print("# Translation Completeness Verification")
    print()
    print(f"- Checked files: {len(LOCALIZED)}")
    if failures:
        print(f"- Result: FAIL ({len(failures)} issue(s))")
        print()
        for item in failures:
            print(f"- {item}")
        return 1
    print("- Result: PASS")
    print("- Structural terms intentionally allowed: " + ", ".join(sorted(STRUCTURAL_ALLOWED)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
