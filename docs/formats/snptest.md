# snptest

## Overview

| Field | Value |
| --- | --- |
| Format key | `snptest` |
| Spec file | `formats/snptest.json` |
| Cite name | SNPTEST |
| Version | v2.5.4-beta3 |
| Source | [https://mathgen.stats.ox.ac.uk/genetics_software/snptest/snptest](https://mathgen.stats.ox.ac.uk/genetics_software/snptest/snptest) |
| Citation | Marchini, J., Howie, B., Myers, S., McVean, G., & Donnelly, P. (2007). A new multipoint method for genome-wide association studies via imputation of genotypes. Nature Genetics, 39(7), 906-913. |
## Column mapping

| Raw header | Canonical |
| --- | --- |
| `all_maf` | MAF |
| `all_total` | N |
| `allele_A` | NEA |
| `allele_B` | EA |
| `alleleA` | NEA |
| `alleleB` | EA |
| `alternate_ids` | SNPID |
| `average_maximum_posterior_call` | INFO |
| `bayesian_add_beta_1` | BETA |
| `bayesian_add_pvalue` | P |
| `bayesian_add_se_1` | SE |
| `cases_maf` | MAF_CASE |
| `cases_total` | N_CASE |
| `chromosome` | CHR |
| `controls_maf` | MAF_CONTROL |
| `controls_total` | N_CONTROL |
| `freq_allele_B` | EAF |
| `freq_alleleB` | EAF |
| `freqA` | EAF |
| `freqB` | EAF |
| `frequentist_add_beta_1` | BETA |
| `frequentist_add_OR_1` | OR |
| `frequentist_add_OR_95L_1` | OR_95L |
| `frequentist_add_OR_95U_1` | OR_95U |
| `frequentist_add_pvalue` | P |
| `frequentist_add_se_1` | SE |
| `id` | SNPID |
| `info` | INFO |
| `pos` | POS |
| `position` | POS |
| `rsid` | rsID |
## Coverage

**9/9** tier groups satisfied.

| Tier | Status | Matched | Missing |
| --- | --- | --- | --- |
| Variant ID | yes | SNPID, rsID | — |
| Genomic location | yes | CHR, POS | — |
| Effect / other allele | yes | EA, NEA | — |
| Effect size | yes | BETA, OR | HR, Z |
| Uncertainty | yes | SE | — |
| P-value | yes | P | MLOG10P |
| Sample size | yes | N, N_CASE | — |
| Allele frequency | yes | EAF, MAF | NEAF |
| Imputation / QC | yes | INFO | — |
## See also

- [Format summary](../format_summary.html)
- [All formats](index.md)