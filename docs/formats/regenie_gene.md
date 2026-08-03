# regenie_gene

## Overview

| Field | Value |
| --- | --- |
| Format key | `regenie_gene` |
| Spec file | `formats/regenie_gene.json` |
| Cite name | REGENIE |
| Version | 20230926 |
| Last checked | 20230926 |
| Source | [https://rgcgithub.github.io/regenie/](https://rgcgithub.github.io/regenie/) |
| Source (2) | [https://github.com/rgcgithub/regenie/blob/master/example/test_bin_out_firth_Y1.regenie](https://github.com/rgcgithub/regenie/blob/master/example/test_bin_out_firth_Y1.regenie) |
| GitHub | [https://github.com/rgcgithub/regenie](https://github.com/rgcgithub/regenie) |
| Citation | Mbatchou, J., Barnard, L., Backman, J., Marcketta, A., Kosmicki, J. A., Ziyatdinov, A., ... & Marchini, J. (2021). Computationally efficient whole-genome regression for quantitative and binary traits. Nature genetics, 53(7), 1097-1103. |
## File layout

| Field | Value |
| --- | --- |
| Separator | SPACE |
| NA value | NA |
| Comment prefix | # |
| Column order | `CHROM`, `GENPOS`, `ID`, `ALLELE0`, `ALLELE1`, `A1FREQ`, `N`, `TEST`, `BETA`, `SE`, `CHISQ`, `LOG10P` |
## Column mapping

| Raw header | Canonical |
| --- | --- |
| `A1FREQ` | EAF |
| `ALLELE0` | NEA |
| `ALLELE1` | EA |
| `BETA` | BETA |
| `CHISQ` | CHISQ |
| `CHROM` | CHR |
| `EXTRA` | DOF |
| `GENPOS` | POS |
| `ID` | SNPID |
| `LOG10P` | MLOG10P |
| `N` | N |
| `SE` | SE |
| `TEST` | TEST |
## Coverage

**8/9** tier groups satisfied.

| Tier | Status | Matched | Missing |
| --- | --- | --- | --- |
| Variant ID | yes | SNPID | rsID |
| Genomic location | yes | CHR, POS | — |
| Effect / other allele | yes | EA, NEA | — |
| Effect size | yes | BETA | OR, HR, Z |
| Uncertainty | yes | SE | — |
| P-value | yes | MLOG10P | P |
| Sample size | yes | N | N_CASE |
| Allele frequency | yes | EAF | MAF, NEAF |
| Imputation / QC | no | — | INFO |
## See also

- [Format summary](../format_summary.html)
- [All formats](index.md)