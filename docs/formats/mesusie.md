# MESuSiE

## Overview

| Field | Value |
| --- | --- |
| Format key | `mesusie` |
| Spec file | `formats/mesusie.json` |
| Cite name | MESuSiE |
| Version | 20221109 |
| Source | [https://borangao.github.io/meSuSie_Analysis/](https://borangao.github.io/meSuSie_Analysis/) |
| GitHub | [https://github.com/borangao/MESuSiE](https://github.com/borangao/MESuSiE) |
| Citation | Gao, B., & Zhou, X. (2024). MESuSiE enables scalable and powerful multi-ancestry fine-mapping of causal variants in genome-wide association studies. Nature Genetics, 56(1), 170-179. |
## Column mapping

| Raw header | Canonical |
| --- | --- |
| `Beta` | BETA |
| `N` | N |
| `POS` | POS |
| `Se` | SE |
| `SNP` | SNPID |
| `Z` | Z |
## Coverage

**4/9** tier groups satisfied.

| Tier | Status | Matched | Missing |
| --- | --- | --- | --- |
| Variant ID | yes | SNPID | rsID |
| Genomic location | partial | POS | CHR |
| Effect / other allele | no | — | EA, NEA |
| Effect size | yes | BETA, Z | OR, HR |
| Uncertainty | yes | SE | — |
| P-value | no | — | P, MLOG10P |
| Sample size | yes | N | N_CASE |
| Allele frequency | no | — | EAF, MAF, NEAF |
| Imputation / QC | no | — | INFO |
## See also

- [Format summary](../format_summary.html)
- [All formats](index.md)