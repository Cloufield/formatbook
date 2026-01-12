# Format Design Documentation

## Overview

The formatbook is a standardized specification system for genetic association study output formats. It provides a unified way to describe, map, and convert between different file formats used in genomics research, enabling interoperability across various tools and pipelines.

## Core Concept

Each format specification maps tool-specific column names to a standardized set of canonical field names. This allows downstream tools to work with data from different sources without needing to know the specific column names used by each tool.

## Format Structure

Each format specification is a JSON object with three main sections:

### 1. `meta_data`

Contains metadata about the format specification itself:

- **`format_name`** (required): The name of the format (e.g., "tensorqtl_cis", "plink", "vcf")
- **`format_source`** (required): URL or reference to the official documentation for this format
- **`format_version`** (required): Version identifier for the format specification
- **`format_cite_name`** (optional): Name to use when citing this format
- **`format_citation`** (optional): Full citation string
- **`format_description`** (optional): Human-readable description of what this format represents
- **`format_separator`** (optional): Field separator character (e.g., "\t" for tab, " " for space)
- **`format_na`** (optional): How missing values are represented (e.g., "NA", ".", null, or an array of possible values)
- **`format_comment`** (optional): Character used for comment lines (e.g., "#")
- **`format_header`** (optional): Boolean indicating whether the file has a header row
- **`format_col_order`** (optional): Array specifying the expected column order
- **`format_datatype`** (optional): Object mapping column names to data types (e.g., "int", "float", "string", "category")
- **`format_fixed_header`** (optional): Fixed header lines (e.g., for VCF format)
- **`format_fixed`** (optional): Fixed columns that must be present
- **`format_format`** (optional): Format-specific fields (e.g., for VCF FORMAT field)
- **`format_assumption`** (optional): Notes about assumptions made in the format mapping
- **`format_notes`** (optional): Array of additional notes about the format
- **`last_check_date`** (optional): Date when the format specification was last verified
- **`software_license`** (optional): License information for the software that produces this format

### 2. `format_dict`

A dictionary mapping format-specific column names to canonical field names. This is the core mapping that enables format conversion.

**Key**: The actual column name as it appears in the format's output files  
**Value**: The standardized canonical field name (must be one of the headers defined in `src/gwaslab/qc/qc_researved_header.json`)

Example:
```json
{
  "variant_id": "SNPID",
  "pval_nominal": "P",
  "slope": "BETA",
  "slope_se": "SE"
}
```

This means:
- The column named `variant_id` in the format maps to the canonical field `SNPID`
- The column named `pval_nominal` maps to the canonical field `P`
- The column named `slope` maps to the canonical field `BETA`
- The column named `slope_se` maps to the canonical field `SE`

### 3. `header_description` (optional)

A dictionary providing human-readable descriptions for each canonical field used in this format. This helps users understand what each field represents.

**Key**: The canonical field name (same as values in `format_dict`)  
**Value**: Human-readable description

Example:
```json
{
  "variant_id": "Variant ID",
  "pval_nominal": "Nominal p-value of the association between the phenotype and variant",
  "slope": "Regression slope",
  "slope_se": "Standard error of the regression slope"
}
```

## Canonical Field Names

The formatbook uses a standardized set of canonical field names. **All canonical headers are defined in `gwaslab/qc/qc_researved_header.json`**, which serves as the authoritative reference for all valid canonical field names.

All values in `format_dict` must map to one of these reserved canonical headers. This ensures consistency and prevents the introduction of non-standard field names.

Common canonical field names include:

### Variant Identification
- **`SNPID`**: Variant identifier (primary)
- **`rsID`**: dbSNP rsID
- **`CHR`**: Chromosome
- **`POS`**: Base pair position
- **`REF`**: Reference allele
- **`ALT`**: Alternate allele

### Allele Information
- **`EA`**: Effect allele (the allele for which the effect size is reported)
- **`NEA`**: Non-effect allele (the other allele)
- **`EAF`**: Effect allele frequency
- **`NEAF`**: Non-effect allele frequency
- **`MAF`**: Minor allele frequency

