# Maintenance

## Source Policy

- First scaffold uses owner-provided source material only.
- Do not invent prompts to fill missing cases.
- Community or X/Twitter updates must go through prompt curation before README mutation.
- Official-source-only cases use the README-level source policy and do not use pseudo-author labels.
- Private export URLs and section-level provenance stay in ignored local audit evidence, not in public README links or public source pages.
- Prompt text copied from owner-provided source material may be translated when the README is English, but the private source boundary must remain recorded in the run evidence.
- Collected GIFs from the official material must be embedded as GIFs when they are public cases; do not silently replace them with static PNG fallbacks.
- If a prompt has no paired public output image in the official material, keep it prompt-only instead of borrowing unrelated media.
- Owner-corrected case counts are part of the contract: `Interaction Control = 2` and `Layer Editing = 6`.

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
