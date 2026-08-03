# Formatbook add-format reference

## Authoritative docs

- [`docs/design.md`](../../../docs/design.md) — JSON structure, meta fields, SNPID/rsID policy
- [`formats/template.json`](../../../formats/template.json) — starter spec
- [`keys/software_citations.json`](../../../keys/software_citations.json) — shared cite_name, citation, github_url (copy manually into new specs; no apply script)
- [`keys/key_canonical_headers.json`](../../../keys/key_canonical_headers.json) — coverage tier groups

## Citing target

| Format type | Cite |
|-------------|------|
| Software output | Primary methods paper for the tool |
| Catalog file layout | Resource paper (GWAS Catalog, PGS Catalog) |
| Format specification | Spec paper (GWAS-VCF, GWAS-SSF) |

## `github_url` vs `format_source`

| Field | Purpose |
|-------|---------|
| `format_source` | Best URL for **column documentation** |
| `github_url` | **GitHub repo root** when code is hosted on GitHub |

## Family reuse

Copy identical `format_cite_name`, `format_citation`, and `github_url` across all specs for the same software (e.g. all `tensorqtl_*.json`, all PLINK 2.0 `plink2_*.json`).

## Worked examples

**Complete spec:** `formats/plink.json`, `formats/pheweb.json`

**Docs vs repo:** `formats/regenie.json` — `format_source` on regenie docs site; `github_url` → `https://github.com/rgcgithub/regenie`

**No GitHub:** `formats/metal.json` — omit `github_url`