### Association Statistics
- **`BETA`**: Effect size (beta coefficient)
- **`SE`**: Standard error of the effect size
- **`P`**: P-value
- **`MLOG10P`**: Minus log10 of p-value
- **`OR`**: Odds ratio
- **`OR_95L`**: Lower bound of 95% confidence interval for OR
- **`OR_95U`**: Upper bound of 95% confidence interval for OR
- **`Z`**: Z-score
- **`T`**: T-statistic
- **`CHISQ`**: Chi-square statistic

### Sample Information
- **`N`**: Sample size
- **`N_CASE`**: Number of cases
- **`N_CONTROL`**: Number of controls
- **`N_EFF`**: Effective sample size

### Quality Metrics
- **`INFO`**: Imputation quality score (INFO score)
- **`DIRECTION`**: Direction of effect across studies


## Format Examples

### Simple Format (tensorqtl_trans)

```json
{
  "meta_data": {
    "format_name": "tensorqtl_trans",
    "format_source": "https://raw.githubusercontent.com/broadinstitute/tensorqtl/refs/heads/master/docs/outputs.md",
    "format_version": "20220726",
    "format_cite_name": "tensorQTL",
    "format_description": "tensorQTL trans mode output format"
  },
  "format_dict": {
    "variant_id": "SNPID",
    "phenotype_id": "TRAIT",
    "pval": "P",
    "b": "BETA",
    "b_se": "SE",
    "r2": "R2",
    "af": "EAF"
  },
  "header_description": {
    "variant_id": "Variant ID",
    "phenotype_id": "Phenotype ID",
    "pval": "Nominal p-value of the association between the phenotype and variant",
    "b": "Regression slope",
    "b_se": "Standard error of the regression slope",
    "r2": "Squared residual genotype-phenotype correlation",
    "af": "In-sample ALT allele frequency of the variant"
  }
}
```

### Complex Format with Metadata (plink2_linear)

```json
{
  "meta_data": {
    "format_name": ".glm.linear",
    "format_source": "https://www.cog-genomics.org/plink/2.0/formats#glm",
    "format_version": "Alpha 3.3 final (3 Jun)",
    "format_cite_name": "PLINK 2.0",
    "format_separator": "\t",
    "format_na": ".",
    "format_comment": "#",
    "format_header": true,
    "format_col_order": [
      "#CHROM", "POS", "ID", "REF", "ALT", "A1",
      "FIRTH?", "TEST", "OBS_CT", "BETA", "SE", "T_STAT", "P"
    ],
    "last_check_date": "20250106"
  },
  "format_dict": {
    "ID": "SNPID",
    "#CHROM": "CHR",
    "CHROM": "CHR",
    "POS": "POS",
    "REF": "REF",
    "ALT": "ALT",
    "A1": "EA",
    "OBS_CT": "N",
    "A1_FREQ": "EAF",
    "BETA": "BETA",
    "SE": "SE",
    "T_STAT": "T",
    "P": "P"
  }
}
```

## Design Principles

1. **Standardization**: All formats map to the same set of canonical field names, enabling universal compatibility.

2. **Extensibility**: New formats can be added by creating new JSON files following the same structure.

3. **Documentation**: Each format includes source references and descriptions to ensure traceability.

4. **Flexibility**: Optional fields allow formats to specify their unique characteristics (separators, missing value representations, etc.).

5. **Versioning**: Format versions and last check dates help track changes and ensure specifications stay current.


## Usage

The formatbook enables:

- **Format Detection**: Automatically identify which format a file uses based on column names
- **Format Conversion**: Convert between different formats by mapping through canonical fields
- **Tool Interoperability**: Use the same downstream tools with data from different sources
- **Validation**: Verify that files conform to expected format specifications
- **Documentation**: Provide clear descriptions of what each field represents

## File Organization

- Individual format specifications are stored in `formats/*.json`
- All formats are aggregated into a single `formatbook.json` file
- Each format is keyed by its format identifier (e.g., "tensorqtl_cis", "plink")
- **Canonical headers are defined in `src/gwaslab/qc/qc_researved_header.json`** - this file contains the authoritative list of all valid canonical field names that can be used as values in `format_dict`

## Future Considerations

- Support for nested/structured data formats
- Validation schemas for data types and value ranges
- Format evolution tracking
- Automated format detection and validation tools
