# Format Design Documentation

## Overview

The formatbook is a standardized specification system for genetic association study output formats. It provides a unified way to describe, map, and convert between different file formats used in genomics research, enabling interoperability across various tools and pipelines.

## Core Concept

Each format specification maps tool-specific column names to a standardized set of canonical field names used in GWASLab. This allows downstream tools to work with data from different sources without needing to know the specific column names used by each tool.

## Format Structure

Each format specification is a JSON object with required `meta_data` and `format_dict`, plus optional sections `format_dict_2`, `header_description`, `companion_meta`, and `phenotype_types` (see below).

### 1. `meta_data`

Contains metadata about the format specification itself:

| Field | Required | Description |
| --- | --- | --- |
| `format_name` | Yes | The name of the format (e.g., "tensorqtl_cis", "plink", "vcf") |
| `format_source` | Yes | URL or reference to the official documentation for this format |
| `format_source_2` | No | Second URL/reference when a format has multiple official sources |
| `format_version` | Yes | Version identifier for the format specification |
| `format_cite_name` | No | Name to use when citing this format |
| `format_citation` | No | Full citation string |
| `format_description` | No | Human-readable description of what this format represents |
| `format_separator` | No | Field separator character (e.g., "\t" for tab, " " for space) |
| `format_na` | No | How missing values are represented (e.g., "NA", ".", null, or an array of possible values) |
| `format_comment` | No | Character used for comment lines (e.g., "#") |
| `format_header` | No | Boolean indicating whether the file has a header row |
| `format_header_lines` | No | Number of header lines before data rows (e.g. `2` for Oxford `.sample` files with a two-line header) |
| `format_header_line2_description` | No | Human-readable explanation of the second header line when `format_header_lines` ≥ 2 (e.g. column type codes in `.sample` files) |
| `format_col_order` | No | Array specifying the expected column order |
| `format_datatype` | No | Object mapping column names to data types (e.g., "int", "float", "string", "category") |
| `format_fixed_header` | No | Fixed header lines (e.g., for VCF format) |
| `format_contig_19` | No | Literal `##contig=` header block for GRCh37/hg19 (assembly 19), when a format embeds or documents reference contigs separately from `format_fixed_header` (e.g. GWAS-VCF examples) |
| `format_contig_38` | No | Literal `##contig=` header block for GRCh38/hg38 (assembly 38), same use case as `format_contig_19` |
| `format_fixed` | No | Fixed columns that must be present |
| `format_format` | No | Format-specific fields (e.g., for VCF FORMAT field) |
| `format_assumption` | No | Notes about assumptions made in the format mapping |
| `format_notes` | No | Array of additional notes about the format |
| `last_check_date` | No | Date when the format specification was last verified |
| `software_license` | No | License information for the software that produces this format |

Naming rule for repeated metadata fields:

- For multiple values of the same field, use an underscore and a numeric suffix: `2`, `3`, ...
- Example: `format_source` (first), `format_source_2`, `format_source_3`, ...
- Do not use `format_source_1` (use `format_source` for the primary reference) or legacy keys like `format_source2` (no underscore).

### 2. `format_dict`

A dictionary mapping format-specific column names to canonical field names. This is the core mapping that enables format conversion.

**Key**: The actual column name as it appears in the format's output files  
**Value**: A GWASLab canonical field name (string from `qc/qc_researved_header.json`), or **`null`** if the column may appear but is not mapped to any canonical field.

Do **not** repeat the same key twice in `format_dict` (duplicate JSON keys are invalid for this repo and rejected by `scripts/check_format_jsons.py`). For a second canonical mapping for the same raw header, use **`format_dict_2`** (see below).

Use `null` when you want to document extra columns (for example tool-specific statistics) so detectors and validators know the header may appear, without claiming a GWASLab canonical mapping. Do not use `format_other_cols` or similar separate lists; keep those columns in `format_dict` with `null` values instead.

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

### 3. `format_dict_2` (optional)

Additional raw → canonical pairs for headers that already appear in `format_dict` with a **different** canonical. Use this when one physical column may represent two GWASLab fields (for example `SNP` as both `SNPID` and `rsID`).

**Rules:**

- Every key in `format_dict_2` must also be a key in `format_dict`.
- `format_dict_2[raw]` must be a non-empty string (a canonical name) and must **differ** from `format_dict[raw]` (when the latter is not `null`).
- `format_dict[raw]` must be a mapped string (not `null`) if `raw` appears in `format_dict_2`.

