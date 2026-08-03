# mtag

## Overview

| Field | Value |
| --- | --- |
| Format key | `mtag` |
| Spec file | `formats/mtag.json` |
| Cite name | MTAG v1.0.8 |
| Version | v1.0.8 |
| Source | [https://github.com/JonJala/mtag/wiki/Tutorial-1:-The-Basics](https://github.com/JonJala/mtag/wiki/Tutorial-1:-The-Basics) |
| GitHub | [https://github.com/JonJala/mtag](https://github.com/JonJala/mtag) |
| Citation | Turley, P., Walters, R. K., Maghzian, O., Okbay, A., Lee, J. J., Fontana, M. A., ... & Benjamin, D. J. (2018). Multi-trait analysis of genome-wide association summary statistics using MTAG. Nature Genetics, 50(2), 229-237. |
## File layout

| Field | Value |
| --- | --- |
| Separator | TAB |
| Column order | `snpid`, `chr`, `bpos`, `a1`, `a2`, `freq`, `beta`, `se`, `z`, `pval`, `p_value`, `n` |
## Column mapping

| Raw header | Canonical |
| --- | --- |
| `a1` | EA |
| `a2` | NEA |
| `beta` | BETA |
| `bpos` | POS |
| `chr` | CHR |
| `freq` | EAF |
| `n` | N |
| `p_value` | P |
| `pval` | P |
| `se` | SE |
| `snpid` | rsID |
| `z` | Z |
## Coverage

**8/9** tier groups satisfied.

| Tier | Status | Matched | Missing |
| --- | --- | --- | --- |
| Variant ID | yes | rsID | SNPID |
| Genomic location | yes | CHR, POS | — |
| Effect / other allele | yes | EA, NEA | — |
| Effect size | yes | BETA, Z | OR, HR |
| Uncertainty | yes | SE | — |
| P-value | yes | P | MLOG10P |
| Sample size | yes | N | N_CASE |
| Allele frequency | yes | EAF | MAF, NEAF |
| Imputation / QC | no | — | INFO |
## See also

- [Format summary](../format_summary.html)
- [All formats](index.md)