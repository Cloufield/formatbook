# pheweb

## Overview

| Field | Value |
| --- | --- |
| Format key | `pheweb` |
| Spec file | `formats/pheweb.json` |
| Cite name | PheWeb |
| Version | 20220928 |
| Last checked | 20250106 |
| Source | [https://github.com/statgen/pheweb](https://github.com/statgen/pheweb) |
| GitHub | [https://github.com/statgen/pheweb](https://github.com/statgen/pheweb) |
| Citation | Gagliano Taliun, S.A., VandeHaar, P. et al. Exploring and visualizing large-scale genetic associations by using PheWeb. Nat Genet 52, 550–552 (2020). |
## File layout

| Field | Value |
| --- | --- |
| Separator | 'tab, space, or comma' |
| NA value | , ., NA, N/A, n/a, nan, -nan, NaN, -NaN, null, NULL |
| Header row | yes |
## Column mapping

| Raw header | Canonical |
| --- | --- |
| `#chrom` | CHR |
| `a1freq` | EAF |
| `ac` | N |
| `af` | EAF |
| `af.cases` | EAF_CASE |
| `af.controls` | EAF_CONTROL |
| `alt` | EA |
| `alternate` | EA |
| `beg` | POS |
| `begin` | POS |
| `beta` | BETA |
| `bp` | POS |
| `case_af` | EAF_CASE |
| `chr` | CHR |
| `chrom` | CHR |
| `control_af` | EAF_CONTROL |
| `frq` | EAF |
| `maf` | MAF |
| `marker_id` | SNPID |
| `n` | N |
| `n_cases` | N_CASE |
| `n_controls` | N_CONTROL |
| `ns` | N |
| `ns.case` | N_CASE |
| `ns.ctrl` | N_CONTROL |
| `num_cases` | N_CASE |
| `num_controls` | N_CONTROL |
| `num_samples` | N |
| `or` | OR |
| `p` | P |
| `p.value` | P |
| `pos` | POS |
| `pval` | P |
| `pvalue` | P |
| `r2` | INFO |
| `ref` | NEA |
| `reference` | NEA |
| `se` | SE |
| `sebeta` | SE |
## Notes

- File can be gzipped
- Variants must be sorted by chromosome and position, with chromosomes in order [1-22,X,Y,MT]
- Column names are case-insensitive
- Reference allele must match the reference genome specified in config.py (hg_build_number 19 or 38)
- If pval is log10 (e.g., REGENIE output), set pval_is_neglog10 = True in config.py
- Custom column names can be mapped using field_aliases in config.py
## Coverage

**9/9** tier groups satisfied.

| Tier | Status | Matched | Missing |
| --- | --- | --- | --- |
| Variant ID | yes | SNPID | rsID |
| Genomic location | yes | CHR, POS | — |
| Effect / other allele | yes | EA, NEA | — |
| Effect size | yes | BETA, OR | HR, Z |
| Uncertainty | yes | SE | — |
| P-value | yes | P | MLOG10P |
| Sample size | yes | N, N_CASE | — |
| Allele frequency | yes | EAF, MAF | NEAF |
| Imputation / QC | yes | INFO | — |
## See also

- [Format summary](../format_summary.html)
- [All formats](index.md)