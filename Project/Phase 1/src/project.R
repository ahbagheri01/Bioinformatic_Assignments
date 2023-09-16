if (!require("BiocManager", quietly = TRUE)){
  install.packages("BiocManager",repos='http://cran.us.r-project.org')
  BiocManager::install(version = "3.10")
  BiocManager::install("GEOquery")
}
if (!require("BiocManager", quietly = TRUE)){
  install.packages("BiocManager")
  BiocManager::install(version = "3.10")
  BiocManager::install("GEOquery")
}

if(length(new.packages)) install.packages(new.packages)


