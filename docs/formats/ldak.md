# ldak

LDAK/SumHer summary statistics with Predictor, A1, A2, n, and either Z or BETA plus SE; A1Freq is recommended.
## Overview

| Field | Value |
| --- | --- |
| Format key | `ldak` |
| Spec file | `formats/ldak.json` |
| Cite name | LDAK/SumHer |
| Version | 20260801 |
| Last checked | 20260801 |
| Source | [https://dougspeed.com/summary-statistics/](https://dougspeed.com/summary-statistics/) |
| Citation | Speed D, Holmes J, Sumner MD, et al. (2020). Reevaluation of SNP heritability in complex human traits. Nature Genetics. |
## File layout

| Field | Value |
| --- | --- |
| Separator | TAB |
| Header row | yes |
| Column order | `Predictor`, `A1`, `A2`, `Z`, `BETA`, `SE`, `n`, `A1Freq` |
## Column mapping

| Raw header | Canonical |
| --- | --- |
| `A1` | EA |
| `A1Freq` | EAF |
| `A2` | NEA |
| `BETA` | BETA |
| `n` | N |
| `Predictor` | SNPID |
| `SE` | SE |
| `Z` | Z |
## Coverage

**6/9** tier groups satisfied.

| Tier | Status | Matched | Missing |
| --- | --- | --- | --- |
| Variant ID | yes | SNPID | rsID |
| Genomic location | no | — | CHR, POS |
| Effect / other allele | yes | EA, NEA | — |
| Effect size | yes | BETA, Z | OR, HR |
| Uncertainty | yes | SE | — |
| P-value | no | — | P, MLOG10P |
| Sample size | yes | N | N_CASE |
| Allele frequency | yes | EAF | MAF, NEAF |
| Imputation / QC | no | — | INFO |
## See also

- [Format summary](../format_summary.html)
- [All formats](index.md)