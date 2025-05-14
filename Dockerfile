FROM jupyter/datascience-notebook:latest

LABEL maintainer="Spencer Long"

USER root

# Install mamba (fast conda alternative)
RUN conda install -y -c conda-forge mamba

# Install bioinformatics tools efficiently with mamba
RUN mamba install -y -c bioconda -c conda-forge \
    fastqc \
    multiqc \
    prokka \
    busco

USER $NB_UID
