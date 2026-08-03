# gwascatalog_hm

## Overview

| Field | Value |
| --- | --- |
| Format key | `gwascatalog_hm` |
| Spec file | `formats/gwascatalog_hm.json` |
| Cite name | GWAS Catalog |
| Version | 20220806 |
| Source | [https://www.ebi.ac.uk/gwas/docs/methods/summary-statistics](https://www.ebi.ac.uk/gwas/docs/methods/summary-statistics) |
| Citation | Buniello, A., MacArthur, J. A. L., Cerezo, M., Harris, L. W., Hayhurst, J., Malangone, C., ... & Parkinson, H. (2019). The NHGRI-EBI GWAS Catalog of published genome-wide association studies, targeted arrays and summary statistics 2019. Nucleic acids research, 47(D1), D1005-D1012. |
## Column mapping

| Raw header | Canonical |
| --- | --- |
| `base_pair_location` | POS |
| `chromosome` | CHR |
| `hm_beta` | BETA |
| `hm_ci_lower` | OR_95L |
| `hm_ci_upper` | OR_95U |
| `hm_effect_allele` | EA |
| `hm_effect_allele_frequency` | EAF |
| `hm_odds_ratio` | OR |
| `hm_other_allele` | NEA |
| `hm_variant_id` | SNPID |
| `p_value` | P |
| `standard_error` | SE |
## Coverage

**7/9** tier groups satisfied.

| Tier | Status | Matched | Missing |
| --- | --- | --- | --- |
| Variant ID | yes | SNPID | rsID |
| Genomic location | yes | CHR, POS | — |
| Effect / other allele | yes | EA, NEA | — |
| Effect size | yes | BETA, OR | HR, Z |
| Uncertainty | yes | SE | — |
| P-value | yes | P | MLOG10P |
| Sample size | no | — | N, N_CASE |
| Allele frequency | yes | EAF | MAF, NEAF |
| Imputation / QC | no | — | INFO |
## See also

- [Format summary](../format_summary.html)
- [All formats](index.md)