# Contributing

This repository accepts issues and pull requests that improve source-backed Seedream 5.0 Pro guide content, prompt formatting, media references, link health, and EvoLink conversion-path clarity.

## What To Submit

- Fix broken links, anchors, media paths, or UTM parameters.
- Improve official-source-backed wording without adding unsupported claims.
- Add prompt examples only when the prompt text comes from official source material or an approved public source.
- Improve documentation, provenance notes, or maintenance scripts.

## Source Rules

- Do not invent prompts, model IDs, benchmark claims, pricing, availability, or API behavior.
- Use `Source: 官方.` for current official-source cases unless a future public source policy changes.
- Keep private source URLs out of public files.
- Put comparison images on the same row when they are meant to be read together.

## Pull Request Checklist

- `python3 scripts/verify_repo.py` passes.
- `python3 scripts/audit_public_surface.py --repo . --out local-audits/<run>/public-surface-link-audit.md` has no unresolved P0/P1 failures or documents the blocker.
- `git diff --check` passes.
- New public links are action-labeled and use the expected UTM parameters when they point to EvoLink.
