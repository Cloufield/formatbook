# .glm.linear

Linear regression from --glm (quantitative phenotype). Header line starts with '#'. Column set can be reduced with cols=; optional NEG_LOG10_P and joint F_STAT appear with modifiers.
## Overview

| Field | Value |
| --- | --- |
| Format key | `plink2_linear` |
| Spec file | `formats/plink2_linear.json` |
| Cite name | PLINK 2.0 |
| Version | PLINK 2.0 (doc revision 11 Mar 2026) |
| Last checked | 20260326 |
| Source | [https://www.cog-genomics.org/plink/2.0/formats#glm_linear](https://www.cog-genomics.org/plink/2.0/formats#glm_linear) |
| Citation | Chang, C. C., Chow, C. C., Tellier, L. C., Vattikuti, S., Purcell, S. M., & Lee, J. J. (2015). Second-generation PLINK: rising to the challenge of larger and richer datasets. Gigascience, 4(1), s13742-015. |
## File layout

| Field | Value |
| --- | --- |
| Separator | TAB |
| NA value | . |
| Comment prefix | # |
| Header row | yes |
| Column order | `#CHROM`, `POS`, `ID`, `REF`, `ALT1`, `ALT`, `PROVISIONAL_REF?`, `A1`, `OMITTED`, `A1_CT`, `ALLELE_CT`, `A1_FREQ`, `MACH_R2`, `TEST`, `OBS_CT`, `BETA`, `SE`, `L95`, `U95`, `T_STAT`, `F_STAT`, `P`, `ERRCODE`, `LOG10_P` |
## Column mapping

| Raw header | Canonical | Canonical (secondary) |
| --- | --- | --- |
| `#CHROM` | CHR | — |
| `A1` | EA | — |
| `A1_CT` | — | — |
| `A1_FREQ` | EAF | — |
| `ALLELE_CT` | — | — |
| `ALT` | ALT | — |
| `ALT1` | — | — |
| `BETA` | BETA | — |
| `CHROM` | CHR | — |
| `ERRCODE` | — | — |
| `F_STAT` | F | — |
| `ID` | SNPID | rsID |
| `L95` | BETA_95L | — |
| `LOG10_P` | MLOG10P | — |
| `MACH_R2` | INFO | — |
| `OBS_CT` | N | — |
| `OMITTED` | — | — |
| `P` | P | — |
| `POS` | POS | — |
| `PROVISIONAL_REF?` | — | — |
| `REF` | REF | — |
| `SE` | SE | — |
| `T_STAT` | T | — |
| `TEST` | — | — |
| `U95` | BETA_95U | — |
## Header descriptions

| Column | Description |
| --- | --- |
| `#CHROM` | Chromosome code |
| `A1` | Counted allele in regression |
| `A1_CT` | Total A1 allele count |
| `A1_FREQ` | A1 allele frequency |
| `ALLELE_CT` | Allele observation count |
| `ALT` | All alternate alleles (comma-separated) |
| `ALT1` | First alternate allele |
| `BETA` | Regression coefficient for A1 |
| `ERRCODE` | Reason for NA result |
| `F_STAT` | F-statistic (joint tests) |
| `ID` | Variant ID |
| `L95` | Lower symmetric approx. CI for beta (--ci) |
| `LOG10_P` | Optional -log10(p) column |
| `MACH_R2` | MaCH imputation R-squared |
| `OBS_CT` | Samples in regression |
| `OMITTED` | Omitted allele |
| `P` | Asymptotic p-value |
| `POS` | Base-pair coordinate |
| `PROVISIONAL_REF?` | Whether REF is provisional |
| `REF` | Reference allele |
| `SE` | Standard error of beta |
| `T_STAT` | t-statistic (linear model) |
| `TEST` | Test identifier |
| `U95` | Upper symmetric approx. CI for beta (--ci) |
## Coverage

**8/9** tier groups satisfied.

| Tier | Status | Matched | Missing |
| --- | --- | --- | --- |
| Variant ID | yes | SNPID, rsID | — |
| Genomic location | yes | CHR, POS | — |
| Effect / other allele | partial | EA | NEA |
| Effect size | yes | BETA | OR, HR, Z |
| Uncertainty | yes | SE | — |
| P-value | yes | P, MLOG10P | — |
| Sample size | yes | N | N_CASE |
| Allele frequency | yes | EAF | MAF, NEAF |
| Imputation / QC | yes | INFO | — |
## See also

- [Format summary](../format_summary.html)
- [All formats](index.md)