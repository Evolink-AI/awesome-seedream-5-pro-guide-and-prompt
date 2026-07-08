# Maintenance

## Source Policy

- First scaffold uses owner-provided source material only.
- Do not invent prompts to fill missing cases.
- Community or X/Twitter updates must go through prompt curation before README mutation.
- Prompt text copied from Chinese source material may be translated when the README is English, but the source section must be recorded in the case notes.

## Update Cadence

- Manual updates until a recurring prompt update loop is explicitly approved.
- Each update should record selected, deferred, unsure, and dropped counts.

## Verification

Before public release, run:

```bash
python3 scripts/verify_repo.py
python3 scripts/audit_public_surface.py --repo . --out local-audits/<run-id>/public-surface-link-audit.md
git diff --check
find . \( -name .DS_Store -o -name __pycache__ -o -name '*.pyc' \) -print
```

Public release also needs owner-approved GitHub repository creation, push evidence, About metadata verification, and a decision on real EvoLink API smoke-test evidence or waiver.
