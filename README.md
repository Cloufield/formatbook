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

# Citations and sources
1. GWAS-SSF
    - CITATION: Hayhurst, J., Buniello, A., Harris, L., Mosaku, A., Chang, C., Gignoux, C. R., ... & Barroso, I. (2022). A community driven GWAS summary statistics standard. bioRxiv.
1. GWAS Catalog
    - SOURCE: [https://www.ebi.ac.uk/gwas/docs/summary-statistics-format](https://www.ebi.ac.uk/gwas/docs/summary-statistics-format)
    - CITATION: Buniello, A., MacArthur, J. A. L., Cerezo, M., Harris, L. W., Hayhurst, J., Malangone, C., ... & Parkinson, H. (2019). The NHGRI-EBI GWAS Catalog of published genome-wide association studies, targeted arrays and summary statistics 2019. Nucleic acids research, 47(D1), D1005-D1012.
1. metal
    - SOURCE: [https://genome.sph.umich.edu/wiki/METAL_Documentation](https://genome.sph.umich.edu/wiki/METAL_Documentation)
    - CITATION: Willer, C. J., Li, Y., & Abecasis, G. R. (2010). METAL: fast and efficient meta-analysis of genomewide association scans. Bioinformatics, 26(17), 2190-2191.
1. pgscatalog
    - SOURCE: [https://www.pgscatalog.org/downloads/#dl_ftp_scoring](https://www.pgscatalog.org/downloads/#dl_ftp_scoring)
    - CITATION: Lambert, S. A., Gil, L., Jupp, S., Ritchie, S. C., Xu, Y., Buniello, A., ... & Inouye, M. (2021). The Polygenic Score Catalog as an open database for reproducibility and systematic evaluation. Nature Genetics, 53(4), 420-425.
1. saige
    - SOURCE:
    - CITATION:
1. regenie
    - SOURCE:
    - CITATION:
1. plink
    - SOURCE:
    - CITATION:
1. plink2
    - SOURCE:
    - CITATION:
1. regenie
    - SOURCE:
    - CITATION:
1. fastgwa
    - SOURCE:
    - CITATION:
1. mrmega
    - SOURCE:
    - CITATION:
1. fuma
    - SOURCE:
    - CITATION:
1. ldsc
    - SOURCE:
    - CITATION:
1. locuszoom
    - SOURCE:
    - CITATION:
1. vcf
    - SOURCE:
    - CITATION:

