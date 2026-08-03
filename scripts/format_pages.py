#!/usr/bin/env python3
"""Generate MkDocs pages for each format spec and update mkdocs.yml nav."""
from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from format_summary import display_meta_value, evaluate_tier, summarize_format
from formatbook_lib import canonicals_for_format, load_format_specs, load_json

SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_KEYS = SCRIPT_DIR.parent / "keys" / "key_canonical_headers.json"
DEFAULT_META_COLUMNS = SCRIPT_DIR.parent / "keys" / "meta_summary_columns.json"
DEFAULT_PAGE_TEMPLATE = SCRIPT_DIR / "templates" / "format_page.md.j2"
DEFAULT_INDEX_TEMPLATE = SCRIPT_DIR / "templates" / "format_index.md.j2"
DEFAULT_OUTPUT_DIR = "docs/formats"
DEFAULT_MKDOCS = "mkdocs.yml"

NAV_BEGIN = "    # BEGIN GENERATED FORMAT NAV — do not edit by hand"
NAV_END = "    # END GENERATED FORMAT NAV"
NAV_PATTERN = re.compile(
    re.escape(NAV_BEGIN) + r".*?" + re.escape(NAV_END),
    re.DOTALL,
)

_FILE_LAYOUT_FIELDS: list[tuple[str, str]] = [
    ("format_separator", "Separator"),
    ("format_na", "NA value"),
    ("format_comment", "Comment prefix"),
    ("format_header", "Header row"),
    ("format_header_lines", "Header lines"),
    ("format_header_line2_description", "Second header line"),
    ("format_col_order", "Column order"),
]

_LONG_META_FIELDS: list[tuple[str, str]] = [
    ("format_fixed_header", "Fixed header block"),
    ("format_contig_19", "GRCh37 contig headers"),
    ("format_contig_38", "GRCh38 contig headers"),
]

_MAX_LONG_BLOCK_CHARS = 2000


def md_cell(value: Any) -> str:
    if value is None or value == "":
        return "—"
    text = str(value).replace("|", "\\|").replace("\n", " ")
    return text


def format_dict_primary_value(v: Any) -> str | None:
    if v is None:
        return None
    if isinstance(v, str) and v.strip():
        return v
    return None


def build_mapping_rows(spec: dict[str, Any]) -> list[dict[str, Any]]:
    fmt = spec.get("format_dict") or {}
    fd2 = spec.get("format_dict_2") or {}
    if not isinstance(fmt, dict):
        return []
    if not isinstance(fd2, dict):
        fd2 = {}
    rows: list[dict[str, Any]] = []
    for raw in sorted(fmt.keys(), key=lambda x: str(x).lower()):
        primary = format_dict_primary_value(fmt.get(raw))
        secondary = format_dict_primary_value(fd2.get(raw)) if raw in fd2 else None
        rows.append(
            {
                "raw": raw,
                "canonical": primary,
                "canonical_2": secondary,
            }
        )
    return rows


def build_header_description_rows(spec: dict[str, Any]) -> list[dict[str, str]]:
    hd = spec.get("header_description")
    if not isinstance(hd, dict):
        return []
    return [
        {"column": str(col), "description": str(desc)}
        for col, desc in sorted(hd.items(), key=lambda x: str(x[0]).lower())
    ]


