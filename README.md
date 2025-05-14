# PROTECT ASMA Exemplar Data Platform

This Dockerized environment is designed to support metagenomic, isolate, MAG, and other exemplar data processing pipelines for the ASMA project.

## Structure

- `data/asma_exemplar_data/raw/` – Raw input data, organized by type
- `data/asma_exemplar_data/processed/` – Cleaned and processed outputs
- `scripts/` – Pipeline scripts organized by data type
- `notebooks/` – Jupyter notebooks for EDA and reporting

## Usage

Build and start the environment:
```bash
docker-compose up --build
```

Then open your browser to `localhost:8888` to begin.

## Types Supported

- `metag` – metagenomic shotgun data
- `isolates` – isolate genomes
- `mag` – metagenome-assembled genomes
- `metat` – metatranscriptomic data

More types can be added modularly.
