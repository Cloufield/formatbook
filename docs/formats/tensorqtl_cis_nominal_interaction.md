# tensorqtl_cis_nominal_interaction

tensorQTL cis-nominal mode with interaction term output format
## Overview

| Field | Value |
| --- | --- |
| Format key | `tensorqtl_cis_nominal_interaction` |
| Spec file | `formats/tensorqtl_cis_nominal_interaction.json` |
| Cite name | tensorQTL |
| Version | 20220726 |
| Source | [https://raw.githubusercontent.com/broadinstitute/tensorqtl/refs/heads/master/docs/outputs.md](https://raw.githubusercontent.com/broadinstitute/tensorqtl/refs/heads/master/docs/outputs.md) |
| GitHub | [https://github.com/broadinstitute/tensorqtl](https://github.com/broadinstitute/tensorqtl) |
| Citation | Taylor-Weiner, A., Aguet, F., Jones, M., Zaitlen, N., Daly, M., & Ardlie, K. (2019). Scaling computational genomics to millions of individuals with GPUs. Genome Biology, 20, 183. |
## Column mapping

| Raw header | Canonical |
| --- | --- |
| `af` | EAF |
| `b_g` | BETA_G |
| `b_g_se` | SE_G |
| `b_gi` | BETA_GI |
| `b_gi_se` | SE_GI |
| `b_i` | BETA_I |
| `b_i_se` | SE_I |
| `end_distance` | END_DISTANCE |
| `ma_count` | MA_COUNT |
| `ma_samples` | MA_SAMPLES |
| `phenotype_id` | TRAIT |
| `pval_adj_bh` | P_ADJ_BH |
| `pval_emt` | P_EMT |
| `pval_g` | P_G |
| `pval_gi` | P_GI |
| `pval_i` | P_I |
| `start_distance` | START_DISTANCE |
| `tests_emt` | TESTS_EMT |
| `variant_id` | SNPID |
## Header descriptions

| Column | Description |
| --- | --- |
| `af` | In-sample ALT allele frequency of the variant |
| `b_g` | Slope of the genotype term |
| `b_g_se` | Standard error of b_g |
| `b_gi` | Slope of the interaction term |
| `b_gi_se` | Standard error of b_gi |
| `b_i` | Slope of the interaction variable |
| `b_i_se` | Standard error of b_i |
| `end_distance` | Distance between the variant and phenotype end position (only present if different from start position) |
| `ma_count` | Number of minor alleles |
| `ma_samples` | Number of samples carrying at least one minor allele |
| `phenotype_id` | Phenotype ID |
| `pval_adj_bh` | Benjamini-Hochberg adjusted pval_emt |
| `pval_emt` | Bonferroni-adjusted pval_gi (i.e., multiplied by M_eff) |
| `pval_g` | Nominal p-value of the genotype term |
| `pval_gi` | Nominal p-value of the interaction term |
| `pval_i` | Nominal p-value of the interaction variable |
| `start_distance` | Distance between the variant and phenotype start position (e.g., TSS) |
| `tests_emt` | Effective number of independent variants (M_eff) estimated by eigenMT |
| `variant_id` | Variant ID |
## Coverage

**2/9** tier groups satisfied.

| Tier | Status | Matched | Missing |
| --- | --- | --- | --- |
| Variant ID | yes | SNPID | rsID |
| Genomic location | no | — | CHR, POS |
| Effect / other allele | no | — | EA, NEA |
| Effect size | no | — | BETA, OR, HR, Z |
| Uncertainty | no | — | SE |
| P-value | no | — | P, MLOG10P |
| Sample size | no | — | N, N_CASE |
| Allele frequency | yes | EAF | MAF, NEAF |
| Imputation / QC | no | — | INFO |
## See also

- [Format summary](../format_summary.html)
- [All formats](index.md)