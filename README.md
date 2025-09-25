<p align="center">
  <img src="./ProtectBanner_whitebg.png" alt="Protect Banner"/>
</p>

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
```

---

## 🐳 Quickstart

### 1. Build and Launch JupyterLab

```bash
docker-compose up --build
```

Then open your browser to [http://localhost:8888](http://localhost:8888) to begin.

---

### 2. Run a Pipeline by Data Type

From inside the container or a terminal window:

```bash
# Example: Run the isolate pipeline
python /app/scripts/run_exemplar_pipeline.py --type isolates --input /app/data/asma_exemplar_data/raw/isolates
```

Outputs will be saved to:

```
/app/data/asma_exemplar_data/processed/isolates/
```

---

## 📄 Output Files (Isolates)

Each isolate run will generate the following:

- `isolate_qc_summary.csv` – Folder and file structure validation
- `busco_summary.csv` – Genome completeness and assembly stats
- `faa_summary.csv`, `gff_summary.csv` – Annotation summaries
- `amr_matrix.csv`, `vf_matrix.csv` – Gene presence/absence matrices
- `isolate_master_summary.csv` – Full merged metadata and QC results
- `isolate_report_summary.csv` – Report-friendly view (for sharing)
- `isolate_pipeline_log_<timestamp>.csv` – Run log of pipeline execution

---

## 🙌 Contributions

Want to help expand support for MAGs, metaT, visualization dashboards, or cloud support?

PRs, issues, and feature requests are welcome!  
Please open an issue or reach out directly — we’d love your input.

---

## 👨‍🔬 Maintainer

**Spencer Long**  
Data Scientist @ WeArePROTECT  
🌐 [LinkedIn](https://www.linkedin.com/in/spencer42long)
