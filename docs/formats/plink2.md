# plink2_glm_outputs

Union of columns across .glm.linear, .glm.logistic, and .glm.firth; full column sets are in formats/plink2_*.json.
## Overview

| Field | Value |
| --- | --- |
| Format key | `plink2` |
| Spec file | `formats/plink2.json` |
| Cite name | PLINK 2.0 |
| Version | PLINK 2.0 (doc revision 11 Mar 2026) |
| Last checked | 20260326 |
| Source | [https://www.cog-genomics.org/plink/2.0/formats](https://www.cog-genomics.org/plink/2.0/formats) |
| Citation | Chang, C. C., Chow, C. C., Tellier, L. C., Vattikuti, S., Purcell, S. M., & Lee, J. J. (2015). Second-generation PLINK: rising to the challenge of larger and richer datasets. Gigascience, 4(1), s13742-015. |
## File layout

| Field | Value |
| --- | --- |
| Separator | TAB |
| NA value | . |
| Comment prefix | # |
| Header row | yes |
## Column mapping

| Raw header | Canonical | Canonical (secondary) |
| --- | --- | --- |
| `#CHROM` | CHR | — |
| `A1` | EA | — |
| `A1_CASE_FREQ` | EAF_CASE | — |
| `A1_CTRL_FREQ` | EAF_CONTROL | — |
| `A1_FREQ` | EAF | — |
| `ALT` | ALT | — |
| `BETA` | BETA | — |
| `CHROM` | CHR | — |
| `F_STAT` | F | — |
| `ID` | SNPID | rsID |
| `L95` | OR_95L | — |
| `LOG(OR)_SE` | SE | — |
| `LOG10_P` | MLOG10P | — |
| `MACH_R2` | INFO | — |
| `OBS_CT` | N | — |
| `OR` | OR | — |
| `P` | P | — |
| `POS` | POS | — |
| `REF` | REF | — |
| `SE` | SE | — |
| `T_STAT` | T | — |
| `U95` | OR_95U | — |
| `Z_STAT` | Z | — |
## Coverage

**8/9** tier groups satisfied.

| Tier | Status | Matched | Missing |
| --- | --- | --- | --- |
| Variant ID | yes | SNPID, rsID | — |
| Genomic location | yes | CHR, POS | — |
| Effect / other allele | partial | EA | NEA |
| Effect size | yes | BETA, OR, Z | HR |
| Uncertainty | yes | SE | — |
| P-value | yes | P, MLOG10P | — |
| Sample size | yes | N | N_CASE |
| Allele frequency | yes | EAF | MAF, NEAF |
| Imputation / QC | yes | INFO | — |
## See also

- [Format summary](../format_summary.html)
- [All formats](index.md)