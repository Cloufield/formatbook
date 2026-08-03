# mrmega

## Overview

| Field | Value |
| --- | --- |
| Format key | `mrmega` |
| Spec file | `formats/mrmega.json` |
| Cite name | MR-MEGA |
| Version | ver0.2 |
| Last checked | 20220806 |
| Source | [https://genomics.ut.ee/en/tools](https://genomics.ut.ee/en/tools) |
| Citation | Mägi, R., Horikoshi, M., Sofer, T., Mahajan, A., Kitajima, H., Franceschini, N., ... & Morris, A. P. (2017). Trans-ethnic meta-regression of genome-wide association studies accounting for ancestry increases power for discovery and improves fine-mapping resolution. Human molecular genetics, 26(18), 3639-3650. |
## Column mapping

| Raw header | Canonical |
| --- | --- |
| `chisq_association` | CHISQ |
| `Chromosome` | CHR |
| `EA` | EA |
| `EAF` | EAF |
| `Effects` | DIRECTION |
| `MarkerName ` | SNPID |
| `ndf_association` | ndf_association |
| `NEA` | NEA |
| `Nsample` | N |
| `P-value_association` | P |
| `Position` | POS |
## Coverage

**6/9** tier groups satisfied.

| Tier | Status | Matched | Missing |
| --- | --- | --- | --- |
| Variant ID | yes | SNPID | rsID |
| Genomic location | yes | CHR, POS | — |
| Effect / other allele | yes | EA, NEA | — |
| Effect size | no | — | BETA, OR, HR, Z |
| Uncertainty | no | — | SE |
| P-value | yes | P | MLOG10P |
| Sample size | yes | N | N_CASE |
| Allele frequency | yes | EAF | MAF, NEAF |
| Imputation / QC | no | — | INFO |
## See also

- [Format summary](../format_summary.html)
- [All formats](index.md)