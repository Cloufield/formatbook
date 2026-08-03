# fastgwa

## Overview

| Field | Value |
| --- | --- |
| Format key | `fastgwa` |
| Spec file | `formats/fastgwa.json` |
| Cite name | fastGWA |
| Version | 20220726 |
| Source | [https://yanglab.westlake.edu.cn/software/gcta/#fastGWA](https://yanglab.westlake.edu.cn/software/gcta/#fastGWA) |
| Source (2) | [https://yanglab.westlake.edu.cn/software/gcta/#fastGWA-GLMM](https://yanglab.westlake.edu.cn/software/gcta/#fastGWA-GLMM) |
| Citation | Jiang, L., Zheng, Z., Qi, T., Kemper, K. E., Wray, N. R., Visscher, P. M., & Yang, J. (2019). A resource-efficient tool for mixed model association analysis of large-scale data. Nature genetics, 51(12), 1749-1755. |
## Column mapping

| Raw header | Canonical |
| --- | --- |
| `A1` | EA |
| `A2` | NEA |
| `AF1` | EAF |
| `BETA` | BETA |
| `CHR` | CHR |
| `P` | P |
| `POS` | POS |
| `SE` | SE |
| `SNP` | SNPID |
## Coverage

**7/9** tier groups satisfied.

| Tier | Status | Matched | Missing |
| --- | --- | --- | --- |
| Variant ID | yes | SNPID | rsID |
| Genomic location | yes | CHR, POS | — |
| Effect / other allele | yes | EA, NEA | — |
| Effect size | yes | BETA | OR, HR, Z |
| Uncertainty | yes | SE | — |
| P-value | yes | P | MLOG10P |
| Sample size | no | — | N, N_CASE |
| Allele frequency | yes | EAF | MAF, NEAF |
| Imputation / QC | no | — | INFO |
## See also

- [Format summary](../format_summary.html)
- [All formats](index.md)