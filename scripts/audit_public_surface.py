#!/usr/bin/env python3
"""Audit public README/docs links, anchors, relative files, media, and EvoLink UTM tags."""

from __future__ import annotations

import argparse
import re
import sys
import time
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import parse_qs, urldefrag, urlparse


MARKDOWN_LINK_RE = re.compile(r"(!?)\[([^\]]*)\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
HTML_LINK_RE = re.compile(r"<a\s+[^>]*href=[\"']([^\"']+)[\"']", re.IGNORECASE)
HTML_IMG_RE = re.compile(r"<img\s+[^>]*src=[\"']([^\"']+)[\"']", re.IGNORECASE)
RAW_URL_RE = re.compile(r"https?://[^\s<>)\"]+")


@dataclass
class Finding:
    severity: str
    file: str
    target: str
    detail: str


def slugify_heading(heading: str) -> str:
    heading = re.sub(r"^#+\s*", "", heading).strip().lower()
    heading = heading.encode("ascii", "ignore").decode("ascii")
    heading = re.sub(r"[^\w\s-]", "", heading)
    heading = re.sub(r"\s+", "-", heading)
    return heading


def anchors_for(text: str) -> set[str]:
    anchors: set[str] = set()
    for line in text.splitlines():
        if line.startswith("#"):
            anchors.add(slugify_heading(line))
    anchors.update(re.findall(r"<a\s+id=[\"']([^\"']+)[\"']", text, flags=re.IGNORECASE))
    return anchors


def public_files(root: Path) -> list[Path]:
    files = sorted(root.glob("README*.md"))
    files.extend(sorted((root / "docs").glob("**/*.md")) if (root / "docs").is_dir() else [])
    return [path for path in files if path.is_file()]


def extract_targets(text: str) -> list[tuple[str, str]]:
    targets: list[tuple[str, str]] = []
    for is_image, label, target in MARKDOWN_LINK_RE.findall(text):
        targets.append(("image" if is_image else "link", target.strip()))
    for target in HTML_LINK_RE.findall(text):
        targets.append(("html-link", target.strip()))
    for target in HTML_IMG_RE.findall(text):
        targets.append(("html-image", target.strip()))
    known = {target for _, target in targets}
    for target in RAW_URL_RE.findall(text):
        if target not in known:
            targets.append(("raw-url", target.strip().rstrip(".,;")))
    return targets


def request_http(url: str, timeout: int, method: str) -> tuple[bool, str]:
    headers = {"User-Agent": "model-repo-link-audit/1.0"}
    if method == "GET":
        headers["Range"] = "bytes=0-0"
    request = urllib.request.Request(url, method=method, headers=headers)
    with urllib.request.urlopen(request, timeout=timeout) as response:
        status = response.getcode()
        final_url = response.geturl()
        if 200 <= status < 400:
            if final_url != url:
                return True, f"{status}, redirected to {final_url}"
            return True, str(status)
        return False, f"HTTP {status}"


def check_http(url: str, timeout: int) -> tuple[bool, str]:
    last_error = ""
    for attempt in range(3):
        try:
            return request_http(url, timeout, "HEAD")
        except urllib.error.HTTPError as exc:
            if exc.code in {403, 405, 501}:
                try:
                    return request_http(url, timeout, "GET")
                except urllib.error.HTTPError as get_exc:
                    return False, f"HTTP {get_exc.code}"
                except Exception as get_exc:
                    last_error = get_exc.__class__.__name__
            else:
                return False, f"HTTP {exc.code}"
        except Exception as exc:
            last_error = exc.__class__.__name__
            if attempt < 2:
                time.sleep(1.5 * (attempt + 1))
    return False, last_error


def is_evolink_owned(url: str) -> bool:
    host = urlparse(url).netloc.lower()
    return host == "evolink.ai" or host.endswith(".evolink.ai")


def check_utm(url: str) -> str | None:
    parsed = urlparse(url)
    query = parse_qs(parsed.query)
    if query.get("utm_source", [""])[0] != "github":
        return "missing utm_source=github"
    if not query.get("utm_campaign", [""])[0]:
        return "missing utm_campaign"
    if not query.get("utm_content", [""])[0]:
        return "missing utm_content"
    return None


def audit(root: Path, timeout: int) -> tuple[list[Finding], dict[str, int]]:
    findings: list[Finding] = []
    counts = {"targets": 0, "checked_http": 0, "http_cache_hits": 0, "skipped_http": 0, "redirects": 0}
    http_cache: dict[str, tuple[bool, str]] = {}
    file_anchors = {path: anchors_for(path.read_text(encoding="utf-8", errors="replace")) for path in public_files(root)}

    for path, anchors in file_anchors.items():
        rel_file = str(path.relative_to(root))
        text = path.read_text(encoding="utf-8", errors="replace")
        for kind, target in extract_targets(text):
            counts["targets"] += 1
            base, fragment = urldefrag(target)
            if target.startswith("mailto:"):
                counts["skipped_http"] += 1
                continue
            if target.startswith("#"):
                if target[1:] not in anchors:
                    findings.append(Finding("P1", rel_file, target, "missing fragment anchor"))
                continue
            if base.startswith("http://") or base.startswith("https://"):
                if is_evolink_owned(base):
                    utm_issue = check_utm(base)
                    if utm_issue:
                        findings.append(Finding("P1", rel_file, target, utm_issue))
                if base in http_cache:
                    ok, detail = http_cache[base]
                    counts["http_cache_hits"] += 1
                else:
                    ok, detail = check_http(base, timeout)
                    http_cache[base] = (ok, detail)
                    counts["checked_http"] += 1
                if "redirected to" in detail:
                    counts["redirects"] += 1
                if not ok:
                    severity = "P0" if "dashboard/keys" in base or is_evolink_owned(base) else "P1"
                    findings.append(Finding(severity, rel_file, target, detail))
                continue

            resolved = (path.parent / base).resolve()
            try:
                resolved.relative_to(root.resolve())
            except ValueError:
                findings.append(Finding("P1", rel_file, target, "relative path escapes repository root"))
                continue
            if not resolved.exists():
                findings.append(Finding("P1", rel_file, target, "relative file does not exist"))
                continue
            if fragment and resolved.is_file() and resolved.suffix.lower() == ".md":
                target_anchors = anchors_for(resolved.read_text(encoding="utf-8", errors="replace"))
                if fragment not in target_anchors:
                    findings.append(Finding("P1", rel_file, target, "fragment anchor missing in target file"))
            if kind in {"image", "html-image"} and resolved.is_file() and resolved.stat().st_size == 0:
                findings.append(Finding("P1", rel_file, target, "image/media file is empty"))

    return findings, counts


def write_report(root: Path, out: Path, findings: list[Finding], counts: dict[str, int], command: str) -> None:
    p0 = sum(1 for finding in findings if finding.severity == "P0")
    p1 = sum(1 for finding in findings if finding.severity == "P1")
    p2 = sum(1 for finding in findings if finding.severity == "P2")
    lines = [
        "# Public Surface Link Audit",
        "",
        f"- Repository: `{root}`",
        "- Scope: root `README*.md`, `docs/**/*.md`",
        "- Excluded: `local-audits/` private evidence, `source-material/` provenance copies, generated/vendor/cache paths",
        f"- Command: `{command}`",
        f"- Total extracted links/assets: {counts['targets']}",
        f"- Checked unique HTTP(S): {counts['checked_http']}",
        f"- HTTP(S) cache hits: {counts['http_cache_hits']}",
        f"- Skipped HTTP(S): {counts['skipped_http']}",
        f"- Redirects: {counts['redirects']}",
        f"- P0 failures: {p0}",
        f"- P1 failures: {p1}",
        f"- P2 warnings: {p2}",
        f"- Result: {'PASS' if p0 == 0 and p1 == 0 else 'FAIL'}",
        "",
        "## Findings",
    ]
    if findings:
        for finding in findings:
            lines.append(f"- `{finding.severity}` `{finding.file}` `{finding.target}`: {finding.detail}")
    else:
        lines.append("- None")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=".")
    parser.add_argument("--out", required=True)
    parser.add_argument("--timeout", type=int, default=10)
    args = parser.parse_args()

    root = Path(args.repo).resolve()
    out = Path(args.out).resolve()
    findings, counts = audit(root, args.timeout)
    command = " ".join(sys.argv)
    write_report(root, out, findings, counts, command)
    p0 = sum(1 for finding in findings if finding.severity == "P0")
    p1 = sum(1 for finding in findings if finding.severity == "P1")
    print(out)
    return 0 if p0 == 0 and p1 == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
