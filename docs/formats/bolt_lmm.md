# .stats

## Overview

| Field | Value |
| --- | --- |
| Format key | `bolt_lmm` |
| Spec file | `formats/bolt_lmm.json` |
| Cite name | BOLT-LMM |
| Version | v2.4 (July 22, 2022) |
| Source | [https://alkesgroup.broadinstitute.org/BOLT-LMM/BOLT-LMM_manual.html](https://alkesgroup.broadinstitute.org/BOLT-LMM/BOLT-LMM_manual.html) |
| Citation | Loh, P. R., Tucker, G., Bulik-Sullivan, B. K., Vilhjalmsson, B. J., Finucane, H. K., Salem, R. M., ... & Price, A. L. (2015). Efficient Bayesian mixed-model analysis increases association power in large cohorts. Nature genetics, 47(3), 284-290. |
## Column mapping

| Raw header | Canonical |
| --- | --- |
| `A1FREQ` | EAF |
| `ALLELE0` | NEA |
| `ALLELE1` | EA |
| `BETA` | BETA |
| `BP` | POS |
| `CHISQ_BOLT_LMM` | CHISQ |
| `CHR` | CHR |
| `INFO` | INFO |
| `P_BOLT_LMM` | P |
| `SE` | SE |
| `SNP` | SNPID |
## Coverage

**8/9** tier groups satisfied.

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
| Imputation / QC | yes | INFO | — |
## See also

- [Format summary](../format_summary.html)
- [All formats](index.md)