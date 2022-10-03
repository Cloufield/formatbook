# FormatBook

This is a companion repo for [gwaslab](https://github.com/Cloufield/gwaslab). 

A collection of commonly used formats for GWAS summmary statistics. 

All the formats are stored as json files.

Each format consists of the following info (manually curated):
1. `meta_data`: meta data, inlcluding software name, source urls, version and so on.
2. `format_dict`: target format to gwaslab format column-name conversion dictionary 

For example : format for metal software
```
{
"meta_data":{"format_name":"metal",
            "format_source":"https://genome.sph.umich.edu/wiki/METAL_Documentation",
            "format_version":"20220726"
            },
"format_dict":{
            "MarkerName":"SNPID",
            "Allele1":"EA",
            "Allele2":"NEA",
            "Freq1":"EAF",
            "Effect":"BETA",
            "StdErr":"SE",
            "P-value":"P",
            "Direction": "DIRECTION"
            }
}
```

Supported formats:
1. `ssf`: GWAS-SSF
2. `gwascatalog` : GWAS Catalog format
3. `pgscatalog` : PGS Catalog format
4. `plink`: PLINK output format
5. `plink2`:  PLINK2 output format
6. `saige`: SAIGE output format
7. `regenie`: output format
8. `fastgwa`: output format
9. `metal`: output format
10. `mrmega`: output format
11. `fuma`: input format
12. `ldsc`: input format
13. `locuszoom`: input format
14. `vcf`: gwas-vcf format
