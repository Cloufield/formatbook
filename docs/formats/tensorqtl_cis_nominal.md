# tensorqtl_cis_nominal

tensorQTL cis-nominal mode output format
## Overview

| Field | Value |
| --- | --- |
| Format key | `tensorqtl_cis_nominal` |
| Spec file | `formats/tensorqtl_cis_nominal.json` |
| Cite name | tensorQTL |
| Version | 20220726 |
| Source | [https://raw.githubusercontent.com/broadinstitute/tensorqtl/refs/heads/master/docs/outputs.md](https://raw.githubusercontent.com/broadinstitute/tensorqtl/refs/heads/master/docs/outputs.md) |
| GitHub | [https://github.com/broadinstitute/tensorqtl](https://github.com/broadinstitute/tensorqtl) |
| Citation | Taylor-Weiner, A., Aguet, F., Jones, M., Zaitlen, N., Daly, M., & Ardlie, K. (2019). Scaling computational genomics to millions of individuals with GPUs. Genome Biology, 20, 183. |
## Column mapping

| Raw header | Canonical |
| --- | --- |
| `af` | EAF |
| `end_distance` | END_DISTANCE |
| `ma_count` | MA_COUNT |
| `ma_samples` | MA_SAMPLES |
| `phenotype_id` | TRAIT |
| `pval_nominal` | P |
| `slope` | BETA |
| `slope_se` | SE |
| `start_distance` | START_DISTANCE |
| `variant_id` | SNPID |
## Header descriptions

| Column | Description |
| --- | --- |
| `af` | In-sample ALT allele frequency of the variant |
| `end_distance` | Distance between the variant and phenotype end position (only present if different from start position) |
| `ma_count` | Number of minor alleles |
| `ma_samples` | Number of samples carrying at least one minor allele |
| `phenotype_id` | Phenotype ID |
| `pval_nominal` | Nominal p-value of the association between the phenotype and variant |
| `slope` | Regression slope |
| `slope_se` | Standard error of the regression slope |
| `start_distance` | Distance between the variant and phenotype start position (e.g., TSS) |
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