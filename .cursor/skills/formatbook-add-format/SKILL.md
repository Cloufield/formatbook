---
name: formatbook-add-format
description: Add or complete a GWAS summary-statistics format spec in formatbook. Use when adding formats/*.json, backfilling metadata, or auditing format coverage.
---

# Formatbook — add or complete a format

Read [checklist.md](checklist.md) and track progress per format. Details in [reference.md](reference.md).

## Pipeline

| Phase | Outputs |
|-------|---------|
| **1. Intake** | Software, analysis type, input/output role, example filename, docs URL |
| **2. Identity** | `formats/<key>.json` stem; `meta_data.format_name`; one spec per distinct column layout |
| **3. Provenance** | `format_source`, `format_source_2`, `github_url`, `format_version`, `last_check_date`, `software_license` |
| **4. Citation** | `format_cite_name`, `format_citation` (copy from `keys/software_citations.json` when possible) |
| **5. File layout** | `format_separator`, `format_na`, `format_comment`, `format_header`, `format_header_lines`, `format_col_order` |
| **6. Analysis context** | `format_description`, `format_assumption`, `format_notes` |
| **7. Header mapping** | `format_dict`, `format_dict_2`, `header_description` |
| **8. Validate and publish** | Run repo check scripts and regenerate catalog |

## Phase 3 — github_url

Set only when a GitHub repository exists. Form: `https://github.com/{owner}/{repo}` (repo root only).

- `format_source` = best documentation URL
- `github_url` = code repo when different
- Omit for docs-only tools (PLINK, METAL wiki, EBI catalog)

## Phase 4 — Citation lookup

1. Sibling specs in the same software family
2. `keys/software_citations.json`
3. `README.md` supported-formats table
4. `format_source` Cite us / References
5. Literature search

Never set `format_citation: null`.

## Phase 8 — Validate and publish

```bash
python3 scripts/check_format_jsons.py formats/
python3 scripts/check_format_jsons.py --strict
python3 scripts/format_pages.py
python3 scripts/format_summary.py
python3 create_formatbook.py
```
