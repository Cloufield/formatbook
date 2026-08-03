# metal

## Overview

| Field | Value |
| --- | --- |
| Format key | `metal` |
| Spec file | `formats/metal.json` |
| Cite name | METAL |
| Version | 20220726 |
| Source | [https://genome.sph.umich.edu/wiki/METAL_Documentation](https://genome.sph.umich.edu/wiki/METAL_Documentation) |
| Citation | Willer, C. J., Li, Y., & Abecasis, G. R. (2010). METAL: fast and efficient meta-analysis of genomewide association scans. Bioinformatics, 26(17), 2190-2191. |
## Column mapping

| Raw header | Canonical |
| --- | --- |
| `Allele1` | EA |
| `Allele2` | NEA |
| `Direction` | DIRECTION |
| `Effect` | BETA |
| `Freq1` | EAF |
| `MarkerName` | SNPID |
| `P-value` | P |
| `StdErr` | SE |
## Coverage

**6/9** tier groups satisfied.

| Tier | Status | Matched | Missing |
| --- | --- | --- | --- |
| Variant ID | yes | SNPID | rsID |
| Genomic location | no | — | CHR, POS |
| Effect / other allele | yes | EA, NEA | — |
| Effect size | yes | BETA | OR, HR, Z |
| Uncertainty | yes | SE | — |
| P-value | yes | P | MLOG10P |
| Sample size | no | — | N, N_CASE |
| Allele frequency | yes | EAF | MAF, NEAF |
| Imputation / QC | no | — | INFO |
## See also

- [Format summary](../format_summary.html)
- [All formats](index.md)