**Order:** Treat `format_dict` as the primary mapping, then `format_dict_2` for the secondary canonical for the same raw header.

Example:

```json
{
  "format_dict": { "SNP": "SNPID", "A1": "EA" },
  "format_dict_2": { "SNP": "rsID" }
}
```

### 4. `header_description` (optional)

A dictionary providing human-readable descriptions for each raw/source header used in this format.

**Key**: The raw/source header name (same as keys in `format_dict`)  
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

### 5. `companion_meta` (optional)

Use this section when a format has a companion metadata file (for example SSF sidecar metadata).

Minimal fields:

| Field | Required | Description |
| --- | --- | --- |
| `meta_file_required` | No | Whether the companion metadata file is required for parsing/conversion |
| `meta_file_format` | No | Metadata file type (e.g., `yaml`, `json`) |
| `meta_to_canonical` | No | Mapping from metadata keys to GWASLab canonical fields |

Example:
```json
{
  "companion_meta": {
    "meta_file_required": false,
    "meta_file_format": "yaml",
    "meta_to_canonical": {
      "genome_build": "BUILD",
      "trait": "TRAIT",
      "sample_size": "N"
    }
  }
}
```

### 6. `phenotype_types` (optional)

Top-level object documenting phenotype column type letters used by a format (not mapped through `format_dict`). Keys are single-letter codes; values are short human-readable definitions.

Example (Oxford `.sample` second-line codes `B` / `D` / `P`):

```json
{
  "phenotype_types": {
    "B": "Binary phenotype ('0' = control, '1' = case, 'NA' = missing)",
    "D": "Discrete/categorical phenotype (positive integers, 'NA' = missing)",
    "P": "Continuous phenotype (real numbers, 'NA' = missing)"
  }
}
```

## Canonical Field Names

The formatbook uses a standardized set of canonical field names. **All canonical headers are defined in the GWASLab package (`qc/qc_researved_header.json`)**, which serves as the authoritative reference for all valid canonical field names.

Every canonical name used in `format_dict` and `format_dict_2` must be one of these reserved headers. This ensures consistency and prevents the introduction of non-standard field names.

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

## Auto-detection presets

The `formats/auto*.json` specs are wide alias tables for GWAS summary statistics. Names **omit** default choices: default is **A1** = EA, effect on **ALT**, generic **Frq** → **EAF** (`auto.json`). Non-default index, REF-as-EA, or NEAF appear as suffixes (e.g. **`auto_0`**, **`auto_ref`**, **`auto_neaf`**). Assumption-key columns in each **`format_dict`** are checked against **`format_name`** by **`scripts/check_auto_assumption_dict.py`** (see **[auto.md](auto.md)**).

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

- Auto-preset documentation: [docs/auto.md](auto.md)
- Individual format specifications are stored in `formats/*.json`
- All formats are aggregated into a single `formatbook.json` file
- Each format is keyed by its format identifier (e.g., "tensorqtl_cis", "plink")
- **Canonical headers are defined in the GWASLab package (`qc/qc_researved_header.json`)** - this file contains the authoritative list of all valid canonical field names that can be used as values in `format_dict` and `format_dict_2`

## Future Considerations

- Support for nested/structured data formats
- Validation schemas for data types and value ranges
- Format evolution tracking
- Automated format detection and validation tools

## Policy: `SNPID`, `rsID`, and one raw column

When one physical column (e.g. `SNP`, FORMAT `ID`) can represent **both** a primary variant ID and an rsID, put the primary mapping in `format_dict` and the second in `format_dict_2` with the **same raw key** (e.g. `format_dict.SNP` → `SNPID`, `format_dict_2.SNP` → `rsID`). Order is primary then secondary.

### Forward conversion (raw → GWASLab)

- Prefer populating both `SNPID` and `rsID` when the pipeline can classify values (e.g. `rs\d+` → `rsID`).
- If only one harmonized column is produced, follow convention (often `SNPID`).

### Reverse conversion (GWASLab → raw)

- Combine `format_dict` and `format_dict_2` to recover raw header names. When several canonicals map to the same raw header, choose which value to write using your tool’s policy (e.g. prefer `SNPID` if non-missing, else `rsID`).

### Other aliases

- Separate raw headers for rsID vs variant ID should remain **separate keys** in `format_dict` when the file actually has two columns.
