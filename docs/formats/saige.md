# saige

## Overview

| Field | Value |
| --- | --- |
| Format key | `saige` |
| Spec file | `formats/saige.json` |
| Cite name | SAIGE |
| Version | v1.1.3 |
| Last checked | 20220806 |
| Source | [https://saigegit.github.io/SAIGE-doc/docs/single_step2.html](https://saigegit.github.io/SAIGE-doc/docs/single_step2.html) |
| GitHub | [https://github.com/weizhouUMICH/SAIGE](https://github.com/weizhouUMICH/SAIGE) |
| Citation | Zhou, W., Nielsen, J. B., Fritsche, L. G., Dey, R., Gabrielsen, M. E., Wolford, B. N., ... & Lee, S. (2018). Efficiently controlling for case-control imbalance and sample relatedness in large-scale genetic association studies. Nature genetics, 50(9), 1335-1341. |
## Column mapping

| Raw header | Canonical |
| --- | --- |
| `AF_Allele2` | EAF |
| `Allele1` | NEA |
| `Allele2` | EA |
| `BETA` | BETA |
| `CHR` | CHR |
| `imputationInfo` | INFO |
| `N` | N |
| `p.value` | P |
| `POS` | POS |
| `SE` | SE |
| `SNPID` | SNPID |
## Coverage

**9/9** tier groups satisfied.

| Tier | Status | Matched | Missing |
| --- | --- | --- | --- |
| Variant ID | yes | SNPID | rsID |
| Genomic location | yes | CHR, POS | — |
| Effect / other allele | yes | EA, NEA | — |
| Effect size | yes | BETA | OR, HR, Z |
| Uncertainty | yes | SE | — |
| P-value | yes | P | MLOG10P |
| Sample size | yes | N | N_CASE |
| Allele frequency | yes | EAF | MAF, NEAF |
| Imputation / QC | yes | INFO | — |
## See also

- [Format summary](../format_summary.html)
- [All formats](index.md)