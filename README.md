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

|Keyword|Software|Description|Citation|
|-|-|-|-|
|`ssf`|[GWAS Catalog](https://www.ebi.ac.uk/gwas/docs/summary-statistics-format)|GWAS-SSF|Hayhurst, J., Buniello, A., Harris, L., Mosaku, A., Chang, C., Gignoux, C. R., ... & Barroso, I. (2022). A community driven GWAS summary statistics standard. bioRxiv.|
|`gwascatalog`|[GWAS Catalog](https://www.ebi.ac.uk/gwas/docs/summary-statistics-format)|GWAS Catalog format (outdated; please use GWAS-SSF)| Buniello, A., MacArthur, J. A. L., Cerezo, M., Harris, L. W., Hayhurst, J., Malangone, C., ... & Parkinson, H. (2019). The NHGRI-EBI GWAS Catalog of published genome-wide association studies, targeted arrays and summary statistics 2019. Nucleic acids research, 47(D1), D1005-D1012. |
|`pgscatalog`|[PGS Catalog](https://www.pgscatalog.org/downloads/#dl_ftp_scoring)|PGS Catalog format|Lambert, S. A., Gil, L., Jupp, S., Ritchie, S. C., Xu, Y., Buniello, A., ... & Inouye, M. (2021). The Polygenic Score Catalog as an open database for reproducibility and systematic evaluation. Nature Genetics, 53(4), 420-425.|
|`plink`|[PLINK](https://www.cog-genomics.org/plink/1.9/formats)|PLINK output format (only unambiguous headers)|Purcell, S., Neale, B., Todd-Brown, K., Thomas, L., Ferreira, M. A., Bender, D., ... & Sham, P. C. (2007). PLINK: a tool set for whole-genome association and population-based linkage analyses. The American journal of human genetics, 81(3), 559-575.|
|`plink_assoc` / `plink_fisher`|[PLINK](https://www.cog-genomics.org/plink/1.9/formats)| `.assoc`, `.assoc.fisher`|Purcell, S., Neale, B., Todd-Brown, K., Thomas, L., Ferreira, M. A., Bender, D., ... & Sham, P. C. (2007). PLINK: a tool set for whole-genome association and population-based linkage analyses. The American journal of human genetics, 81(3), 559-575.|
|`plink_dosage`|[PLINK](https://www.cog-genomics.org/plink/1.9/formats)|`.assoc.dosage`|Purcell, S., Neale, B., Todd-Brown, K., Thomas, L., Ferreira, M. A., Bender, D., ... & Sham, P. C. (2007). PLINK: a tool set for whole-genome association and population-based linkage analyses. The American journal of human genetics, 81(3), 559-575.|
|`plink_logistic`|[PLINK](https://www.cog-genomics.org/plink/1.9/formats)| `.assoc.logistic`|Purcell, S., Neale, B., Todd-Brown, K., Thomas, L., Ferreira, M. A., Bender, D., ... & Sham, P. C. (2007). PLINK: a tool set for whole-genome association and population-based linkage analyses. The American journal of human genetics, 81(3), 559-575.|
|`plink_linear`|[PLINK](https://www.cog-genomics.org/plink/1.9/formats)|`.assoc.linear`|Purcell, S., Neale, B., Todd-Brown, K., Thomas, L., Ferreira, M. A., Bender, D., ... & Sham, P. C. (2007). PLINK: a tool set for whole-genome association and population-based linkage analyses. The American journal of human genetics, 81(3), 559-575.|
|`plink2`|[PLINK2](https://www.cog-genomics.org/plink/2.0/formats)|PLINK2 output format (only unambiguous headers)|Chang, C. C., Chow, C. C., Tellier, L. C., Vattikuti, S., Purcell, S. M., & Lee, J. J. (2015). Second-generation PLINK: rising to the challenge of larger and richer datasets. Gigascience, 4(1), s13742-015.|
|`plink2_linear`|[PLINK2](https://www.cog-genomics.org/plink/2.0/formats)| `.glm.linear`|Chang, C. C., Chow, C. C., Tellier, L. C., Vattikuti, S., Purcell, S. M., & Lee, J. J. (2015). Second-generation PLINK: rising to the challenge of larger and richer datasets. Gigascience, 4(1), s13742-015.|
|`plink2_logistic` / `plink2_firth`|[PLINK2](https://www.cog-genomics.org/plink/2.0/formats)| `.glm.firth`, `.glm.logistic[.hybrid]`|Chang, C. C., Chow, C. C., Tellier, L. C., Vattikuti, S., Purcell, S. M., & Lee, J. J. (2015). Second-generation PLINK: rising to the challenge of larger and richer datasets. Gigascience, 4(1), s13742-015.|
|`saige`|[SAIGE](https://github.com/weizhouUMICH/SAIGE/wiki/Genetic-association-tests-using-SAIGE#output-file)| output format|Zhou, W., Nielsen, J. B., Fritsche, L. G., Dey, R., Gabrielsen, M. E., Wolford, B. N., ... & Lee, S. (2018). Efficiently controlling for case-control imbalance and sample relatedness in large-scale genetic association studies. Nature genetics, 50(9), 1335-1341.|
|`regenie`|[REGENIE](https://rgcgithub.github.io/regenie/options/#output)|output format|Mbatchou, J., Barnard, L., Backman, J., Marcketta, A., Kosmicki, J. A., Ziyatdinov, A., ... & Marchini, J. (2021). Computationally efficient whole-genome regression for quantitative and binary traits. Nature genetics, 53(7), 1097-1103.|
|`fastgwa`|[FASTGWA](https://yanglab.westlake.edu.cn/software/gcta/#fastGWA)|output format|Jiang, L., Zheng, Z., Qi, T., Kemper, K. E., Wray, N. R., Visscher, P. M., & Yang, J. (2019). A resource-efficient tool for mixed model association analysis of large-scale data. Nature genetics, 51(12), 1749-1755.|
|`metal`|[METAL](https://genome.sph.umich.edu/wiki/METAL_Documentation)|output format|Willer, C. J., Li, Y., & Abecasis, G. R. (2010). METAL: fast and efficient meta-analysis of genomewide association scans. Bioinformatics, 26(17), 2190-2191.|
|`mrmega`|[MRMEGA](https://genomics.ut.ee/en/tools)|output format|Mägi, R., Horikoshi, M., Sofer, T., Mahajan, A., Kitajima, H., Franceschini, N., ... & Morris, A. P. (2017). Trans-ethnic meta-regression of genome-wide association studies accounting for ancestry increases power for discovery and improves fine-mapping resolution. Human molecular genetics, 26(18), 3639-3650.|
|`fuma`|[FUMA](https://fuma.ctglab.nl/tutorial#snp2gene)|input format|atanabe, K., Taskesen, E., Van Bochoven, A., & Posthuma, D. (2017). Functional mapping and annotation of genetic associations with FUMA. Nature communications, 8(1), 1-11.|
|`ldsc`|[LDSC](https://github.com/bulik/ldsc/wiki/Heritability-and-Genetic-Correlation)|input format|Bulik-Sullivan, B. K., Loh, P. R., Finucane, H. K., Ripke, S., Yang, J., Patterson, N., ... & Neale, B. M. (2015). LD Score regression distinguishes confounding from polygenicity in genome-wide association studies. Nature genetics, 47(3), 291-295.|
|`locuszoom`|[LocusZoom](https://my.locuszoom.org/about/)|input format|Pruim, R. J., Welch, R. P., Sanna, S., Teslovich, T. M., Chines, P. S., Gliedt, T. P., ... & Willer, C. J. (2010). LocusZoom: regional visualization of genome-wide association scan results. Bioinformatics, 26(18), 2336-2337.|
|`vcf`|[GWAS-VCF](https://github.com/MRCIEU/gwas-vcf-specification)|gwas-vcf format|Lyon, M. S., Andrews, S. J., Elsworth, B., Gaunt, T. R., Hemani, G., & Marcora, E. (2021). The variant call format provides efficient and robust storage of GWAS summary statistics. Genome biology, 22(1), 1-10.|
|`bolt_lmm`|[BOLT-LMM](https://alkesgroup.broadinstitute.org/BOLT-LMM/BOLT-LMM_manual.html)|output format|Loh, P. R., Tucker, G., Bulik-Sullivan, B. K., Vilhjalmsson, B. J., Finucane, H. K., Salem, R. M., ... & Price, A. L. (2015). Efficient Bayesian mixed-model analysis increases association power in large cohorts. Nature genetics, 47(3), 284-290.|
|`popcorn`|[popcorn](https://github.com/brielin/Popcorn)|input format|Brown, B. C., Ye, C. J., Price, A. L., & Zaitlen, N. (2016). Transethnic genetic-correlation estimates from summary statistics. The American Journal of Human Genetics, 99(1), 76-88.|
|`cojo`|[cojo](https://yanglab.westlake.edu.cn/software/gcta/#COJO)|input format|Yang et al. (2012) Conditional and joint multiple-SNP analysis of GWAS summary statistics identifies additional variants influencing complex traits. Nat Genet 44(4):369-375.|

Future update:
To add fields in meta_data:
1. `format_cite_name` : formal name of the format, e.g. GWAS-SSF v0.1
1. `format_separator` : separator used in the format, e.g. `\t`
1. `format_na` : NA notation in the format, e.g. `#NA`
1. `format_comment` : comment line, e.g. `#`
1. `format_col_order`: column order
