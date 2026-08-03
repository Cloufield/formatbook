# bgenie

## Overview

| Field | Value |
| --- | --- |
| Format key | `bgenie` |
| Spec file | `formats/bgenie.json` |
| Cite name | BGENIE |
| Version | latest |
| Source | [https://jmarchini.org/bgenie/](https://jmarchini.org/bgenie/) |
| Citation | Bycroft, C., Freeman, C., Petkova, D., Band, G., Elliott, L. T., Sharp, K., Motyer, A., Vukcevic, D., Delaneau, O., O'Connell, J., Cortes, A., Welsh, S., McVean, G., Leslie, S., Donnelly, P., & Marchini, J. (2018). The UK Biobank resource with deep phenotyping and genomic data. Nature, 562(7726), 203-209. |
## File layout

| Field | Value |
| --- | --- |
| Separator | SPACE |
| Comment prefix | BGENIE output is space-separated and gzip compressed. Phenotype-specific columns follow the pattern {pheno_name}_beta, {pheno_name}_se, {pheno_name}_t, and optionally {pheno_name}_p (if --pvals flag is used). The beta coefficient refers to the effect of having an extra copy of a_1 (the second allele). |
## Column mapping

| Raw header | Canonical |
| --- | --- |
| `a_0` | NEA |
| `a_1` | EA |
| `af` | EAF |
| `chr` | CHR |
| `info` | INFO |
| `pheno1_beta` | BETA |
| `pheno1_p` | MLOG10P |
| `pheno1_se` | SE |
| `pheno1_t` | T |
| `pos` | POS |
| `rsid` | rsID |
## Coverage

**8/9** tier groups satisfied.

| Tier | Status | Matched | Missing |
| --- | --- | --- | --- |
| Variant ID | yes | rsID | SNPID |
| Genomic location | yes | CHR, POS | — |
| Effect / other allele | yes | EA, NEA | — |
| Effect size | yes | BETA | OR, HR, Z |
| Uncertainty | yes | SE | — |
| P-value | yes | MLOG10P | P |
| Sample size | no | — | N, N_CASE |
| Allele frequency | yes | EAF | MAF, NEAF |
| Imputation / QC | yes | INFO | — |
## See also

- [Format summary](../format_summary.html)
- [All formats](index.md)