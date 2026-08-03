# genomicSEM

## Overview

| Field | Value |
| --- | --- |
| Format key | `genomicsem` |
| Spec file | `formats/genomicsem.json` |
| Cite name | genomicSEM |
| Version | 20241210 |
| Source | [https://github.com/GenomicSEM/GenomicSEM/wiki/4.-Common-Factor-GWAS](https://github.com/GenomicSEM/GenomicSEM/wiki/4.-Common-Factor-GWAS) |
| Source (2) | [https://github.com/GenomicSEM/GenomicSEM/wiki/5.-Multivariate-GWAS](https://github.com/GenomicSEM/GenomicSEM/wiki/5.-Multivariate-GWAS) |
| GitHub | [https://github.com/GenomicSEM/GenomicSEM](https://github.com/GenomicSEM/GenomicSEM) |
| Citation | Grotzinger, A. D., Rhemtulla, M., de Vlaming, R., Ritchie, S. J., Mallard, T. T., Hill, W. D., ... & Tucker-Drob, E. M. (2019). Genomic structural equation modelling provides insights into the multivariate genetic architecture of complex traits. Nature communications, 10(1), 3402. |
## Column mapping

| Raw header | Canonical | Canonical (secondary) |
| --- | --- | --- |
| `A1` | EA | — |
| `A2` | NEA | — |
| `BP` | POS | — |
| `CHR` | CHR | — |
| `est` | BETA | — |
| `Frq` | EAF | — |
| `MAF` | MAF | — |
| `N` | N | — |
| `Pval_Estimate` | P | — |
| `Q` | Q | — |
| `Q_df` | DOF | — |
| `Q_pval` | P_HET | — |
| `se_c` | SE | — |
| `SNP` | SNPID | rsID |
| `Z_Estimate` | Z | — |
## Coverage

**8/9** tier groups satisfied.

| Tier | Status | Matched | Missing |
| --- | --- | --- | --- |
| Variant ID | yes | SNPID, rsID | — |
| Genomic location | yes | CHR, POS | — |
| Effect / other allele | yes | EA, NEA | — |
| Effect size | yes | BETA, Z | OR, HR |
| Uncertainty | yes | SE | — |
| P-value | yes | P | MLOG10P |
| Sample size | yes | N | N_CASE |
| Allele frequency | yes | EAF, MAF | NEAF |
| Imputation / QC | no | — | INFO |
## See also

- [Format summary](../format_summary.html)
- [All formats](index.md)