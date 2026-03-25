#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ALLOWED_TOP_LEVEL_KEYS = {"meta_data", "format_dict", "header_description"}

META_REQUIRED = {"format_name", "format_source", "format_version"}
META_OPTIONAL = {
    "format_cite_name",
    "format_citation",
    "format_description",
    "format_separator",
    "format_na",
    "format_comment",
    "format_header",
    "format_col_order",
    "format_datatype",
    "format_fixed_header",
    "format_fixed",
    "format_format",
    "format_assumption",
    "format_notes",
    "last_check_date",
    "software_license",
}
META_ALLOWED = META_REQUIRED | META_OPTIONAL


@dataclass(frozen=True)
class Finding:
    level: str  # "ERROR" | "WARN"
    file: Path
    message: str


def _is_non_empty_str(x: Any) -> bool:
    return isinstance(x, str) and x.strip() != ""


def _as_str_list(x: Any) -> list[str] | None:
    if not isinstance(x, list):
        return None
    if not all(isinstance(v, str) for v in x):
        return None
    return x


def _is_str_list_or_null(x: Any) -> bool:
    return x is None or _as_str_list(x) is not None


def _load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def _load_reserved_headers_from_gwaslab(path: Path) -> set[str]:
    """
    Tries to support a few plausible formats:
    - list[str]
    - dict[str, ...] (keys are headers)
    """
    data = _load_json(path)
    if isinstance(data, list) and all(isinstance(x, str) for x in data):
        return set(data)
    if isinstance(data, dict) and all(isinstance(k, str) for k in data.keys()):
        return set(data.keys())
    raise ValueError(f"Unsupported reserved-header JSON shape in {path}")


def _candidate_reserved_header_paths(repo_root: Path) -> list[Path]:
    # docs/design.md references src/gwaslab/qc/qc_researved_header.json, but this repo
    # may be used alongside a sibling gwaslab checkout.
    rels = [
        Path("src/gwaslab/qc/qc_researved_header.json"),
        Path("gwaslab/qc/qc_researved_header.json"),
        Path("../gwaslab/src/gwaslab/qc/qc_researved_header.json"),
        Path("../gwaslab/gwaslab/qc/qc_researved_header.json"),
    ]
    out: list[Path] = []
    for rel in rels:
        p = (repo_root / rel).resolve()
        if p.exists() and p.is_file():
            out.append(p)
    return out


