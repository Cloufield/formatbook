#!/usr/bin/env python3
"""Generate format summary JSON and interactive HTML coverage report."""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from formatbook_lib import canonicals_for_format, load_format_specs, load_json

SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_KEYS = SCRIPT_DIR.parent / "keys" / "key_canonical_headers.json"
DEFAULT_META_COLUMNS = SCRIPT_DIR.parent / "keys" / "meta_summary_columns.json"
DEFAULT_TEMPLATE = SCRIPT_DIR / "templates" / "format_summary.html.j2"

_SEPARATOR_LABELS = {"\t": "TAB", " ": "SPACE", ",": ",", "|": "|", ";": ";"}


def evaluate_tier(canon: set[str], group: dict[str, Any]) -> dict[str, Any]:
    headers: list[str] = group["headers"]
    mode: str = group["mode"]
    matched = [h for h in headers if h in canon]
    missing = [h for h in headers if h not in canon]
    if mode == "any":
        satisfied = len(matched) > 0
        partial = False
    elif mode == "all":
        satisfied = len(missing) == 0
        partial = not satisfied and len(matched) > 0
    else:
        raise ValueError(f"Unknown tier mode: {mode!r}")
    return {
        "id": group["id"],
        "label": group["label"],
        "mode": mode,
        "satisfied": satisfied,
        "partial": partial,
        "matched_headers": matched,
        "missing_headers": missing,
    }


def display_meta_value(field: str, value: Any) -> str:
    if value is None or value == "" or value == []:
        return "—"
    if field == "format_separator":
        if isinstance(value, str):
            return _SEPARATOR_LABELS.get(value, repr(value))
        return str(value)
    if field == "format_header":
        if value is True:
            return "yes"
        if value is False:
            return "no"
        return str(value)
    if field == "format_na" and isinstance(value, list):
        return ", ".join(str(x) for x in value)
    return str(value)


def build_meta_display(meta: dict[str, Any], meta_columns: list[dict[str, Any]]) -> dict[str, str]:
    if not isinstance(meta, dict):
        meta = {}
    return {
        col["id"]: display_meta_value(col["field"], meta.get(col["field"]))
        for col in meta_columns
        if col.get("widget") != "copy_citation"
    }


def summarize_format(
    key: str,
    path: Path,
    spec: dict[str, Any],
    groups: list[dict[str, Any]],
    meta_columns: list[dict[str, Any]],
) -> dict[str, Any]:
    meta = spec.get("meta_data") or {}
    fmt = spec.get("format_dict") or {}
    if not isinstance(fmt, dict):
        fmt = {}
    canon = canonicals_for_format(spec)
    mapped = sum(1 for v in fmt.values() if v is not None and str(v).strip())
    unmapped = sum(1 for v in fmt.values() if v is None)
    tiers = [evaluate_tier(canon, g) for g in groups]
    tiers_satisfied = sum(1 for t in tiers if t["satisfied"])
    return {
        "key": key,
        "file": path.name,
        "format_name": meta.get("format_name") or key,
        "format_source": meta.get("format_source"),
        "format_version": meta.get("format_version"),
        "format_description": meta.get("format_description"),
        "format_cite_name": meta.get("format_cite_name"),
        "format_citation": meta.get("format_citation"),
        "github_url": meta.get("github_url"),
        "last_check_date": meta.get("last_check_date"),
        "raw_column_count": len(fmt),
        "mapped_count": mapped,
        "unmapped_count": unmapped,
        "canonical_count": len(canon),
        "canonicals": sorted(canon),
        "has_format_dict_2": bool(spec.get("format_dict_2")),
        "has_header_description": bool(spec.get("header_description")),
        "has_companion_meta": bool(spec.get("companion_meta")),
        "tiers": tiers,
        "tiers_satisfied": tiers_satisfied,
        "tiers_total": len(groups),
        "meta_display": build_meta_display(meta if isinstance(meta, dict) else {}, meta_columns),
    }


def build_report(
    *,
    repo_root: Path,
    formats_dir: Path,
    keys_path: Path,
    meta_columns_path: Path,
    exclude_globs: list[str],
) -> dict[str, Any]:
    keys_data = load_json(keys_path)
    meta_data = load_json(meta_columns_path)
    groups: list[dict[str, Any]] = keys_data["groups"]
    meta_columns: list[dict[str, Any]] = meta_data["columns"]
    formats = [
        summarize_format(key, path, spec, groups, meta_columns)
        for key, path, spec in load_format_specs(formats_dir, exclude_globs=exclude_globs)
    ]
    avg_tiers = sum(f["tiers_satisfied"] for f in formats) / len(formats) if formats else 0.0
    return {
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        "format_count": len(formats),
        "tier_groups": groups,
        "meta_columns": meta_columns,
        "avg_tiers_satisfied": round(avg_tiers, 2),
        "formats": formats,
        "repo_root": str(repo_root),
    }


def render_html(report: dict[str, Any], template_path: Path) -> str:
    try:
        from jinja2 import Environment, FileSystemLoader, select_autoescape
    except ImportError as e:
        raise SystemExit("jinja2 is required: pip install jinja2") from e
    env = Environment(
        loader=FileSystemLoader(template_path.parent),
        autoescape=select_autoescape(["html", "xml"]),
    )
    template = env.get_template(template_path.name)
    return template.render(report=report)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate format summary HTML and JSON.")
    parser.add_argument("--repo-root", default=".", help="Repository root")
    parser.add_argument("--formats-dir", default="formats", help="Formats directory")
    parser.add_argument("--keys", default=str(DEFAULT_KEYS), help="Tier groups JSON")
    parser.add_argument("--meta-columns", default=str(DEFAULT_META_COLUMNS), help="Meta table columns JSON")
    parser.add_argument("--template", default=str(DEFAULT_TEMPLATE), help="Jinja2 HTML template")
    parser.add_argument("--output-html", default="docs/format_summary.html", help="Output HTML path")
    parser.add_argument("--output-json", default="docs/assets/format_summary.json", help="Output JSON path")
    parser.add_argument(
        "--exclude-glob",
        action="append",
        default=["auto*.json", "template.json"],
        help="Glob(s) matched against basename to exclude",
    )
    args = parser.parse_args(argv)

    repo_root = Path(args.repo_root).resolve()
    formats_dir = (repo_root / args.formats_dir).resolve()
    keys_path = Path(args.keys).resolve()
    meta_columns_path = Path(args.meta_columns).resolve()
    template_path = Path(args.template).resolve()
    output_html = (repo_root / args.output_html).resolve()
    output_json = (repo_root / args.output_json).resolve()

    if not keys_path.exists():
        print(f"Keys file not found: {keys_path}", file=sys.stderr)
        return 2
    if not meta_columns_path.exists():
        print(f"Meta columns file not found: {meta_columns_path}", file=sys.stderr)
        return 2
    if not template_path.exists():
        print(f"Template not found: {template_path}", file=sys.stderr)
        return 2

    report = build_report(
        repo_root=repo_root,
        formats_dir=formats_dir,
        keys_path=keys_path,
        meta_columns_path=meta_columns_path,
        exclude_globs=args.exclude_glob,
    )

    output_json.parent.mkdir(parents=True, exist_ok=True)
    output_html.parent.mkdir(parents=True, exist_ok=True)

    with output_json.open("w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
        f.write("\n")

    html = render_html(report, template_path)
    with output_html.open("w", encoding="utf-8") as f:
        f.write(html)

    print(f"Wrote {output_json} ({report['format_count']} formats)")
    print(f"Wrote {output_html}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
