# .assoc.logistic

Multi-covariate logistic regression from --logistic. BETA column appears with '--logistic beta'; otherwise OR. With --ci 0.xy, SE, L_xy, U_xy are inserted before STAT (SE is on log-odds scale).
## Overview

| Field | Value |
| --- | --- |
| Format key | `plink_logistic` |
| Spec file | `formats/plink_logistic.json` |
| Cite name | PLINK 1.9 |
| Version | PLINK 1.9 (doc revision 19 Aug 2025) |
| Last checked | 20260326 |
| Source | [https://www.cog-genomics.org/plink/1.9/formats#assoc_linear](https://www.cog-genomics.org/plink/1.9/formats#assoc_linear) |
| Citation | Purcell, S., Neale, B., Todd-Brown, K., Thomas, L., Ferreira, M. A., Bender, D., ... & Sham, P. C. (2007). PLINK: a tool set for whole-genome association and population-based linkage analyses. The American journal of human genetics, 81(3), 559-575. |
## File layout

| Field | Value |
| --- | --- |
| Separator | TAB |
| Header row | yes |
| Column order | `CHR`, `SNP`, `BP`, `A1`, `TEST`, `NMISS`, `OR`, `BETA`, `SE`, `L95`, `U95`, `STAT`, `P` |
## Column mapping

| Raw header | Canonical | Canonical (secondary) |
| --- | --- | --- |
| `A1` | EA | — |
| `A2` | NEA | — |
| `BETA` | BETA | — |
| `BP` | POS | — |
| `CHISQ` | CHISQ | — |
| `CHR` | CHR | — |
| `L95` | OR_95L | — |
| `NMISS` | N | — |
| `OR` | OR | — |
| `P` | P | — |
| `SE` | SE | — |
| `SNP` | SNPID | rsID |
| `STAT` | T | — |
| `TEST` | — | — |
| `U95` | OR_95U | — |
## Header descriptions

| Column | Description |
| --- | --- |
| `A1` | Allele 1 (omitted with 'no-snp') |
| `A2` | Allele 2 (when present) |
| `BETA` | Log-odds coefficient ('--logistic beta') |
| `BP` | Base-pair coordinate (omitted with 'no-snp') |
| `CHISQ` | Chi-square (when reported for some tests) |
| `CHR` | Chromosome code (omitted with 'no-snp') |
| `L95` | Lower end of symmetric approx. CI for OR (--ci) |
| `NMISS` | Observations with nonmissing genotype, phenotype, and covariates |
| `OR` | Odds ratio (without '--logistic beta') |
| `P` | Asymptotic p-value for t-statistic |
| `SE` | Standard error of beta / log-odds (--ci) |
| `SNP` | Variant identifier (omitted with 'no-snp') |
| `STAT` | t-statistic |
| `TEST` | Test identifier |
| `U95` | Upper end of symmetric approx. CI for OR (--ci) |
## Coverage

**7/9** tier groups satisfied.

| Tier | Status | Matched | Missing |
| --- | --- | --- | --- |
| Variant ID | yes | SNPID, rsID | — |
| Genomic location | yes | CHR, POS | — |
| Effect / other allele | yes | EA, NEA | — |
| Effect size | yes | BETA, OR | HR, Z |
| Uncertainty | yes | SE | — |
| P-value | yes | P | MLOG10P |
| Sample size | yes | N | N_CASE |
| Allele frequency | no | — | EAF, MAF, NEAF |
| Imputation / QC | no | — | INFO |
## See also

- [Format summary](../format_summary.html)
- [All formats](index.md)