def validate_format_json(
    *,
    file_path: Path,
    payload: Any,
    reserved_headers: set[str] | None,
    strict: bool,
) -> list[Finding]:
    f: list[Finding] = []

    if not isinstance(payload, dict):
        return [Finding("ERROR", file_path, "Top-level JSON must be an object.")]

    extra_top = set(payload.keys()) - ALLOWED_TOP_LEVEL_KEYS
    if extra_top:
        msg = f"Unknown top-level keys: {sorted(extra_top)} (allowed: {sorted(ALLOWED_TOP_LEVEL_KEYS)})."
        f.append(Finding("WARN" if not strict else "ERROR", file_path, msg))

    if "meta_data" not in payload:
        f.append(Finding("ERROR", file_path, "Missing required top-level key: meta_data"))
        meta = None
    else:
        meta = payload.get("meta_data")
        if not isinstance(meta, dict):
            f.append(Finding("ERROR", file_path, "meta_data must be an object"))
            meta = None

    if "format_dict" not in payload:
        f.append(Finding("ERROR", file_path, "Missing required top-level key: format_dict"))
        fmt = None
    else:
        fmt = payload.get("format_dict")
        if not isinstance(fmt, dict):
            f.append(Finding("ERROR", file_path, "format_dict must be an object"))
            fmt = None

    header_desc = payload.get("header_description")
    if header_desc is not None and not isinstance(header_desc, dict):
        f.append(Finding("ERROR", file_path, "header_description must be an object when present"))
        header_desc = None

    if meta is not None:
        for k in sorted(META_REQUIRED):
            if k not in meta:
                f.append(Finding("ERROR", file_path, f"meta_data missing required field: {k}"))
            else:
                v = meta.get(k)
                if k in {"format_name", "format_source"}:
                    if not isinstance(v, str):
                        f.append(Finding("ERROR", file_path, f"meta_data.{k} must be a string"))
                    elif v.strip() == "":
                        f.append(Finding("WARN" if not strict else "ERROR", file_path, f"meta_data.{k} is empty"))
                elif k == "format_version":
                    if not isinstance(v, (str, int, float)):
                        f.append(Finding("ERROR", file_path, "meta_data.format_version must be string/number"))
                    elif isinstance(v, str) and v.strip() == "":
                        f.append(Finding("WARN" if not strict else "ERROR", file_path, "meta_data.format_version is empty"))

        unknown_meta = set(meta.keys()) - META_ALLOWED
        if unknown_meta:
            msg = f"Unknown meta_data fields: {sorted(unknown_meta)} (allowed: {sorted(META_ALLOWED)})."
            f.append(Finding("WARN" if not strict else "ERROR", file_path, msg))

        if "format_header" in meta and meta["format_header"] is not None and not isinstance(meta["format_header"], bool):
            f.append(Finding("ERROR", file_path, "meta_data.format_header must be boolean or null when present"))

        if "format_col_order" in meta:
            if not _is_str_list_or_null(meta["format_col_order"]):
                f.append(Finding("ERROR", file_path, "meta_data.format_col_order must be an array of strings or null"))

        if "format_notes" in meta:
            if not _is_str_list_or_null(meta["format_notes"]):
                f.append(Finding("ERROR", file_path, "meta_data.format_notes must be an array of strings or null"))

        if "format_fixed_header" in meta:
            fixed_header = meta["format_fixed_header"]
            if fixed_header is not None and not isinstance(fixed_header, (str, list)):
                f.append(
                    Finding(
                        "ERROR",
                        file_path,
                        "meta_data.format_fixed_header must be a string, array of strings, or null",
                    )
                )
            elif isinstance(fixed_header, list) and _as_str_list(fixed_header) is None:
                f.append(
                    Finding(
                        "ERROR",
                        file_path,
                        "meta_data.format_fixed_header array must contain only strings",
                    )
                )

        if "format_fixed" in meta:
            if not _is_str_list_or_null(meta["format_fixed"]):
                f.append(Finding("ERROR", file_path, "meta_data.format_fixed must be an array of strings or null"))

        if "format_separator" in meta and meta["format_separator"] is not None and not isinstance(meta["format_separator"], str):
            f.append(Finding("ERROR", file_path, "meta_data.format_separator must be a string or null when present"))

        if "format_comment" in meta and meta["format_comment"] is not None and not isinstance(meta["format_comment"], str):
            f.append(Finding("ERROR", file_path, "meta_data.format_comment must be string or null when present"))

        if "format_na" in meta:
            na = meta["format_na"]
            if not (
                na is None
                or isinstance(na, str)
                or (isinstance(na, list) and all(isinstance(x, (str, type(None))) for x in na))
            ):
                f.append(
                    Finding(
                        "ERROR",
                        file_path,
                        "meta_data.format_na must be string, null, or array of strings/nulls when present",
                    )
                )

        if "format_datatype" in meta and meta["format_datatype"] is not None and not isinstance(meta["format_datatype"], dict):
            f.append(Finding("ERROR", file_path, "meta_data.format_datatype must be an object or null when present"))

    if fmt is not None:
        if len(fmt) == 0:
            f.append(Finding("ERROR", file_path, "format_dict must not be empty"))

        for k, v in fmt.items():
            if not _is_non_empty_str(k):
                f.append(Finding("ERROR", file_path, "format_dict contains an empty/invalid key"))
            if not _is_non_empty_str(v):
                f.append(Finding("ERROR", file_path, f"format_dict['{k}'] must map to a non-empty string"))

            if reserved_headers is not None and isinstance(v, str) and v not in reserved_headers:
                f.append(
                    Finding(
                        "ERROR" if strict else "WARN",
                        file_path,
                        f"format_dict['{k}'] maps to unknown canonical header '{v}' (reserved list size={len(reserved_headers)})",
                    )
                )

    # Cross-check col order against format_dict keys (warning by default, since some formats
    # may include columns that are intentionally unmapped).
    if meta is not None and fmt is not None and "format_col_order" in meta and isinstance(meta.get("format_col_order"), list):
        missing = [c for c in meta["format_col_order"] if isinstance(c, str) and c not in fmt]
        if missing:
            f.append(
                Finding(
                    "WARN" if not strict else "ERROR",
                    file_path,
                    f"meta_data.format_col_order contains columns not present in format_dict keys: {missing}",
                )
            )

    # header_description consistency: docs say keys are canonical headers, but some examples
    # use source columns. Accept either; warn if it matches neither.
    if header_desc is not None and isinstance(header_desc, dict) and fmt is not None:
        hdr_keys = {k for k in header_desc.keys() if isinstance(k, str)}
        fmt_keys = set(fmt.keys())
        fmt_vals = {v for v in fmt.values() if isinstance(v, str)}
        if hdr_keys and not (hdr_keys.issubset(fmt_keys) or hdr_keys.issubset(fmt_vals)):
            f.append(
                Finding(
                    "WARN" if not strict else "ERROR",
                    file_path,
                    "header_description keys do not appear to be a subset of format_dict keys or mapped canonical headers.",
                )
            )

    return f


def _iter_format_files(repo_root: Path, formats_dir: Path, explicit: list[Path] | None) -> list[Path]:
    if explicit:
        return [p.resolve() for p in explicit]
    if not formats_dir.exists():
        return []
    return sorted(p.resolve() for p in formats_dir.glob("*.json") if p.is_file())


