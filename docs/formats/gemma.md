# gemma

## Overview

| Field | Value |
| --- | --- |
| Format key | `gemma` |
| Spec file | `formats/gemma.json` |
| Cite name | GEMMA |
| Version | 0.98.5 |
| Source | [https://github.com/genetics-statistics/GEMMA](https://github.com/genetics-statistics/GEMMA) |
| GitHub | [https://github.com/genetics-statistics/GEMMA](https://github.com/genetics-statistics/GEMMA) |
| Citation | Zhou, X., & Stephens, M. (2012). Genome-wide efficient mixed-model analysis for association studies. Nature Genetics, 44(7), 821-824. |
## File layout

| Field | Value |
| --- | --- |
| Separator | TAB |
| Comment prefix | GEMMA univariate linear mixed model (LMM) output format. Columns: chr, rs, ps, n_miss, allele1, allele0, af, beta, se, l_remle, p_wald. The output is tab-separated. allele1 is the effect allele, allele0 is the non-effect allele, af is the allele frequency of allele1, and l_remle is the log-likelihood ratio test statistic. |
## Column mapping

| Raw header | Canonical |
| --- | --- |
| `af` | EAF |
| `allele0` | NEA |
| `allele1` | EA |
| `beta` | BETA |
| `chr` | CHR |
| `l_remle` | L_REMLE |
| `n_miss` | N_MISS |
| `p_wald` | P |
| `ps` | POS |
| `rs` | rsID |
| `se` | SE |
## Coverage

**7/9** tier groups satisfied.

| Tier | Status | Matched | Missing |
| --- | --- | --- | --- |
| Variant ID | yes | rsID | SNPID |
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