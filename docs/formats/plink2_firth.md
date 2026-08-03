# .glm.firth

Same column layout as .glm.logistic when Firth logistic regression is used (extension .glm.firth or .glm.logistic.hybrid).
## Overview

| Field | Value |
| --- | --- |
| Format key | `plink2_firth` |
| Spec file | `formats/plink2_firth.json` |
| Cite name | PLINK 2.0 |
| Version | PLINK 2.0 (doc revision 11 Mar 2026) |
| Last checked | 20260326 |
| Source | [https://www.cog-genomics.org/plink/2.0/formats#glm_logistic](https://www.cog-genomics.org/plink/2.0/formats#glm_logistic) |
| Citation | Chang, C. C., Chow, C. C., Tellier, L. C., Vattikuti, S., Purcell, S. M., & Lee, J. J. (2015). Second-generation PLINK: rising to the challenge of larger and richer datasets. Gigascience, 4(1), s13742-015. |
## File layout

| Field | Value |
| --- | --- |
| Separator | TAB |
| NA value | . |
| Comment prefix | # |
| Header row | yes |
| Column order | `#CHROM`, `POS`, `ID`, `REF`, `ALT1`, `ALT`, `PROVISIONAL_REF?`, `A1`, `OMITTED`, `A1_CT`, `ALLELE_CT`, `A1_CASE_CT`, `A1_CTRL_CT`, `CASE_ALLELE_CT`, `CTRL_ALLELE_CT`, `CASE_NON_A1_CT`, `CASE_HET_A1_CT`, `CASE_HOM_A1_CT`, `CTRL_NON_A1_CT`, `CTRL_HET_A1_CT`, `CTRL_HOM_A1_CT`, `A1_FREQ`, `A1_CASE_FREQ`, `A1_CTRL_FREQ`, `MACH_R2`, `FIRTH?`, `TEST`, `OBS_CT`, `BETA`, `OR`, `LOG(OR)_SE`, `L95`, `U95`, `Z_STAT`, `F_STAT`, `P`, `ERRCODE`, `LOG10_P` |
## Column mapping

| Raw header | Canonical | Canonical (secondary) |
| --- | --- | --- |
| `#CHROM` | CHR | — |
| `A1` | EA | — |
| `A1_CASE_CT` | — | — |
| `A1_CASE_FREQ` | EAF_CASE | — |
| `A1_CT` | — | — |
| `A1_CTRL_CT` | — | — |
| `A1_CTRL_FREQ` | EAF_CONTROL | — |
| `A1_FREQ` | EAF | — |
| `ALLELE_CT` | — | — |
| `ALT` | ALT | — |
| `ALT1` | — | — |
| `BETA` | BETA | — |
| `CASE_ALLELE_CT` | — | — |
| `CASE_HET_A1_CT` | — | — |
| `CASE_HOM_A1_CT` | — | — |
| `CASE_NON_A1_CT` | — | — |
| `CHROM` | CHR | — |
| `CTRL_ALLELE_CT` | — | — |
| `CTRL_HET_A1_CT` | — | — |
| `CTRL_HOM_A1_CT` | — | — |
| `CTRL_NON_A1_CT` | — | — |
| `ERRCODE` | — | — |
| `F_STAT` | F | — |
| `FIRTH?` | — | — |
| `ID` | SNPID | rsID |
| `L95` | OR_95L | — |
| `LOG(OR)_SE` | SE | — |
| `LOG10_P` | MLOG10P | — |
| `MACH_R2` | INFO | — |
| `OBS_CT` | N | — |
| `OMITTED` | — | — |
| `OR` | OR | — |
| `P` | P | — |
| `POS` | POS | — |
| `PROVISIONAL_REF?` | — | — |
| `REF` | REF | — |
| `SE` | SE | — |
| `TEST` | — | — |
| `U95` | OR_95U | — |
| `Z_STAT` | Z | — |
## Header descriptions

| Column | Description |
| --- | --- |
| `#CHROM` | Chromosome code |
| `A1` | Counted allele in regression |
| `A1_FREQ` | A1 allele frequency |
| `ALT` | All alternate alleles (comma-separated) |
| `BETA` | Log-odds coefficient for A1 |
| `ERRCODE` | Reason for NA result |
| `FIRTH?` | Whether Firth regression was used ('firth-fallback' only) |
| `ID` | Variant ID |
| `LOG(OR)_SE` | Standard error of log-odds (beta) |
| `OBS_CT` | Samples in regression |
| `OR` | Odds ratio for A1 |
| `P` | Asymptotic p-value |
| `POS` | Base-pair coordinate |
| `REF` | Reference allele |
| `TEST` | Test identifier |
| `Z_STAT` | Wald Z-score |
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