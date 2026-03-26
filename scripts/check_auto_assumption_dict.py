#!/usr/bin/env python3
"""
Verify formats/auto*.json (except auto_raw) internal consistency:
REF/ALT, numbered alleles A0–A2, and indexed/generic frequency columns must match
the preset implied by format_name.
"""

from __future__ import annotations

import json
import os
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FORMATS = os.path.join(REPO_ROOT, "formats")

# (effect_index 0|1|2, ref_is_ea, generic_frq_is_neaf)
_PRESET_SEMANTICS: dict[str, tuple[int, bool, bool]] = {
    "auto": (1, False, False),
    "auto_0": (0, False, False),
    "auto_2": (2, False, False),
    "auto_neaf": (1, False, True),
    "auto_0_neaf": (0, False, True),
    "auto_2_neaf": (2, False, True),
    "auto_ref": (1, True, False),
    "auto_0_ref": (0, True, False),
    "auto_1_ref": (1, True, False),
    "auto_2_ref": (2, True, False),
    "auto_ref_neaf": (1, True, True),
    "auto_0_ref_neaf": (0, True, True),
    "auto_1_ref_neaf": (1, True, True),
    "auto_2_ref_neaf": (2, True, True),
}


def _allele_roles(effect_index: int) -> tuple[str, str, str]:
    roles = ["NEA", "NEA", "NEA"]
    roles[effect_index] = "EA"
    return roles[0], roles[1], roles[2]


def _check_format_dict(format_name: str, fd: dict) -> list[str]:
    if format_name not in _PRESET_SEMANTICS:
        return [f"unknown format_name {format_name!r} (add to _PRESET_SEMANTICS)"]
    idx, ref_is_ea, generic_neaf = _PRESET_SEMANTICS[format_name]
    errs: list[str] = []
    a0, a1, a2 = _allele_roles(idx)

    if "REF" in fd and "ALT" in fd:
        if ref_is_ea:
            if fd["REF"] != "EA" or fd["ALT"] != "NEA":
                errs.append(f"REF/ALT: expected REF=EA, ALT=NEA; got REF={fd['REF']}, ALT={fd['ALT']}")
        else:
            if fd["REF"] != "NEA" or fd["ALT"] != "EA":
                errs.append(f"REF/ALT: expected REF=NEA, ALT=EA; got REF={fd['REF']}, ALT={fd['ALT']}")

    for i, exp in enumerate((a0, a1, a2)):
        k = f"A{i}"
        if k in fd and fd[k] != exp:
            errs.append(f"{k}: expected {exp} for effect index {idx}; got {fd[k]}")

    exp_g = "NEAF" if generic_neaf else "EAF"
    for key in ("Frq", "FREQ", "Freq", "FRQ", "frq", "Frequency"):
        if key in fd and fd[key] != exp_g:
            errs.append(f"{key}: expected {exp_g} for this preset; got {fd[key]}")

    for i in (0, 1, 2):
        ak = f"A{i}"
        if ak not in fd:
            continue
        role = fd[ak]
        exp_f = "EAF" if role == "EA" else "NEAF"
        for key in (f"A{i}FREQ", f"Freq{i}"):
            if key in fd and fd[key] != exp_f:
                errs.append(f"{key}: expected {exp_f} because {ak}={role}; got {fd[key]}")

    return errs


def main(argv: list[str]) -> int:
    os.chdir(REPO_ROOT)
    bad = 0
    for name in sorted(os.listdir(FORMATS)):
        if not name.startswith("auto") or not name.endswith(".json"):
            continue
        if name == "auto_raw.json":
            continue
        path = os.path.join(FORMATS, name)
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        fn = data["meta_data"]["format_name"]
        errs = _check_format_dict(fn, data["format_dict"])
        if errs:
            bad += 1
            print(f"{name} ({fn}):", file=sys.stderr)
            for e in errs:
                print(f"  {e}", file=sys.stderr)
    if bad:
        print(f"check_auto_assumption_dict: {bad} file(s) failed", file=sys.stderr)
        return 1
    print("check_auto_assumption_dict: OK (all auto presets consistent)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
