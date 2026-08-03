# popcorn

## Overview

| Field | Value |
| --- | --- |
| Format key | `popcorn` |
| Spec file | `formats/popcorn.json` |
| Cite name | Popcorn |
| Version | 20230807 |
| Source | [https://github.com/brielin/Popcorn](https://github.com/brielin/Popcorn) |
| GitHub | [https://github.com/brielin/Popcorn](https://github.com/brielin/Popcorn) |
| Citation | Brown, B. C., Ye, C. J., Price, A. L., & Zaitlen, N. (2016). Transethnic genetic-correlation estimates from summary statistics. The American Journal of Human Genetics, 99(1), 76-88. |
## File layout

| Field | Value |
| --- | --- |
| Column order | `rsid`, `A1`, `A2`, `N`, `beta`, `SE`, `OR`, `p-value`, `Z`, `AF` |
## Column mapping

| Raw header | Canonical |
| --- | --- |
| `A1` | NEA |
| `A2` | EA |
| `AF` | EAF |
| `beta` | BETA |
| `N` | N |
| `OR` | OR |
| `p-value` | P |
| `rsid` | rsID |
| `SE` | SE |
| `Z` | Z |
## Coverage

**7/9** tier groups satisfied.

| Tier | Status | Matched | Missing |
| --- | --- | --- | --- |
| Variant ID | yes | rsID | SNPID |
| Genomic location | no | — | CHR, POS |
| Effect / other allele | yes | EA, NEA | — |
| Effect size | yes | BETA, OR, Z | HR |
| Uncertainty | yes | SE | — |
| P-value | yes | P | MLOG10P |
| Sample size | yes | N | N_CASE |
| Allele frequency | yes | EAF | MAF, NEAF |
| Imputation / QC | no | — | INFO |
## See also

- [Format summary](../format_summary.html)
- [All formats](index.md)