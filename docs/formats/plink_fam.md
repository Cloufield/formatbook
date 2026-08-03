# .fam

Per-sample row for .bed: FID, IID, father IID, mother IID, sex, phenotype. Quantitative phenotype if numeric values other than {-9,0,1,2} appear.
## Overview

| Field | Value |
| --- | --- |
| Format key | `plink_fam` |
| Spec file | `formats/plink_fam.json` |
| Cite name | PLINK 1.9 |
| Version | PLINK 1.9 (doc revision 19 Aug 2025) |
| Last checked | 20260326 |
| Source | [https://www.cog-genomics.org/plink/1.9/formats#fam](https://www.cog-genomics.org/plink/1.9/formats#fam) |
| Citation | Purcell, S., Neale, B., Todd-Brown, K., Thomas, L., Ferreira, M. A., Bender, D., ... & Sham, P. C. (2007). PLINK: a tool set for whole-genome association and population-based linkage analyses. The American journal of human genetics, 81(3), 559-575. |
## File layout

| Field | Value |
| --- | --- |
| Separator | TAB |
| Header row | no |
| Column order | `0`, `1`, `2`, `3`, `4`, `5` |
## Column mapping

| Raw header | Canonical |
| --- | --- |
| `0` | FID |
| `1` | IID |
| `2` | PAT |
| `3` | MAT |
| `4` | SEX |
| `5` | PHENO1 |
## Header descriptions

| Column | Description |
| --- | --- |
| `0` | Family ID |
| `1` | Within-family ID (cannot be '0') |
| `2` | Paternal IID ('0' if unknown) |
| `3` | Maternal IID ('0' if unknown) |
| `4` | Sex (1=male, 2=female, 0=unknown) |
| `5` | Phenotype (1=control, 2=case; -9/0/non-numeric missing for case/control) |
## Coverage

**0/9** tier groups satisfied.

| Tier | Status | Matched | Missing |
| --- | --- | --- | --- |
| Variant ID | no | — | SNPID, rsID |
| Genomic location | no | — | CHR, POS |
| Effect / other allele | no | — | EA, NEA |
| Effect size | no | — | BETA, OR, HR, Z |
| Uncertainty | no | — | SE |
| P-value | no | — | P, MLOG10P |
| Sample size | no | — | N, N_CASE |
| Allele frequency | no | — | EAF, MAF, NEAF |
| Imputation / QC | no | — | INFO |
## See also

- [Format summary](../format_summary.html)
- [All formats](index.md)