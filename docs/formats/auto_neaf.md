# auto_neaf

## Overview

| Field | Value |
| --- | --- |
| Format key | `auto_neaf` |
| Spec file | `formats/auto_neaf.json` |
| Version | 20250827 |
## File layout

| Field | Value |
| --- | --- |
| Separator | TAB |
| NA value | #NA |
## Column mapping

| Raw header | Canonical |
| --- | --- |
| `#CHROM` | CHR |
| `A0` | NEA |
| `a0` | NEA |
| `A1` | EA |
| `a1` | EA |
| `A1_CASE_FREQ` | EAF_CASE |
| `A1_CTRL_FREQ` | EAF_CONTROL |
| `A1_FREQ` | EAF |
| `A1FREQ` | EAF |
| `A2` | NEA |
| `a2` | NEA |
| `AF` | EAF |
| `AF1` | EAF |
| `ALLELE0` | NEA |
| `Allele0` | NEA |
| `allele0` | NEA |
| `ALLELE1` | EA |
| `Allele1` | EA |
| `allele1` | EA |
| `ALLELE2` | NEA |
| `Allele2` | NEA |
| `allele2` | NEA |
| `ALLELE_0` | NEA |
| `Allele_0` | NEA |
| `allele_0` | NEA |
| `ALLELE_1` | EA |
| `Allele_1` | EA |
| `allele_1` | EA |
| `ALLELE_2` | NEA |
| `Allele_2` | NEA |
| `allele_2` | NEA |
| `allelefrequency_effect` | EAF |
| `ALT` | EA |
| `Alt` | EA |
| `alternative` | EA |
| `alternative_allele` | EA |
| `B` | BETA |
| `b` | BETA |
| `base_pair_location` | POS |
| `beta` | BETA |
| `BETA` | BETA |
| `Beta` | BETA |
| `BETA_95L` | BETA_95L |
| `BETA_95U` | BETA_95U |
| `betase` | SE |
| `BP` | POS |
| `bp` | POS |
| `bpos` | POS |
| `chisq` | CHISQ |
| `chisq_association` | CHISQ |
| `CHISQ_BOLT_LMM` | CHISQ |
| `CHR` | CHR |
| `chr` | CHR |
| `Chr` | CHR |
| `CHROM` | CHR |
| `Chrom` | CHR |
| `chrom` | CHR |
| `chromosome` | CHR |
| `Chromosome` | CHR |
| `CHROMOSOME` | CHR |
| `ci_lower` | OR_95L |
| `ci_upper` | OR_95U |
| `Direction` | DIRECTION |
| `DIRECTION` | DIRECTION |
| `EA` | EA |
| `ea` | EA |
| `eaf` | EAF |
| `EAF` | EAF |
| `Effect` | BETA |
| `effect_allele` | EA |
| `effect_allele_frequency` | EAF |
| `effect_weight` | BETA |
| `est` | BETA |
| `F` | F |
| `F_STAT` | F |
| `FREQ` | NEAF |
| `Freq` | NEAF |
| `freq` | NEAF |
| `Freq1` | EAF |
| `Frequency` | NEAF |
| `FRQ` | NEAF |
| `Frq` | NEAF |
| `frq` | NEAF |
| `GENPOS` | POS |
| `hazard_ratio` | HR |
| `hm_rsID` | rsID |
| `HR_95L` | HR_95L |
| `HR_95U` | HR_95U |
| `I2` | I2 |
| `imputationInfo` | INFO |
| `info` | INFO |
| `INFO` | INFO |
| `L95` | BETA_95L |
| `LOG10_P` | MLOG10P |
| `LOG10P` | MLOG10P |
| `MAC` | MA_COUNT |
| `mac` | MA_COUNT |
| `MACH_R2` | INFO |
| `maf` | MAF |
| `Maf` | MAF |
| `MAF` | MAF |
| `MAF_CASE` | MAF_CASE |
| `maf_case` | MAF_CASE |
| `MAF_CONTROL` | MAF_CONTROL |
| `maf_control` | MAF_CONTROL |
| `MARKER` | SNPID |
| `marker` | SNPID |
| `MARKERNAME` | SNPID |
| `markername` | SNPID |
| `MLOG10P` | MLOG10P |
| `n` | N |
| `N` | N |
| `N_CASE` | N_CASE |
| `n_case` | N_CASE |
| `N_control` | N_CONTROL |
| `N_Control` | N_CONTROL |
| `N_EFF` | N_EFF |
| `Ncase` | N_CASE |
| `ncase` | N_CASE |
| `Ncontrol` | N_CONTROL |
| `NCONTROL` | N_CONTROL |
| `NEA` | NEA |
| `nea` | NEA |
| `Neff` | N_EFF |
| `neg_log_10_p_value` | MLOG10P |
| `non_effect_allele` | NEA |
| `NON_EFFECT_ALLELE` | NEA |
| `Nsample` | N |
| `num_samples` | N |
| `OBS_CT` | N |
| `odds_ratio` | OR |
| `OR` | OR |
| `OR_95L` | OR_95L |
| `OR_95U` | OR_95U |
| `other_allele` | NEA |
| `p` | P |
| `P` | P |
| `P.value` | P |
| `p.value` | P |
| `P_BOLT_LMM` | P |
| `p_value` | P |
| `P_VALUE` | P |
| `POS` | POS |
| `Pos` | POS |
| `pos` | POS |
| `PVAL` | P |
| `Pval` | P |
| `Pval_Estimate` | P |
| `Pvalue` | P |
| `Q` | Q |
| `Q.pval` | P_HET |
| `Q_df` | DOF |
| `Q_pval` | P_HET |
| `R2` | INFO |
| `r2` | INFO |
| `REF` | NEA |
| `Ref` | NEA |
| `ref_allele` | REF |
| `reference` | NEA |
| `reference_allele` | NEA |
| `RSID` | rsID |
| `rsid` | rsID |
| `rsID` | SNPID |
| `Rsq` | INFO |
| `sample_size` | N |
| `se` | SE |
| `SE` | SE |
| `se_c` | SE |
| `sebeta` | SE |
| `SNP` | SNPID |
| `snp` | SNPID |
| `SNPID` | SNPID |
| `snpid` | SNPID |
| `standard_error` | SE |
| `STATUS` | STATUS |
| `StdErr` | SE |
| `T` | T |
| `T_STAT` | T |
| `TEST` | TEST |
| `TotalSampleSize` | N |
| `TRAIT` | TRAIT |
| `U95` | BETA_95U |
| `variant_id` | SNPID |
| `Z` | Z |
| `z` | Z |
| `Z_Estimate` | Z |
## Assumptions

Note: auto_neaf assumes A1=EA; Alt=EA; Frq=NEAF — same as `auto_1_alt_neaf`
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
| Allele frequency | yes | EAF, MAF, NEAF | — |
| Imputation / QC | yes | INFO | — |
## See also

- [Format summary](../format_summary.html)
- [All formats](index.md)