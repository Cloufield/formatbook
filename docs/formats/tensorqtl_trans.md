# tensorqtl_trans

tensorQTL trans mode output format
## Overview

| Field | Value |
| --- | --- |
| Format key | `tensorqtl_trans` |
| Spec file | `formats/tensorqtl_trans.json` |
| Cite name | tensorQTL |
| Version | 20220726 |
| Source | [https://raw.githubusercontent.com/broadinstitute/tensorqtl/refs/heads/master/docs/outputs.md](https://raw.githubusercontent.com/broadinstitute/tensorqtl/refs/heads/master/docs/outputs.md) |
| GitHub | [https://github.com/broadinstitute/tensorqtl](https://github.com/broadinstitute/tensorqtl) |
| Citation | Taylor-Weiner, A., Aguet, F., Jones, M., Zaitlen, N., Daly, M., & Ardlie, K. (2019). Scaling computational genomics to millions of individuals with GPUs. Genome Biology, 20, 183. |
## Column mapping

| Raw header | Canonical |
| --- | --- |
| `af` | EAF |
| `b` | BETA |
| `b_se` | SE |
| `phenotype_id` | TRAIT |
| `pval` | P |
| `r2` | R2 |
| `variant_id` | SNPID |
## Header descriptions

| Column | Description |
| --- | --- |
| `af` | In-sample ALT allele frequency of the variant |
| `b` | Regression slope |
| `b_se` | Standard error of the regression slope |
| `phenotype_id` | Phenotype ID |
| `pval` | Nominal p-value of the association between the phenotype and variant |
| `r2` | Squared residual genotype-phenotype correlation (only generated if map_trans(..., return_r2=True)) |
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