# .pvar

Variant table for .pgen; VCF-style headers allowed. Last header line starts with '#CHROM'. Without headers, columns follow .bim order (CHROM, ID, CM, POS, ALT, REF or 5-column without CM).
## Overview

| Field | Value |
| --- | --- |
| Format key | `plink_pvar` |
| Spec file | `formats/plink_pvar.json` |
| Cite name | PLINK 2.0 |
| Version | PLINK 2.0 (doc revision 11 Mar 2026) |
| Last checked | 20260326 |
| Source | [https://www.cog-genomics.org/plink/2.0/formats#pvar](https://www.cog-genomics.org/plink/2.0/formats#pvar) |
| Citation | Chang, C. C., Chow, C. C., Tellier, L. C., Vattikuti, S., Purcell, S. M., & Lee, J. J. (2015). Second-generation PLINK: rising to the challenge of larger and richer datasets. Gigascience, 4(1), s13742-015. |
## File layout

| Field | Value |
| --- | --- |
| Separator | TAB |
| NA value | . |
| Comment prefix | # |
| Header row | yes |
| Column order | `#CHROM`, `POS`, `ID`, `REF`, `ALT`, `QUAL`, `FILTER`, `INFO`, `FORMAT`, `CM` |
## Column mapping

| Raw header | Canonical | Canonical (secondary) |
| --- | --- | --- |
| `#CHROM` | CHR | — |
| `ALT` | ALT | — |
| `CHROM` | CHR | — |
| `CM` | CM | — |
| `FILTER` | FILTER | — |
| `FORMAT` | FORMAT | — |
| `ID` | SNPID | rsID |
| `INFO` | INFO | — |
| `POS` | POS | — |
| `QUAL` | QUAL | — |
| `REF` | REF | — |
## Header descriptions

| Column | Description |
| --- | --- |
| `#CHROM` | Chromosome code |
| `ALT` | Alternate alleles (comma-separated) |
| `CM` | Centimorgan position (optional) |
| `FILTER` | FILTER field |
| `FORMAT` | FORMAT column when present |
| `ID` | Variant ID |
| `INFO` | INFO field |
| `POS` | Base-pair coordinate |
| `QUAL` | Phred-scaled locus quality |
| `REF` | Reference allele |
## Coverage

**3/9** tier groups satisfied.

| Tier | Status | Matched | Missing |
| --- | --- | --- | --- |
| Variant ID | yes | SNPID, rsID | — |
| Genomic location | yes | CHR, POS | — |
| Effect / other allele | no | — | EA, NEA |
| Effect size | no | — | BETA, OR, HR, Z |
| Uncertainty | no | — | SE |
| P-value | no | — | P, MLOG10P |
| Sample size | no | — | N, N_CASE |
| Allele frequency | no | — | EAF, MAF, NEAF |
| Imputation / QC | yes | INFO | — |
## See also

- [Format summary](../format_summary.html)
- [All formats](index.md)