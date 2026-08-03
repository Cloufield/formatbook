# .bim

Extended variant map with .bed: CHR, SNP, CM, BP, A1 (first/clear-bit allele, usually minor), A2 (second/set-bit allele, usually major). PLINK 2 .bim lists ALT before REF but encodes the same roles as 1.x A1/A2.
## Overview

| Field | Value |
| --- | --- |
| Format key | `plink_bim` |
| Spec file | `formats/plink_bim.json` |
| Cite name | PLINK 1.9 |
| Version | PLINK 1.9 (doc revision 19 Aug 2025) |
| Last checked | 20260326 |
| Source | [https://www.cog-genomics.org/plink/1.9/formats#bim](https://www.cog-genomics.org/plink/1.9/formats#bim) |
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
| `0` | CHR |
| `1` | SNPID |
| `2` | CM |
| `3` | POS |
| `4` | EA |
| `5` | NEA |
## Header descriptions

| Column | Description |
| --- | --- |
| `0` | Chromosome code |
| `1` | Variant identifier |
| `2` | Genetic distance in morgans (often 0) |
| `3` | Base-pair coordinate (1-based) |
| `4` | Allele 1 (minor in .bed; first allele) |
| `5` | Allele 2 (major in .bed; second allele) |
## Coverage

**3/9** tier groups satisfied.

| Tier | Status | Matched | Missing |
| --- | --- | --- | --- |
| Variant ID | yes | SNPID | rsID |
| Genomic location | yes | CHR, POS | — |
| Effect / other allele | yes | EA, NEA | — |
| Effect size | no | — | BETA, OR, HR, Z |
| Uncertainty | no | — | SE |
| P-value | no | — | P, MLOG10P |
| Sample size | no | — | N, N_CASE |
| Allele frequency | no | — | EAF, MAF, NEAF |
| Imputation / QC | no | — | INFO |
## See also

- [Format summary](../format_summary.html)
- [All formats](index.md)