def _group_findings_by_file(findings: list[Finding], repo_root: Path) -> dict[str, list[str]]:
    grouped: dict[str, list[str]] = {}
    for item in findings:
        rel = os.path.relpath(item.file, start=repo_root)
        grouped.setdefault(rel, []).append(item.message)
    return dict(sorted(grouped.items(), key=lambda kv: kv[0]))


def _print_section(title: str) -> None:
    print(f"\n[{title}]", file=sys.stderr)


def _print_findings_grouped(title: str, findings: list[Finding], repo_root: Path) -> None:
    _print_section(title)
    if not findings:
        print("  (none)", file=sys.stderr)
        return
    grouped = _group_findings_by_file(findings, repo_root)
    for rel, messages in grouped.items():
        print(f"  - {rel}", file=sys.stderr)
        for msg in messages:
            print(f"    - {msg}", file=sys.stderr)


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Check integrity of formats/*.json against docs/design.md structure.")
    parser.add_argument("--repo-root", default=".", help="Repository root (default: .)")
    parser.add_argument("--formats-dir", default="formats", help="Formats directory relative to repo root (default: formats)")
    parser.add_argument(
        "--reserved-headers",
        default=None,
        help="Path to gwaslab reserved-header JSON (optional). If omitted, common sibling locations are tried.",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Treat warnings as errors and enforce reserved header checks as errors.",
    )
    parser.add_argument(
        "--exclude-glob",
        action="append",
        default=["auto*.json", "template.json"],
        help="Glob(s) (matched against file basename) to exclude. Can be provided multiple times.",
    )
    parser.add_argument(
        "files",
        nargs="*",
        help="Optional explicit JSON files to check (default: all formats/*.json).",
    )
    args = parser.parse_args(argv)

    repo_root = Path(args.repo_root).resolve()
    formats_dir = (repo_root / args.formats_dir).resolve()
    explicit_files = [Path(p) for p in args.files] if args.files else None
    format_files = _iter_format_files(repo_root, formats_dir, explicit_files)
    if explicit_files is None and args.exclude_glob:
        excluded: set[Path] = set()
        for pat in args.exclude_glob:
            for fp in format_files:
                if fp.name and fp.match(pat):
                    excluded.add(fp)
        format_files = [fp for fp in format_files if fp not in excluded]

    if not format_files:
        print("No format JSON files found.", file=sys.stderr)
        return 2

    reserved_headers: set[str] | None = None
    reserved_path: Path | None = None

    if args.reserved_headers:
        reserved_path = Path(args.reserved_headers).expanduser().resolve()
        if not reserved_path.exists():
            print(f"Reserved header file not found: {reserved_path}", file=sys.stderr)
            return 2
        reserved_headers = _load_reserved_headers_from_gwaslab(reserved_path)
    else:
        candidates = _candidate_reserved_header_paths(repo_root)
        if candidates:
            reserved_path = candidates[0]
            try:
                reserved_headers = _load_reserved_headers_from_gwaslab(reserved_path)
            except Exception as e:
                print(f"Failed to read reserved header file at {reserved_path}: {e}", file=sys.stderr)
                reserved_headers = None

    _print_section("Configuration")
    print(f"  Repo root: {repo_root}", file=sys.stderr)
    print(f"  Formats dir: {formats_dir}", file=sys.stderr)
    print(f"  Files to check: {len(format_files)}", file=sys.stderr)
    if args.exclude_glob and explicit_files is None:
        print(f"  Exclude globs: {args.exclude_glob}", file=sys.stderr)
    print(f"  Strict mode: {args.strict}", file=sys.stderr)
    if reserved_headers is None:
        print("  Canonical headers: not found (validation skipped)", file=sys.stderr)
        print("    Hint: use --reserved-headers or keep a sibling gwaslab checkout.", file=sys.stderr)
    else:
        print(f"  Canonical headers: loaded ({len(reserved_headers)})", file=sys.stderr)
        print(f"    Source: {reserved_path}", file=sys.stderr)

    findings: list[Finding] = []
    for fp in format_files:
        try:
            payload = _load_json(fp)
        except json.JSONDecodeError as e:
            findings.append(Finding("ERROR", fp, f"Invalid JSON: {e}"))
            continue
        except Exception as e:
            findings.append(Finding("ERROR", fp, f"Failed to read: {e}"))
            continue

        findings.extend(
            validate_format_json(
                file_path=fp,
                payload=payload,
                reserved_headers=reserved_headers,
                strict=args.strict,
            )
        )

    errors = [x for x in findings if x.level == "ERROR"]
    warns = [x for x in findings if x.level == "WARN"]

    _print_findings_grouped("Errors", errors, repo_root)
    _print_findings_grouped("Warnings", warns, repo_root)

    _print_section("Summary")
    print(f"  Checked files: {len(format_files)}", file=sys.stderr)
    print(f"  Errors: {len(errors)}", file=sys.stderr)
    print(f"  Warnings: {len(warns)}", file=sys.stderr)
    return 1 if errors or (args.strict and warns) else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

