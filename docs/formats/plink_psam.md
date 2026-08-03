# .psam

Sample table for .pgen. Last header line starts with '#FID' or '#IID'; FID may be omitted (then assumed '0'). Columns after SEX are phenotype/covariate names.
## Overview

| Field | Value |
| --- | --- |
| Format key | `plink_psam` |
| Spec file | `formats/plink_psam.json` |
| Cite name | PLINK 2.0 |
| Version | PLINK 2.0 (doc revision 11 Mar 2026) |
| Last checked | 20260326 |
| Source | [https://www.cog-genomics.org/plink/2.0/formats#psam](https://www.cog-genomics.org/plink/2.0/formats#psam) |
| Citation | Chang, C. C., Chow, C. C., Tellier, L. C., Vattikuti, S., Purcell, S. M., & Lee, J. J. (2015). Second-generation PLINK: rising to the challenge of larger and richer datasets. Gigascience, 4(1), s13742-015. |
## File layout

| Field | Value |
| --- | --- |
| Separator | TAB |
| NA value | NA |
| Comment prefix | # |
| Header row | yes |
| Column order | `#FID`, `IID`, `#IID`, `SID`, `PAT`, `MAT`, `SEX` |
## Column mapping

| Raw header | Canonical |
| --- | --- |
| `#FID` | FID |
| `#IID` | IID |
| `FID` | FID |
| `IID` | IID |
| `MAT` | MAT |
| `PAT` | PAT |
| `SEX` | SEX |
| `SID` | SID |
## Header descriptions

| Column | Description |
| --- | --- |
| `#FID` | Family ID (optional first column) |
| `#IID` | Individual ID (required) |
| `IID` | Individual ID |
| `MAT` | Maternal IID ('0' if unknown) |
| `PAT` | Paternal IID ('0' if unknown) |
| `SEX` | Sex (1=male, 2=female, NA/0=unknown) |
| `SID` | Source ID |
## Coverage

**0/9** tier groups satisfied.

| Tier | Status | Matched | Missing |
| --- | --- | --- | --- |
| Variant ID | no | — | SNPID, rsID |
| Genomic location | no | — | CHR, POS |
| Effect / other allele | no | — | EA, NEA |
| Effect size | no | — | BETA, OR, HR, Z |
| Uncertainty | no | — | SE |
| P-value | no | — | P, MLOG10P |
| Sample size | no | — | N, N_CASE |
| Allele frequency | no | — | EAF, MAF, NEAF |
| Imputation / QC | no | — | INFO |
## See also

- [Format summary](../format_summary.html)
- [All formats](index.md)