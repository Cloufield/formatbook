# ldsc

## Overview

| Field | Value |
| --- | --- |
| Format key | `ldsc` |
| Spec file | `formats/ldsc.json` |
| Cite name | LDSC |
| Version | 20150306 |
| Source | [https://github.com/bulik/ldsc/wiki/Summary-Statistics-File-Format](https://github.com/bulik/ldsc/wiki/Summary-Statistics-File-Format) |
| Source (2) | [https://github.com/bulik/ldsc/blob/master/munge_sumstats.py](https://github.com/bulik/ldsc/blob/master/munge_sumstats.py) |
| GitHub | [https://github.com/bulik/ldsc](https://github.com/bulik/ldsc) |
| Citation | Bulik-Sullivan, B. K., Loh, P. R., Finucane, H. K., Ripke, S., Yang, J., Patterson, N., ... & Neale, B. M. (2015). LD Score regression distinguishes confounding from polygenicity in genome-wide association studies. Nature genetics, 47(3), 291-295. |
## Column mapping

| Raw header | Canonical | Canonical (secondary) |
| --- | --- | --- |
| `A1` | EA | — |
| `A2` | NEA | — |
| `Beta` | BETA | — |
| `CHR` | CHR | — |
| `Frq` | EAF | — |
| `INFO` | INFO | — |
| `N` | N | — |
| `OR` | OR | — |
| `P` | P | — |
| `POS` | POS | — |
| `SNP` | rsID | SNPID |
| `Z` | Z | — |
## Coverage

**8/9** tier groups satisfied.

| Tier | Status | Matched | Missing |
| --- | --- | --- | --- |
| Variant ID | yes | SNPID, rsID | — |
| Genomic location | yes | CHR, POS | — |
| Effect / other allele | yes | EA, NEA | — |
| Effect size | yes | BETA, OR, Z | HR |
| Uncertainty | no | — | SE |
| P-value | yes | P | MLOG10P |
| Sample size | yes | N | N_CASE |
| Allele frequency | yes | EAF | MAF, NEAF |
| Imputation / QC | yes | INFO | — |
## See also

- [Format summary](../format_summary.html)
- [All formats](index.md)