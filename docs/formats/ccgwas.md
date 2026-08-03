# CCGWAS

## Overview

| Field | Value |
| --- | --- |
| Format key | `ccgwas` |
| Spec file | `formats/ccgwas.json` |
| Cite name | CC-GWAS |
| Version | 20220901 |
| Last checked | 20250416 |
| Source | [https://github.com/wouterpeyrot/CCGWAS#output-files](https://github.com/wouterpeyrot/CCGWAS#output-files) |
| GitHub | [https://github.com/wouterpeyrot/CCGWAS](https://github.com/wouterpeyrot/CCGWAS) |
| Citation | Peyrot, W. J., & Price, A. L. (2021). Identifying loci with different allele frequencies among cases of eight psychiatric disorders using CC-GWAS. Nature genetics, 53(4), 445-454. |
## File layout

| Field | Value |
| --- | --- |
| Separator | TAB |
## Column mapping

| Raw header | Canonical |
| --- | --- |
| `A1` | EA |
| `A2` | NEA |
| `BP` | POS |
| `CCGWAS_signif` | — |
| `CHR` | CHR |
| `Exact_beta` | — |
| `Exact_pval` | — |
| `Exact_se` | — |
| `OLS_beta` | BETA |
| `OLS_pval` | P |
| `OLS_se` | SE |
| `SNP` | SNPID |
## Coverage

**6/9** tier groups satisfied.

| Tier | Status | Matched | Missing |
| --- | --- | --- | --- |
| Variant ID | yes | SNPID | rsID |
| Genomic location | yes | CHR, POS | — |
| Effect / other allele | yes | EA, NEA | — |
| Effect size | yes | BETA | OR, HR, Z |
| Uncertainty | yes | SE | — |
| P-value | yes | P | MLOG10P |
| Sample size | no | — | N, N_CASE |
| Allele frequency | no | — | EAF, MAF, NEAF |
| Imputation / QC | no | — | INFO |
## See also

- [Format summary](../format_summary.html)
- [All formats](index.md)