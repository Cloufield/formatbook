# plink1_assoc_outputs

Union of common association columns across .assoc, .assoc.fisher, .assoc.linear, .assoc.logistic, and .assoc.dosage; see per-extension specs in formats/plink_*.json.
## Overview

| Field | Value |
| --- | --- |
| Format key | `plink` |
| Spec file | `formats/plink.json` |
| Cite name | PLINK 1.9 |
| Version | PLINK 1.9 (doc revision 19 Aug 2025) |
| Last checked | 20260326 |
| Source | [https://www.cog-genomics.org/plink/1.9/formats](https://www.cog-genomics.org/plink/1.9/formats) |
| Citation | Purcell, S., Neale, B., Todd-Brown, K., Thomas, L., Ferreira, M. A., Bender, D., ... & Sham, P. C. (2007). PLINK: a tool set for whole-genome association and population-based linkage analyses. The American journal of human genetics, 81(3), 559-575. |
## File layout

| Field | Value |
| --- | --- |
| Separator | TAB |
| Header row | yes |
## Column mapping

| Raw header | Canonical | Canonical (secondary) |
| --- | --- | --- |
| `A1` | EA | — |
| `A2` | NEA | — |
| `BETA` | BETA | — |
| `BP` | POS | — |
| `CHISQ` | CHISQ | — |
| `CHR` | CHR | — |
| `F_A` | EAF_CASE | — |
| `F_U` | EAF_CONTROL | — |
| `FRQ` | EAF | — |
| `FRQ_A` | EAF_CASE | — |
| `FRQ_U` | EAF_CONTROL | — |
| `INFO` | INFO | — |
| `NMISS` | N | — |
| `OR` | OR | — |
| `P` | P | — |
| `SE` | SE | — |
| `SNP` | SNPID | rsID |
| `STAT` | T | — |
## Coverage

**9/9** tier groups satisfied.

| Tier | Status | Matched | Missing |
| --- | --- | --- | --- |
| Variant ID | yes | SNPID, rsID | — |
| Genomic location | yes | CHR, POS | — |
| Effect / other allele | yes | EA, NEA | — |
| Effect size | yes | BETA, OR | HR, Z |
| Uncertainty | yes | SE | — |
| P-value | yes | P | MLOG10P |
| Sample size | yes | N | N_CASE |
| Allele frequency | yes | EAF | MAF, NEAF |
| Imputation / QC | yes | INFO | — |
## See also

- [Format summary](../format_summary.html)
- [All formats](index.md)