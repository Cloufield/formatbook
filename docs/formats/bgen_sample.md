# .sample

Sample information file (.sample) accompanying .gen, .bgen genotype dosage files, or .haps phased reference panels. Loaded with --data/--sample, and produced by --export. The file is space-delimited with two header lines followed by one line per sample.
## Overview

| Field | Value |
| --- | --- |
| Format key | `bgen_sample` |
| Spec file | `formats/bgen_sample.json` |
| Cite name | Oxford/BGEN |
| Version | 20260208 |
| Last checked | 20260208 |
| Source | [https://www.well.ox.ac.uk/~gav/qctool_v2/documentation/sample_file_formats.html](https://www.well.ox.ac.uk/~gav/qctool_v2/documentation/sample_file_formats.html) |
| Source (2) | [https://www.cog-genomics.org/plink/2.0/formats#sample](https://www.cog-genomics.org/plink/2.0/formats#sample) |
| Citation | Band, G., & Marchini, J. (2018). BGEN: a binary file format for imputed genotype and haplotype data. bioRxiv. |
## File layout

| Field | Value |
| --- | --- |
| Separator | SPACE |
| NA value | NA |
| Header row | yes |
| Header lines | 2 |
| Second header line | Second header line specifies column types: '0' for ID/covariates, 'D' for discrete/categorical, 'B' for binary, 'P' for continuous phenotype |
| Column order | `ID_1`, `ID_2`, `missing`, `sex` |
## Column mapping

| Raw header | Canonical |
| --- | --- |
| `ID_1` | FID |
| `ID_2` | IID |
| `missing` | — |
| `sex` | SEX |
## Header descriptions

| Column | Description |
| --- | --- |
| `ID_1` | Family ID (header line 2 value: 0) |
| `ID_2` | Individual ID (header line 2 value: 0) |
| `missing` | Missing call frequency (header line 2 value: 0) |
| `sex` | Sex code ('1' = male, '2' = female, '0' = unknown; header line 2 value: D) |
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