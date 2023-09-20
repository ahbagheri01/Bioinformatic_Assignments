# Bioinformatic_Assignments And Project
<br/>
<p align="center">
  <h1 align="center">Microarray Data Analysis</h3>

  <p align="center">
    Microarray Expression Data Analysis for AML and Normal Cells
    <br/>
    <br/>
  </p>
</p>

## About The Project

This is the project for the "Introduction to Bioinformatics" course at Sharif University of Technology analyzing microarray data. The data is available in the [GEO](https://www.ncbi.nlm.nih.gov/geo/) database with the accession number [GSE48558](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE48558).


## Phase 1

In this phase, we analyze the given data and plot the results. The data is downloaded using the [GEOquery](https://bioconductor.org/packages/release/bioc/html/GEOquery.html) package in [R](https://www.r-project.org/). The data is then normalized using the [limma](https://bioconductor.org/packages/release/bioc/html/limma.html) package in [R](https://www.r-project.org/). It is then analyzed using the [umap](https://cran.r-project.org/web/packages/umap/vignettes/umap.html) package in [R](https://www.r-project.org/). The results are then visualized using [ggplot2](https://ggplot2.tidyverse.org/) and [corrplot](https://cran.r-project.org/web/packages/corrplot/index.html). 

Then, we used dimensionality reduction techniques such as [PCA](https://en.wikipedia.org/wiki/Principal_component_analysis), [TSNE](https://en.wikipedia.org/wiki/T-distributed_stochastic_neighbor_embedding), and [MDS](https://en.wikipedia.org/wiki/Multidimensional_scaling) to visualize the data. The results are shown below:

<table>
  <tr align="center">
    <td>PCA</td>
    <td>TSNE</td>
    <td>MDS</td>
  </tr>
  <tr>
    <td><img src="Phase%201/figs/pca6.png" width=300 height=300></td>
    <td><img src="Phase%201/figs/tsnep5.png" width=300 height=300></td>
    <td><img src="Phase%201/figs/mds.png" width=300 height=300></td>
  </tr>
 </table>

Finally, we analyzed the correlation between different groups of patients. The results are shown below:

![Correlation](Phase%201/figs/SourceName-Cor-Heatmap-1.png)

### Report

The final report (in persian) is presented in the [documentation](/Phase%201/report.pdf) for phase 1. The code is available in [this](/Phase%201/Bio_Phase_1.ipynb) jupyter notebook.

## Phase 2

In this phase, we used the [limma](https://bioconductor.org/packages/release/bioc/html/limma.html) package in [R](https://www.r-project.org/) to find the differentially expressed genes (DEGs) between the AML and normal cells. We then used the [Enricher](https://maayanlab.cloud/Enrichr/) to find the enriched pathways and gene ontology in the DEGs.

Finally, we investigated different research papers to find the most important pathways and genes in AML cancer.

### Report

The final report (in persian) is presented in the [documentation](/Phase%202/report.pdf) for phase 2. The code is available in [this](/Phase%202/Bio_Phase_2.ipynb) jupyter notebook. The data is available in [this](/Phase%202/data/AML_Healthy.tsv) tsv file.