def build_file_layout(meta: dict[str, Any]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for field, label in _FILE_LAYOUT_FIELDS:
        value = meta.get(field)
        if value is None or value == "" or value == []:
            continue
        if field == "format_col_order" and isinstance(value, list):
            display = ", ".join(f"`{col}`" for col in value)
        else:
            display = display_meta_value(field, value)
        rows.append({"label": label, "value": display})
    return rows


def build_long_blocks(meta: dict[str, Any]) -> list[dict[str, str]]:
    blocks: list[dict[str, str]] = []
    for field, title in _LONG_META_FIELDS:
        value = meta.get(field)
        if not value or not isinstance(value, str):
            continue
        text = value
        if len(text) > _MAX_LONG_BLOCK_CHARS:
            text = text[:_MAX_LONG_BLOCK_CHARS] + "\n… (truncated)"
        blocks.append({"title": title, "text": text})
    return blocks


def build_page_context(
    key: str,
    path: Path,
    spec: dict[str, Any],
    groups: list[dict[str, Any]],
    meta_columns: list[dict[str, Any]],
) -> dict[str, Any]:
    summary = summarize_format(key, path, spec, groups, meta_columns)
    meta = spec.get("meta_data") if isinstance(spec.get("meta_data"), dict) else {}
    mapping_rows = build_mapping_rows(spec)
    return {
        **summary,
        "format_source_2": meta.get("format_source_2"),
        "format_assumption": meta.get("format_assumption"),
        "format_notes": meta.get("format_notes") if isinstance(meta.get("format_notes"), list) else None,
        "fixed_headers": meta.get("format_fixed") if isinstance(meta.get("format_fixed"), list) else None,
        "format_format": meta.get("format_format") if isinstance(meta.get("format_format"), list) else None,
        "file_layout": build_file_layout(meta),
        "mapping_rows": mapping_rows,
        "header_description_rows": build_header_description_rows(spec),
        "long_blocks": build_long_blocks(meta),
    }


def jinja_env(template_dir: Path):
    try:
        from jinja2 import Environment, FileSystemLoader, select_autoescape
    except ImportError as e:
        raise SystemExit("jinja2 is required: pip install jinja2") from e
    env = Environment(
        loader=FileSystemLoader(template_dir),
        autoescape=False,
    )
    env.filters["md_cell"] = md_cell
    return env


def render_pages(
    pages: list[dict[str, Any]],
    *,
    page_template_path: Path,
    index_template_path: Path,
    output_dir: Path,
) -> None:
    env = jinja_env(page_template_path.parent)
    page_tpl = env.get_template(page_template_path.name)
    index_tpl = env.get_template(index_template_path.name)

    output_dir.mkdir(parents=True, exist_ok=True)
    current_keys = {p["key"] for p in pages}

    for stale in output_dir.glob("*.md"):
        if stale.name == "index.md":
            continue
        if stale.stem not in current_keys:
            stale.unlink()

    for page in pages:
        out_path = output_dir / f"{page['key']}.md"
        out_path.write_text(page_tpl.render(page=page), encoding="utf-8")

    index_path = output_dir / "index.md"
    index_items = sorted(
        [{"key": p["key"], "format_name": p["format_name"]} for p in pages],
        key=lambda x: x["format_name"].lower(),
    )
    index_path.write_text(index_tpl.render(formats=index_items), encoding="utf-8")


def update_mkdocs_nav(mkdocs_path: Path, format_keys: list[str]) -> None:
    if not mkdocs_path.exists():
        print(f"mkdocs.yml not found: {mkdocs_path}", file=sys.stderr)
        return

    nav_lines = [f"    - {key}: formats/{key}.md" for key in sorted(format_keys, key=str.lower)]
    new_block = NAV_BEGIN + "\n" + "\n".join(nav_lines) + "\n" + NAV_END

    text = mkdocs_path.read_text(encoding="utf-8")
    if not NAV_PATTERN.search(text):
        print(
            f"Nav markers not found in {mkdocs_path}; add {NAV_BEGIN} / {NAV_END} under Formats.",
            file=sys.stderr,
        )
        return

    mkdocs_path.write_text(NAV_PATTERN.sub(new_block, text, count=1), encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate MkDocs pages for format specs.")
    parser.add_argument("--repo-root", default=".", help="Repository root")
    parser.add_argument("--formats-dir", default="formats", help="Formats directory")
    parser.add_argument("--keys", default=str(DEFAULT_KEYS), help="Tier groups JSON")
    parser.add_argument("--meta-columns", default=str(DEFAULT_META_COLUMNS), help="Meta table columns JSON")
    parser.add_argument("--page-template", default=str(DEFAULT_PAGE_TEMPLATE), help="Per-format Jinja2 template")
    parser.add_argument("--index-template", default=str(DEFAULT_INDEX_TEMPLATE), help="Index Jinja2 template")
    parser.add_argument("--output-dir", default=DEFAULT_OUTPUT_DIR, help="Output directory for format pages")
    parser.add_argument("--mkdocs", default=DEFAULT_MKDOCS, help="Path to mkdocs.yml")
    parser.add_argument(
        "--exclude-glob",
        action="append",
        default=["template.json"],
        help="Glob(s) matched against basename to exclude",
    )
    args = parser.parse_args(argv)

    repo_root = Path(args.repo_root).resolve()
    formats_dir = (repo_root / args.formats_dir).resolve()
    keys_path = Path(args.keys).resolve()
    meta_columns_path = Path(args.meta_columns).resolve()
    page_template_path = Path(args.page_template).resolve()
    index_template_path = Path(args.index_template).resolve()
    output_dir = (repo_root / args.output_dir).resolve()
    mkdocs_path = (repo_root / args.mkdocs).resolve()

    for path, label in [
        (keys_path, "Keys file"),
        (meta_columns_path, "Meta columns file"),
        (page_template_path, "Page template"),
        (index_template_path, "Index template"),
    ]:
        if not path.exists():
            print(f"{label} not found: {path}", file=sys.stderr)
            return 2

    keys_data = load_json(keys_path)
    meta_data = load_json(meta_columns_path)
    groups: list[dict[str, Any]] = keys_data["groups"]
    meta_columns: list[dict[str, Any]] = meta_data["columns"]

    specs = load_format_specs(formats_dir, exclude_globs=args.exclude_glob)
    pages = [
        build_page_context(key, path, spec, groups, meta_columns)
        for key, path, spec in specs
    ]

    render_pages(
        pages,
        page_template_path=page_template_path,
        index_template_path=index_template_path,
        output_dir=output_dir,
    )
    update_mkdocs_nav(mkdocs_path, [p["key"] for p in pages])

    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    print(f"Wrote {len(pages)} format pages to {output_dir} ({generated_at})")
    print(f"Updated nav in {mkdocs_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
