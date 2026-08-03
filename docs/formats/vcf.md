# vcf

## Overview

| Field | Value |
| --- | --- |
| Format key | `vcf` |
| Spec file | `formats/vcf.json` |
| Cite name | GWAS-VCF |
| Version | 20220923 |
| Source | [https://github.com/MRCIEU/gwas-vcf-specification/tree/1.0.0](https://github.com/MRCIEU/gwas-vcf-specification/tree/1.0.0) |
| GitHub | [https://github.com/MRCIEU/gwas-vcf-specification](https://github.com/MRCIEU/gwas-vcf-specification) |
| Citation | Lyon, M.S., Andrews, S.J., Elsworth, B. et al. The variant call format provides efficient and robust storage of GWAS summary statistics. Genome Biol 22, 32 (2021). https://doi.org/10.1186/s13059-020-02248-0 |
## Column mapping

| Raw header | Canonical | Canonical (secondary) |
| --- | --- | --- |
| `#CHROM` | CHR | — |
| `AF` | EAF | — |
| `ALT` | EA | — |
| `ES` | BETA | — |
| `EZ` | Z | — |
| `ID` | SNPID | rsID |
| `LP` | MLOG10P | — |
| `POS` | POS | — |
| `REF` | NEA | — |
| `SE` | SE | — |
| `SI` | INFO | — |
| `SS` | N | — |
## Fixed columns

**Required columns:** #CHROM, POS, ID, REF, ALT, QUAL, FILTER, INFO, FORMAT
**FORMAT fields (VCF):** ID, SS, ES, SE, LP, SI, EZ
<details>
<summary>Fixed header block</summary>

```
##fileformat=VCFv4.2
##FILTER=<ID=PASS,Description="All filters passed">
##INFO=<ID=AF,Number=A,Type=Float,Description="Allele Frequency">
##FORMAT=<ID=ES,Number=A,Type=Float,Description="Effect size estimate relative to the alternative allele">
##FORMAT=<ID=SE,Number=A,Type=Float,Description="Standard error of effect size estimate">
##FORMAT=<ID=LP,Number=A,Type=Float,Description="-log10 p-value for effect estimate">
##FORMAT=<ID=AF,Number=A,Type=Float,Description="Alternate allele frequency in the association study">
##FORMAT=<ID=SS,Number=A,Type=Float,Description="Sample size used to estimate genetic effect">
##FORMAT=<ID=EZ,Number=A,Type=Float,Description="Z-score provided if it was used to derive the EFFECT and SE fields">
##FORMAT=<ID=SI,Number=A,Type=Float,Description="Accuracy score of summary data imputation">
##FORMAT=<ID=NC,Number=A,Type=Float,Description="Number of cases used to estimate genetic effect">
##FORMAT=<ID=ID,Number=1,Type=String,Description="Study variant identifier">
##META=<ID=TotalVariants,Number=1,Type=Integer,Description="Total number of variants in input">
##META=<ID=VariantsNotRead,Number=1,Type=Integer,Description="Number of variants that could not be read">
##META=<ID=HarmonisedVariants,Number=1,Type=Integer,Description="Total number of harmonised variants">
##META=<ID=VariantsNotHarmonised,Number=1,Type=Integer,Description="Total number of variants that could not be harmonised">
##META=<ID=SwitchedAlleles,Number=1,Type=Integer,Description="Total number of variants strand switched">
##META=<ID=TotalControls,Number=1,Type=Integer,Description="Total number of controls in the association study">
##META=<ID=TotalCases,Number=1,Type=Integer,Description="Total number of cases in the association study">
##META=<ID=StudyType,Number=1,Type=String,Description="Type of GWAS study [Continuous or CaseControl]">
```
</details>

<details>
<summary>GRCh37 contig headers</summary>

```
##contig=<ID=1,length=249250621,assembly=HG19/GRCh37>
##contig=<ID=2,length=243199373,assembly=HG19/GRCh37>
##contig=<ID=3,length=198022430,assembly=HG19/GRCh37>
##contig=<ID=4,length=191154276,assembly=HG19/GRCh37>
##contig=<ID=5,length=180915260,assembly=HG19/GRCh37>
##contig=<ID=6,length=171115067,assembly=HG19/GRCh37>
##contig=<ID=7,length=159138663,assembly=HG19/GRCh37>
##contig=<ID=8,length=146364022,assembly=HG19/GRCh37>
##contig=<ID=9,length=141213431,assembly=HG19/GRCh37>
##contig=<ID=10,length=135534747,assembly=HG19/GRCh37>
##contig=<ID=11,length=135006516,assembly=HG19/GRCh37>
##contig=<ID=12,length=133851895,assembly=HG19/GRCh37>
##contig=<ID=13,length=115169878,assembly=HG19/GRCh37>
##contig=<ID=14,length=107349540,assembly=HG19/GRCh37>
##contig=<ID=15,length=102531392,assembly=HG19/GRCh37>
##contig=<ID=16,length=90354753,assembly=HG19/GRCh37>
##contig=<ID=17,length=81195210,assembly=HG19/GRCh37>
##contig=<ID=18,length=78077248,assembly=HG19/GRCh37>
##contig=<ID=19,length=59128983,assembly=HG19/GRCh37>
##contig=<ID=20,length=63025520,assembly=HG19/GRCh37>
##contig=<ID=21,length=48129895,assembly=HG19/GRCh37>
##contig=<ID=22,length=51304566,assembly=HG19/GRCh37>
##contig=<ID=23,length=155270560,assembly=HG19/GRCh37>
##contig=<ID=24,length=59373566,assembly=HG19/GRCh37>
##contig=<ID=25,length=16569,assembly=HG19/GRCh37>
```
</details>

<details>
<summary>GRCh38 contig headers</summary>

```
##contig=<ID=1,length=248956422,assembly=HG38/GRCh38>
##contig=<ID=2,length=242193529,assembly=HG38/GRCh38>
##contig=<ID=3,length=198295559,assembly=HG38/GRCh38>
##contig=<ID=4,length=190214555,assembly=HG38/GRCh38>
##contig=<ID=5,length=181538259,assembly=HG38/GRCh38>
##contig=<ID=6,length=170805979,assembly=HG38/GRCh38>
##contig=<ID=7,length=159345973,assembly=HG38/GRCh38>
##contig=<ID=8,length=145138636,assembly=HG38/GRCh38>
##contig=<ID=9,length=138394717,assembly=HG38/GRCh38>
##contig=<ID=10,length=133797422,assembly=HG38/GRCh38>
##contig=<ID=11,length=135086622,assembly=HG38/GRCh38>
##contig=<ID=12,length=133275309,assembly=HG38/GRCh38>
##contig=<ID=13,length=114364328,assembly=HG38/GRCh38>
##contig=<ID=14,length=107043718,assembly=HG38/GRCh38>
##contig=<ID=15,length=101991189,assembly=HG38/GRCh38>
##contig=<ID=16,length=90338345,assembly=HG38/GRCh38>
##contig=<ID=17,length=83257441,assembly=HG38/GRCh38>
##contig=<ID=18,length=80373285,assembly=HG38/GRCh38>
##contig=<ID=19,length=58617616,assembly=HG38/GRCh38>
##contig=<ID=20,length=64444167,assembly=HG38/GRCh38>
##contig=<ID=21,length=46709983,assembly=HG38/GRCh38>
##contig=<ID=22,length=50818468,assembly=HG38/GRCh38>
##contig=<ID=23,length=156040895,assembly=HG38/GRCh38>
##contig=<ID=24,length=57227415,assembly=HG38/GRCh38>
##contig=<ID=25,length=16569,assembly=HG38/GRCh38>
```
</details>

## Coverage

**9/9** tier groups satisfied.

| Tier | Status | Matched | Missing |
| --- | --- | --- | --- |
| Variant ID | yes | SNPID, rsID | — |
| Genomic location | yes | CHR, POS | — |
| Effect / other allele | yes | EA, NEA | — |
| Effect size | yes | BETA, Z | OR, HR |
| Uncertainty | yes | SE | — |
| P-value | yes | MLOG10P | P |
| Sample size | yes | N | N_CASE |
| Allele frequency | yes | EAF | MAF, NEAF |
| Imputation / QC | yes | INFO | — |
## See also

- [Format summary](../format_summary.html)
- [All formats](index.md)