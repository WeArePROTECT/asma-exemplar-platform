# ASMA Exemplar Platform 🚀  
**Dockerized, scalable pipeline for processing exemplar microbiome data types**  
Built by the [WeArePROTECT](https://github.com/WeArePROTECT) team for the ARPA-H ASMA project.

---

## 🧬 What It Does

This platform supports standardized quality control and metadata extraction for multiple exemplar data types:
- `isolates` — Bacterial isolate genomes (FASTQ, assemblies, annotation, AMR/VF)
- `metag` — Shotgun metagenomic data (coming soon)
- `mag` — Metagenome-assembled genomes (planned)
- `metat` — Metatranscriptomic data (planned)

Each data type has its own modular pipeline for easy expansion and clean separation of logic.

---

## 📂 Project Structure

```bash
protect_asma_exemplar_platform/
├── data/
│   └── asma_exemplar_data/
│       ├── raw/         # Raw input data by type
│       └── processed/   # QC results and structured metadata
├── notebooks/           # Jupyter notebooks for EDA and reporting
├── scripts/
│   ├── isolate/         # Isolate pipeline scripts
│   ├── metag/           # (Coming soon)
│   ├── mag/, metat/     # (Scaffolded for future data types)
│   └── run_exemplar_pipeline.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md

🐳 Quickstart
1. Build and Launch JupyterLab
bash
Copy
Edit
docker-compose up --build
Then open http://localhost:8888 to begin.

2. Run a Pipeline by Data Type
From inside the container or terminal:

bash
Copy
Edit
# Example: Run isolate pipeline
python /app/scripts/run_exemplar_pipeline.py --type isolates --input /app/data/asma_exemplar_data/raw/isolates
Outputs will be saved to:

swift
Copy
Edit
/app/data/asma_exemplar_data/processed/isolates/
📄 Output Files
For isolates, the following files are produced:

isolate_qc_summary.csv – Folder and file structure validation

busco_summary.csv – Genome completeness and assembly stats

faa_summary.csv, gff_summary.csv – Annotation summaries

amr_matrix.csv, vf_matrix.csv – Gene presence/absence matrices

isolate_master_summary.csv – Full merged metadata and QC results

isolate_report_summary.csv – Filtered summary for presentation

isolate_pipeline_log_<timestamp>.csv – Batch processing log

🙌 Contributions
Want to help expand support for MAGs, metaT, or visualization dashboards?

PRs, ideas, and feature requests are welcome! Please open an issue or reach out directly.

👨‍🔬 Maintainer
Spencer Long
Data Scientist @ WeArePROTECT
