## Summary

- 

## Verification

- [ ] `python3 scripts/verify_repo.py --repo .`
- [ ] `python3 scripts/audit_public_surface.py --repo . --out local-audits/<run>/public-surface-link-audit.md`
- [ ] `git diff --check`

## Source Policy

- [ ] No invented prompts or unsupported model/API claims
- [ ] Private source URLs are not exposed in public files
- [ ] EvoLink links use the expected target and UTM parameters
