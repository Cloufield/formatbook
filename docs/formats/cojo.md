# cojo

## Overview

| Field | Value |
| --- | --- |
| Format key | `cojo` |
| Spec file | `formats/cojo.json` |
| Cite name | GCTA-COJO |
| Version | 20230807 |
| Source | [https://yanglab.westlake.edu.cn/software/gcta/#COJO](https://yanglab.westlake.edu.cn/software/gcta/#COJO) |
| Citation | Yang, J., Ferreira, T., Morris, A. P., Medland, S. E., Madden, P. A., Heath, A. C., ... & Visscher, P. M. (2012). Conditional and joint multiple-SNP analysis of GWAS summary statistics identifies additional variants influencing complex traits. Nature genetics, 44(4), 369-375. |
## File layout

| Field | Value |
| --- | --- |
| Column order | `SNP`, `A1`, `A2`, `freq`, `b`, `se`, `p`, `N` |
## Column mapping

| Raw header | Canonical |
| --- | --- |
| `A1` | EA |
| `A2` | NEA |
| `b` | BETA |
| `freq` | EAF |
| `N` | N |
| `p` | P |
| `se` | SE |
| `SNP` | SNPID |
## Coverage

**7/9** tier groups satisfied.

| Tier | Status | Matched | Missing |
| --- | --- | --- | --- |
| Variant ID | yes | SNPID | rsID |
| Genomic location | no | — | CHR, POS |
| Effect / other allele | yes | EA, NEA | — |
| Effect size | yes | BETA | OR, HR, Z |
| Uncertainty | yes | SE | — |
| P-value | yes | P | MLOG10P |
| Sample size | yes | N | N_CASE |
| Allele frequency | yes | EAF | MAF, NEAF |
| Imputation / QC | no | — | INFO |
## See also

- [Format summary](../format_summary.html)
- [All formats](index.md)