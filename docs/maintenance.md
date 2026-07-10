# Maintenance

## Source Policy

- First scaffold uses owner-provided source material only.
- Do not invent prompts to fill missing cases.
- Community or X/Twitter updates must go through the model-repo usecase update loop before README mutation.
- Official-source-only cases use the README-level source policy and do not use pseudo-author labels.
- Private export URLs and section-level provenance stay in ignored local audit evidence, not in public README links or public source pages.
- Prompt text copied from owner-provided source material may be translated when the README is English, but the private source boundary must remain recorded in the run evidence.
- Collected GIFs from the official material must be embedded as GIFs when they are public cases; do not silently replace them with static PNG fallbacks.
- If a prompt has no paired public output image in the official material, keep it prompt-only instead of borrowing unrelated media.
- Owner-corrected case counts are part of the contract: `Interaction Control = 2` and `Layer Editing = 6`.

## Community Case Rendering

- JSON, scripts, raw collections, and audit runtime artifacts are local-only and ignored by this public repository.
- Public delivery consists of the rendered README files and public maintenance documentation.
- Run the canonical model-repo pipeline agent from its own repository; do not copy its verifier or working data into this public repository.
- Images render directly from R2. Multiple images for one case render in one table row.
- GIFs render directly from their R2 GIF URL; do not substitute a static image when the GIF is the evidence.
- Videos render as a poster frame linked to the playable R2 video URL; do not use a direct-download presentation.
- Prompt blocks preserve the source prompt byte-for-byte across every locale. Cases without a public exact prompt do not invent one.

## Update Cadence

- Manual updates until a recurring prompt update loop is explicitly approved.
- Each update should record selected, deferred, unsure, and dropped counts.

## Verification

Before public release, run:

```bash
python3 /path/to/model-repo-pipeline/bundled-skills/usecase-update-loop/scripts/verify_usecase_update.py --repo .
git diff --check
find . \( -name .DS_Store -o -name __pycache__ -o -name '*.pyc' \) -print
```

Public release also needs owner-approved GitHub repository creation, push evidence, About metadata verification, and a decision on real EvoLink API smoke-test evidence or waiver.
