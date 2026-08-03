# pgscatalog

## Overview

| Field | Value |
| --- | --- |
| Format key | `pgscatalog` |
| Spec file | `formats/pgscatalog.json` |
| Cite name | PGS Catalog |
| Version | 20220726 |
| Source | [https://www.pgscatalog.org/downloads/](https://www.pgscatalog.org/downloads/) |
| Citation | Lambert, S. A., Gil, L., Jupp, S., Ritchie, S. C., Xu, Y., Buniello, A., ... & Inouye, M. (2021). The Polygenic Score Catalog as an open database for reproducibility and systematic evaluation. Nature Genetics, 53(4), 420-425. |
## Column mapping

| Raw header | Canonical |
| --- | --- |
| `allelefrequency_effect` | EAF |
| `chr_name` | CHR |
| `chr_position` | POS |
| `effect_allele` | EA |
| `effect_weight` | BETA |
| `OR` | OR |
| `other_allele` | NEA |
| `rsID` | rsID |
## Coverage

**5/9** tier groups satisfied.

| Tier | Status | Matched | Missing |
| --- | --- | --- | --- |
| Variant ID | yes | rsID | SNPID |
| Genomic location | yes | CHR, POS | — |
| Effect / other allele | yes | EA, NEA | — |
| Effect size | yes | BETA, OR | HR, Z |
| Uncertainty | no | — | SE |
| P-value | no | — | P, MLOG10P |
| Sample size | no | — | N, N_CASE |
| Allele frequency | yes | EAF | MAF, NEAF |
| Imputation / QC | no | — | INFO |
## See also

- [Format summary](../format_summary.html)
- [All formats](index.md)