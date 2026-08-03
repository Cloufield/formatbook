#!/usr/bin/env python3
"""Shared helpers for loading formatbook JSON specs and extracting canonical headers."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def format_dict_primary_value(v: Any) -> str | None:
    """format_dict / format_dict_2 value: mapped canonical string, or None when unmapped."""
    if v is None:
        return None
    if isinstance(v, str) and v.strip():
        return v
    return None


def all_canonicals_for_raw(raw: str, fmt: dict[str, Any], fd2: dict[str, Any] | None) -> list[str]:
    """Ordered: primary from format_dict, then optional second canonical from format_dict_2."""
    out: list[str] = []
    p = format_dict_primary_value(fmt.get(raw))
    if p:
        out.append(p)
    if fd2 is not None and raw in fd2:
        s = format_dict_primary_value(fd2.get(raw))
        if s and s not in out:
            out.append(s)
    return out


def canonicals_for_format(spec: dict[str, Any]) -> set[str]:
    """All distinct canonical headers mapped by a format spec."""
    fmt = spec.get("format_dict") or {}
    fd2 = spec.get("format_dict_2") or {}
    out: set[str] = set()
    if not isinstance(fmt, dict):
        return out
    for raw in fmt:
        for canon in all_canonicals_for_raw(raw, fmt, fd2 if isinstance(fd2, dict) else None):
            out.add(canon)
    return out


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def iter_format_files(
    formats_dir: Path,
    *,
    exclude_globs: list[str] | None = None,
    explicit: list[Path] | None = None,
) -> list[Path]:
    if explicit:
        return [p.resolve() for p in explicit]
    if not formats_dir.exists():
        return []
    files = sorted(p.resolve() for p in formats_dir.glob("*.json") if p.is_file())
    if not exclude_globs:
        return files
    excluded: set[Path] = set()
    for pat in exclude_globs:
        for fp in files:
            if fp.match(pat):
                excluded.add(fp)
    return [fp for fp in files if fp not in excluded]


def load_format_specs(
    formats_dir: Path,
    *,
    exclude_globs: list[str] | None = None,
) -> list[tuple[str, Path, dict[str, Any]]]:
    """Return (format_key, path, spec) sorted by format_key."""
    out: list[tuple[str, Path, dict[str, Any]]] = []
    for fp in iter_format_files(formats_dir, exclude_globs=exclude_globs):
        spec = load_json(fp)
        if not isinstance(spec, dict):
            continue
        key = fp.stem
        out.append((key, fp, spec))
    return sorted(out, key=lambda x: x[0].lower())
