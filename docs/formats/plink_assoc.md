# .assoc

Case/control basic allelic test from --assoc (not --linear/--logistic). Default columns; 'counts' replaces F_A/F_U with C_A/C_U; --ci 0.xy appends SE, L_xy, U_xy after OR.
## Overview

| Field | Value |
| --- | --- |
| Format key | `plink_assoc` |
| Spec file | `formats/plink_assoc.json` |
| Cite name | PLINK 1.9 |
| Version | PLINK 1.9 (doc revision 19 Aug 2025) |
| Last checked | 20260326 |
| Source | [https://www.cog-genomics.org/plink/1.9/formats#assoc](https://www.cog-genomics.org/plink/1.9/formats#assoc) |
| Citation | Purcell, S., Neale, B., Todd-Brown, K., Thomas, L., Ferreira, M. A., Bender, D., ... & Sham, P. C. (2007). PLINK: a tool set for whole-genome association and population-based linkage analyses. The American journal of human genetics, 81(3), 559-575. |
## File layout

| Field | Value |
| --- | --- |
| Separator | TAB |
| Header row | yes |
| Column order | `CHR`, `SNP`, `BP`, `A1`, `F_A`, `F_U`, `A2`, `CHISQ`, `P`, `OR`, `SE`, `L95`, `U95` |
## Column mapping

| Raw header | Canonical | Canonical (secondary) |
| --- | --- | --- |
| `A1` | EA | — |
| `A2` | NEA | — |
| `BP` | POS | — |
| `C_A` | — | — |
| `C_U` | — | — |
| `CHISQ` | CHISQ | — |
| `CHR` | CHR | — |
| `F_A` | EAF_CASE | — |
| `F_U` | EAF_CONTROL | — |
| `L95` | OR_95L | — |
| `OR` | OR | — |
| `P` | P | — |
| `SE` | SE | — |
| `SNP` | SNPID | rsID |
| `U95` | OR_95U | — |
## Header descriptions

| Column | Description |
| --- | --- |
| `A1` | Allele 1 (usually minor) |
| `A2` | Allele 2 (usually major) |
| `BP` | Base-pair coordinate (1-based) |
| `C_A` | Allele 1 count among cases ('counts' modifier) |
| `C_U` | Allele 1 count among controls ('counts' modifier) |
| `CHISQ` | Allelic test chi-square (omitted with fisher / fisher-midp) |
| `CHR` | Chromosome code |
| `F_A` | Allele 1 frequency among cases |
| `F_U` | Allele 1 frequency among controls |
| `L95` | Lower end of symmetric approx. CI for OR (--ci) |
| `OR` | odds(A1\|case) / odds(A1\|control) |
| `P` | Allelic test p-value |
| `SE` | Standard error of odds ratio estimate (--ci) |
| `SNP` | Variant identifier |
| `U95` | Upper end of symmetric approx. CI for OR (--ci) |
## Coverage

**6/9** tier groups satisfied.

| Tier | Status | Matched | Missing |
| --- | --- | --- | --- |
| Variant ID | yes | SNPID, rsID | — |
| Genomic location | yes | CHR, POS | — |
| Effect / other allele | yes | EA, NEA | — |
| Effect size | yes | OR | BETA, HR, Z |
| Uncertainty | yes | SE | — |
| P-value | yes | P | MLOG10P |
| Sample size | no | — | N, N_CASE |
| Allele frequency | no | — | EAF, MAF, NEAF |
| Imputation / QC | no | — | INFO |
## See also

- [Format summary](../format_summary.html)
- [All formats](index.md)