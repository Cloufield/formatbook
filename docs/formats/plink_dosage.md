# .assoc.dosage

Dosage association from --dosage. CHR/BP require --map. 'case-control-freqs' replaces FRQ with FRQ_A and FRQ_U.
## Overview

| Field | Value |
| --- | --- |
| Format key | `plink_dosage` |
| Spec file | `formats/plink_dosage.json` |
| Cite name | PLINK 1.9 |
| Version | PLINK 1.9 (doc revision 19 Aug 2025) |
| Last checked | 20260326 |
| Source | [https://www.cog-genomics.org/plink/1.9/formats#assoc_dosage](https://www.cog-genomics.org/plink/1.9/formats#assoc_dosage) |
| Citation | Purcell, S., Neale, B., Todd-Brown, K., Thomas, L., Ferreira, M. A., Bender, D., ... & Sham, P. C. (2007). PLINK: a tool set for whole-genome association and population-based linkage analyses. The American journal of human genetics, 81(3), 559-575. |
## File layout

| Field | Value |
| --- | --- |
| Separator | TAB |
| Header row | yes |
| Column order | `CHR`, `SNP`, `BP`, `A1`, `A2`, `FRQ`, `FRQ_A`, `FRQ_U`, `INFO`, `BETA`, `OR`, `SE`, `P` |
## Column mapping

| Raw header | Canonical | Canonical (secondary) |
| --- | --- | --- |
| `A1` | EA | — |
| `A2` | NEA | — |
| `BETA` | BETA | — |
| `BP` | POS | — |
| `CHR` | CHR | — |
| `FRQ` | EAF | — |
| `FRQ_A` | EAF_CASE | — |
| `FRQ_U` | EAF_CONTROL | — |
| `INFO` | INFO | — |
| `OR` | OR | — |
| `P` | P | — |
| `SE` | SE | — |
| `SNP` | SNPID | rsID |
## Header descriptions

| Column | Description |
| --- | --- |
| `A1` | Allele 1 (usually minor) |
| `A2` | Allele 2 (usually major) |
| `BETA` | Regression coefficient (quantitative trait) |
| `BP` | Base-pair coordinate |
| `CHR` | Chromosome code |
| `FRQ` | Allele 1 frequency (overall) |
| `FRQ_A` | Allele 1 frequency in cases ('case-control-freqs') |
| `FRQ_U` | Allele 1 frequency in controls ('case-control-freqs') |
| `INFO` | R-squared quality / information content |
| `OR` | Odds ratio (case/control) |
| `P` | Association p-value |
| `SE` | Standard error of effect (not OR SE) |
| `SNP` | Variant identifier |
## Coverage

**8/9** tier groups satisfied.

| Tier | Status | Matched | Missing |
| --- | --- | --- | --- |
| Variant ID | yes | SNPID, rsID | — |
| Genomic location | yes | CHR, POS | — |
| Effect / other allele | yes | EA, NEA | — |
| Effect size | yes | BETA, OR | HR, Z |
| Uncertainty | yes | SE | — |
| P-value | yes | P | MLOG10P |
| Sample size | no | — | N, N_CASE |
| Allele frequency | yes | EAF | MAF, NEAF |
| Imputation / QC | yes | INFO | — |
## See also

- [Format summary](../format_summary.html)
- [All formats](index.md)