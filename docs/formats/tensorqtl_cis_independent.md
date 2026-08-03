# tensorqtl_cis_independent

tensorQTL cis-independent mode output format
## Overview

| Field | Value |
| --- | --- |
| Format key | `tensorqtl_cis_independent` |
| Spec file | `formats/tensorqtl_cis_independent.json` |
| Cite name | tensorQTL |
| Version | 20220726 |
| Source | [https://raw.githubusercontent.com/broadinstitute/tensorqtl/refs/heads/master/docs/outputs.md](https://raw.githubusercontent.com/broadinstitute/tensorqtl/refs/heads/master/docs/outputs.md) |
| GitHub | [https://github.com/broadinstitute/tensorqtl](https://github.com/broadinstitute/tensorqtl) |
| Citation | Taylor-Weiner, A., Aguet, F., Jones, M., Zaitlen, N., Daly, M., & Ardlie, K. (2019). Scaling computational genomics to millions of individuals with GPUs. Genome Biology, 20, 183. |
## Column mapping

| Raw header | Canonical |
| --- | --- |
| `af` | EAF |
| `beta_shape1` | BETA_SHAPE1 |
| `beta_shape2` | BETA_SHAPE2 |
| `end_distance` | END_DISTANCE |
| `ma_count` | MA_COUNT |
| `ma_samples` | MA_SAMPLES |
| `num_var` | NUM_VAR |
| `phenotype_id` | TRAIT |
| `pval_beta` | P_BETA |
| `pval_nominal` | P |
| `pval_perm` | P_PERM |
| `pval_true_df` | P_TRUE_DF |
| `rank` | RANK |
| `slope` | BETA |
| `slope_se` | SE |
| `start_distance` | START_DISTANCE |
| `true_df` | TRUE_DF |
| `variant_id` | SNPID |
## Header descriptions

| Column | Description |
| --- | --- |
| `af` | In-sample ALT allele frequency of the variant |
| `beta_shape1` | Parameter of the fitted Beta distribution |
| `beta_shape2` | Parameter of the fitted Beta distribution |
| `end_distance` | Distance between the variant and phenotype end position (only present if different from start position) |
| `ma_count` | Number of minor alleles |
| `ma_samples` | Number of samples carrying at least one minor allele |
| `num_var` | Number of variants in cis-window |
| `phenotype_id` | Phenotype ID |
| `pval_beta` | Beta-approximated empirical p-value |
| `pval_nominal` | Nominal p-value of the association between the phenotype and variant |
| `pval_perm` | Empirical p-value from permutations |
| `pval_true_df` | Nominal p-value based on true_df |
| `rank` | Rank of the variant for the phenotype |
| `slope` | Regression slope |
| `slope_se` | Standard error of the regression slope |
| `start_distance` | Distance between the variant and phenotype start position (e.g., TSS) |
| `true_df` | Degrees of freedom used to compute p-values |
| `variant_id` | Variant ID |
## Coverage

**5/9** tier groups satisfied.

| Tier | Status | Matched | Missing |
| --- | --- | --- | --- |
| Variant ID | yes | SNPID | rsID |
| Genomic location | no | — | CHR, POS |
| Effect / other allele | no | — | EA, NEA |
| Effect size | yes | BETA | OR, HR, Z |
| Uncertainty | yes | SE | — |
| P-value | yes | P | MLOG10P |
| Sample size | no | — | N, N_CASE |
| Allele frequency | yes | EAF | MAF, NEAF |
| Imputation / QC | no | — | INFO |
## See also

- [Format summary](../format_summary.html)
- [All formats](index.md)