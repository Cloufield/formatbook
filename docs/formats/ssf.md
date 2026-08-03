# ssf

## Overview

| Field | Value |
| --- | --- |
| Format key | `ssf` |
| Spec file | `formats/ssf.json` |
| Cite name | GWAS-SSF v0.1 |
| Version | 20230328 |
| Source | [https://www.ebi.ac.uk/gwas/docs/summary-statistics-format](https://www.ebi.ac.uk/gwas/docs/summary-statistics-format) |
| Citation | Hayhurst, J., Buniello, A., Harris, L., Mosaku, A., Chang, C., Gignoux, C. R., ... & Barroso, I. (2022). A community driven GWAS summary statistics standard. bioRxiv. |
## File layout

| Field | Value |
| --- | --- |
| Separator | TAB |
| NA value | #NA |
| Column order | `chromosome`, `base_pair_location`, `effect_allele`, `other_allele`, `beta`, `odds_ratio`, `hazard_ratio`, `standard_error`, `effect_allele_frequency`, `p_value`, `neg_log_10_p_value`, `ci_upper`, `ci_lower`, `rsid`, `variant_id`, `info`, `ref_allele`, `n` |
## Column mapping

| Raw header | Canonical |
| --- | --- |
| `base_pair_location` | POS |
| `beta` | BETA |
| `chromosome` | CHR |
| `ci_lower` | OR_95L |
| `ci_upper` | OR_95U |
| `effect_allele` | EA |
| `effect_allele_frequency` | EAF |
| `hazard_ratio` | HR |
| `info` | INFO |
| `n` | N |
| `neg_log_10_p_value` | MLOG10P |
| `odds_ratio` | OR |
| `other_allele` | NEA |
| `p_value` | P |
| `ref_allele` | REF |
| `rsid` | rsID |
| `standard_error` | SE |
| `variant_id` | SNPID |
## Coverage

**9/9** tier groups satisfied.

| Tier | Status | Matched | Missing |
| --- | --- | --- | --- |
| Variant ID | yes | SNPID, rsID | — |
| Genomic location | yes | CHR, POS | — |
| Effect / other allele | yes | EA, NEA | — |
| Effect size | yes | BETA, OR, HR | Z |
| Uncertainty | yes | SE | — |
| P-value | yes | P, MLOG10P | — |
| Sample size | yes | N | N_CASE |
| Allele frequency | yes | EAF | MAF, NEAF |
| Imputation / QC | yes | INFO | — |
## See also

- [Format summary](../format_summary.html)
- [All formats](index.md)