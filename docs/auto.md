# Auto-detection presets (`formats/auto*.json`)

## Defaults and omitted name parts

Three independent choices define a preset:

| Axis | Default | Meaning when default |
| --- | --- | --- |
| **Index** | **1** | Effect allele is **A1** / allele 1 (and indexed freqs follow that). |
| **REF/ALT** | **ALT = EA** | Effect on **alternate**; REF-like columns → NEA, ALT-like → EA. |
| **Generic `Frq`** | **EAF** | Headers like `Frq`, `FREQ`, `Frequency` → **EAF**. |

**Filename rule:** only include a segment when it **differs** from the default.

- All three default → **`auto.json`** (`format_name`: **`auto`**). Do **not** spell `auto_1_alt_eaf` (redundant).
- Only generic frequency is NEAF → **`auto_neaf.json`** (index 1 and ALT=EA omitted).
- Only index ≠ 1 → **`auto_0.json`**, **`auto_2.json`** (ALT + EAF omitted).
- Only REF/ALT convention differs (REF = EA) → **`auto_ref.json`** (1 + EAF omitted).
- REF = EA **and** index ≠ 1 → **`auto_0_ref.json`**, **`auto_1_ref.json`**, **`auto_2_ref.json`** (EAF omitted).
- Index ≠ 1 **and** generic NEAF → **`auto_0_neaf.json`**, **`auto_2_neaf.json`**.
- **REF** = EA **and** generic **NEAF** → **`auto_ref_neaf.json`**, **`auto_0_ref_neaf.json`**, **`auto_1_ref_neaf.json`**, **`auto_2_ref_neaf.json`**.

There is no **`auto_1_eaf.json`**: it would duplicate **`auto.json`**.

## Design: the three ambiguities

### (1) Number-indexed alleles (A0 / A1 / A2)

Which **numbered** allele column is EA? **`auto_0`**, **`auto`** (default **1**), **`auto_2`**. Indexed keys (`A0FREQ`, `AF1`, `Freq0`, …) follow that choice.

### (2) REF / ALT columns

**Default:** effect on **alternate** (REF → NEA, ALT → EA), consistent with **`auto`**.  
**Exception:** effect on **reference** → **`auto_ref`** or **`auto_*_ref`** when you also need a non-default index.

### (3) Generic frequency columns

**Default:** ambiguous `Frq`-style columns → **EAF**.  
**Exception:** → **NEAF** → add **`_neaf`** to the name (`auto_neaf`, `auto_0_neaf`, …).

### How it fits together

- **`auto_raw`**: mappings that do not depend on the three choices.
- Each **`auto_*`**: `auto_raw` + explicit non-default choices only (by filename).
- Pick **one** preset per file.

```text
Default (1, alt, eaf)     → auto
Only NEAF                 → auto_neaf
Only index 0 or 2         → auto_0 / auto_2
Only REF=EA               → auto_ref
REF=EA + index 0/1/2      → auto_0_ref / auto_1_ref / auto_2_ref
Index 0/2 + NEAF          → auto_0_neaf / auto_2_neaf
REF=EA + NEAF             → auto_ref_neaf / auto_*_ref_neaf
```

## Full 3×2×2 grid (index × REF-as-EA × generic Frq)

Rows: effect-index (**0** / **1** / **2**). Columns: **ALT=EA** (default ref/alt) vs **REF=EA**; cells **EAF** vs **NEAF** for generic `Frq`-style headers.

| Index | ALT = EA, generic EAF | ALT = EA, generic NEAF | REF = EA, generic EAF | REF = EA, generic NEAF |
| --- | --- | --- | --- | --- |
| **A0** = EA | `auto_0.json` | `auto_0_neaf.json` | `auto_0_ref.json` | `auto_0_ref_neaf.json` |
| **A1** = EA | `auto.json` | `auto_neaf.json` | `auto_1_ref.json` | `auto_1_ref_neaf.json` |
| **A2** = EA | `auto_2.json` | `auto_2_neaf.json` | `auto_2_ref.json` | `auto_2_ref_neaf.json` |

**Extra layout for (A1, REF=EA, EAF):** **`auto_ref.json`** uses the same three-way assumptions as **`auto_1_ref`** but a slightly different mix of indexed frequency columns (see diffs in-repo). Prefer **`auto_1_ref`** unless you need **`auto_ref`**’s column layout.

For **(A1, REF=EA, NEAF)** use **`auto_1_ref_neaf`**; **`auto_ref_neaf`** mirrors **`auto_ref`** with generic **NEAF**.

## `auto_raw.json` and sync

1. Edit **`auto_raw.json`**, or regenerate from **`auto.json`**: `python3 scripts/sync_auto_from_raw.py --init-raw`.
2. `python3 scripts/sync_auto_from_raw.py` merges into every **`formats/auto*.json`** except **`auto_raw.json`**.
3. `python3 scripts/check_auto_assumption_dict.py` — confirms each preset’s **`format_dict`** matches **`format_name`** (REF/ALT, effect index **A0/A1/A2**, generic **Frq**, and **`Freq{i}`** / **`A{i}FREQ`** aligned with **`A{i}`**).
4. `python3 create_formatbook.py`.

Downstream should use a concrete preset (`auto`, `auto_neaf`, `auto_ref`, …), not **`auto_raw`** alone.

## Preset table

| File | Non-default choices |
| --- | --- |
| `auto_raw.json` | (shared layer only) |
| `auto.json` | none — **1, alt, eaf** |
| `auto_0.json` | index **0** |
| `auto_2.json` | index **2** |
| `auto_ref.json` | **REF** = EA, **ALT** = NEA |
| `auto_neaf.json` | generic **Frq** → **NEAF** |
| `auto_0_neaf.json` | index **0** + **NEAF** |
| `auto_2_neaf.json` | index **2** + **NEAF** |

## REF + indexed (EAF generic)

| File | Non-default choices |
| --- | --- |
| `auto_0_ref.json` | index **0** + **REF** = EA |
| `auto_1_ref.json` | **REF** = EA (index 1 explicit in name for symmetry) |
| `auto_2_ref.json` | index **2** + **REF** = EA |

## REF + indexed + NEAF generic

| File | Non-default choices |
| --- | --- |
| `auto_ref_neaf.json` | **REF** = EA + generic **NEAF** (layout aligned with **`auto_ref`**) |
| `auto_0_ref_neaf.json` | index **0** + **REF** = EA + **NEAF** |
| `auto_1_ref_neaf.json` | index **1** + **REF** = EA + **NEAF** |
| `auto_2_ref_neaf.json` | index **2** + **REF** = EA + **NEAF** |

## Practical notes

- **`auto_0`** / **`auto`** / **`auto_2`** are mutually exclusive on which numbered allele is EA.
- For each preset, **`A{i}`**, **`A{i}FREQ`**, and **`Freq{i}`** (when present) use the same index **i** → **EA** maps to **EAF**, **NEA** to **NEAF** (e.g. under **`auto`**, **A0** is NEA so **A0FREQ** and **Freq0** are NEAF; under **`auto_2`**, **A2** is EA so **A2FREQ** / **Freq2** are EAF). Real files may use only a subset of these headers; validate unknown columns against the study’s coding.

See also [design.md](design.md).
