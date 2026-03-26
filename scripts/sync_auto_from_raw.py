#!/usr/bin/env python3
"""
Merge formats/auto_raw.json into each formats/auto*.json preset (except auto_raw).

Keys listed in keys/auto_assumption_keys.json keep their per-file canonical mapping;
all other format_dict entries come from auto_raw so auto presets stay aligned on shared aliases.
After editing assumption-key mappings, run scripts/check_auto_assumption_dict.py.
"""

from __future__ import annotations

import json
import os
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FORMATS = os.path.join(REPO_ROOT, "formats")
KEYS_DIR = os.path.join(REPO_ROOT, "keys")
ASSUMPTION_KEYS_PATH = os.path.join(KEYS_DIR, "auto_assumption_keys.json")
RAW_NAME = "auto_raw.json"

_assumption_keys_cache: frozenset[str] | None = None


def load_assumption_keys() -> frozenset[str]:
    global _assumption_keys_cache
    if _assumption_keys_cache is not None:
        return _assumption_keys_cache
    if not os.path.isfile(ASSUMPTION_KEYS_PATH):
        raise FileNotFoundError(
            f"Missing {ASSUMPTION_KEYS_PATH}; create it with a JSON object containing a 'keys' array."
        )
    with open(ASSUMPTION_KEYS_PATH, encoding="utf-8") as f:
        data = json.load(f)
    if isinstance(data, list):
        keys = data
    elif isinstance(data, dict) and "keys" in data:
        keys = data["keys"]
    else:
        raise ValueError(
            f"{ASSUMPTION_KEYS_PATH} must be a JSON array of strings or an object with a 'keys' array."
        )
    if not isinstance(keys, list) or not all(isinstance(x, str) for x in keys):
        raise ValueError(f"{ASSUMPTION_KEYS_PATH}: 'keys' must be a list of strings.")
    if len(keys) != len(frozenset(keys)):
        raise ValueError(f"{ASSUMPTION_KEYS_PATH}: duplicate entries in 'keys'.")
    _assumption_keys_cache = frozenset(keys)
    return _assumption_keys_cache


def _merge_format_dict(raw: dict, target: dict, assumption_keys: frozenset[str]) -> dict:
    merged = dict(raw)
    for k in sorted(assumption_keys):
        if k in target:
            merged[k] = target[k]
    for k, v in target.items():
        if k not in merged:
            merged[k] = v
    return merged


def _load_json(path: str) -> dict:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def _write_format(path: str, data: dict) -> None:
    with open(path, "w", encoding="utf-8") as f:
        f.write(json.dumps(data, indent=4, ensure_ascii=False))
        f.write("\n")


def write_auto_raw_from_auto_json() -> dict:
    """Build auto_raw.json from formats/auto.json (strip assumption keys)."""
    assumption_keys = load_assumption_keys()
    auto_path = os.path.join(FORMATS, "auto.json")
    auto = _load_json(auto_path)
    raw_dict = {k: v for k, v in auto["format_dict"].items() if k not in assumption_keys}
    out = {
        "meta_data": {
            "format_name": "auto_raw",
            "format_separator": "\t",
            "format_na": "#NA",
            "format_comment": None,
            "format_description": "Shared raw→canonical aliases for all auto* presets (no allele or ambiguous-frequency assumptions). Merged by scripts/sync_auto_from_raw.py; not sufficient alone for summary-stat allele harmonization.",
            "format_version": 20250827,
        },
        "format_dict": raw_dict,
    }
    _write_format(os.path.join(FORMATS, RAW_NAME), out)
    return raw_dict


def sync_all(raw_dict: dict | None = None) -> None:
    assumption_keys = load_assumption_keys()
    if raw_dict is None:
        raw_dict = _load_json(os.path.join(FORMATS, RAW_NAME))["format_dict"]
    for name in sorted(os.listdir(FORMATS)):
        if not name.startswith("auto") or not name.endswith(".json"):
            continue
        if name == RAW_NAME:
            continue
        path = os.path.join(FORMATS, name)
        data = _load_json(path)
        meta = data["meta_data"]
        target_fd = data["format_dict"]
        merged_fd = _merge_format_dict(raw_dict, target_fd, assumption_keys)
        _write_format(path, {"meta_data": meta, "format_dict": merged_fd})
        print("synced", name)


def main(argv: list[str]) -> int:
    os.chdir(REPO_ROOT)
    raw_path = os.path.join(FORMATS, RAW_NAME)
    if "--write-raw-only" in argv:
        write_auto_raw_from_auto_json()
        print("wrote", RAW_NAME, "from auto.json")
        return 0
    if "--init-raw" in argv or not os.path.isfile(raw_path):
        write_auto_raw_from_auto_json()
        if "--init-raw" in argv:
            print("wrote", RAW_NAME, "from auto.json")
    sync_all()
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
