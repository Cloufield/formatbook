# gwaslab

## Overview

| Field | Value |
| --- | --- |
| Format key | `gwaslab` |
| Spec file | `formats/gwaslab.json` |
| Cite name | GWASLab |
| Version | v4.0.5 |
| Last checked | 20260109 |
| Source | [https://cloufield.github.io/gwaslab/](https://cloufield.github.io/gwaslab/) |
| GitHub | [https://github.com/Cloufield/gwaslab](https://github.com/Cloufield/gwaslab) |
| Citation | Cloufield. GWASLab: a Python package for GWAS summary statistics. https://github.com/Cloufield/gwaslab |
## File layout

| Field | Value |
| --- | --- |
| Separator | TAB |
| Header row | yes |
## Column mapping

| Raw header | Canonical |
| --- | --- |
| `ALT` | ALT |
| `BETA` | BETA |
| `CHISQ` | CHISQ |
| `CHR` | CHR |
| `DIRECTION` | DIRECTION |
| `DOF` | DOF |
| `EA` | EA |
| `EAF` | EAF |
| `F` | F |
| `HR` | HR |
| `HR_95L` | HR_95L |
| `HR_95U` | HR_95U |
| `I2` | I2 |
| `INFO` | INFO |
| `MAF` | MAF |
| `MLOG10P` | MLOG10P |
| `N` | N |
| `N_CASE` | N_CASE |
| `N_CONTROL` | N_CONTROL |
| `NEA` | NEA |
| `OR` | OR |
| `OR_95L` | OR_95L |
| `OR_95U` | OR_95U |
| `P` | P |
| `P_HET` | P_HET |
| `POS` | POS |
| `REF` | REF |
| `rsID` | rsID |
| `SE` | SE |
| `SNPID` | SNPID |
| `SNPR2` | SNPR2 |
| `STATUS` | STATUS |
| `T` | T |
| `Z` | Z |
## Coverage

**9/9** tier groups satisfied.

| Tier | Status | Matched | Missing |
| --- | --- | --- | --- |
| Variant ID | yes | SNPID, rsID | — |
| Genomic location | yes | CHR, POS | — |
| Effect / other allele | yes | EA, NEA | — |
| Effect size | yes | BETA, OR, HR, Z | — |
| Uncertainty | yes | SE | — |
| P-value | yes | P, MLOG10P | — |
| Sample size | yes | N, N_CASE | — |
| Allele frequency | yes | EAF, MAF | NEAF |
| Imputation / QC | yes | INFO | — |
## See also

- [Format summary](../format_summary.html)
- [All formats](index.md)