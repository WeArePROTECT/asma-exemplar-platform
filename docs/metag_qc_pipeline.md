# MetaG QC Pipeline Documentation

## 🔬 Overview
This pipeline performs automated quality control (QC) on metagenomic `.fastq.gz` files for the ARPA-H ASMA project. It standardizes file names, runs QC tools (FastQC + MultiQC), parses MultiQC output, applies thresholds, and generates a QC summary CSV.

---

## 📥 Input
A folder containing raw `.fastq.gz` files. Supported filenames include:
- `PRO123_metaG.fastq.gz`
- `PRO123_Illumina_metaG.fq.gz` (auto-renamed)

---

## ⚙️ What It Does
1. **(Optional)** Renames files to `PRO###_metaG.fastq.gz`
2. Runs **FastQC** on each file
3. Aggregates results with **MultiQC**
4. Parses MultiQC JSON (`multiqc_data.json`)
5. Extracts:
   - Median Q-score
   - Max adapter %
   - Avg read length
6. Filters out poly-G flagged samples (` - polyg`)
7. Applies thresholds:
   - Q ≥ 30
   - Adapter ≤ 5.0%
   - Read Length ≥ 85 bp
8. Writes:
   - `/processed/metag/metag_qc_summary.csv`

---

## 🚀 How to Run

### Full Run:
```bash
python /app/scripts/metag/metag_full_qc_pipeline.py /app/data/asma_exemplar_data/raw/metag
```

### Skip QC (use existing MultiQC data):
```bash
python /app/scripts/metag/metag_full_qc_pipeline.py /app/data/asma_exemplar_data/raw/metag --skip-qc
```

---

## 📤 Output
- `qc/` – FastQC outputs
- `qc_summary/` – MultiQC report + data
- `processed/metag/metag_qc_summary.csv` – Final QC summary

---

## 🧪 Dependencies
- `fastqc`
- `multiqc`
- Python:
  - `pandas`
  - `json`, `re`, `argparse`, `subprocess`

---

## 📌 Notes on Poly-G
- Samples ending in `" - polyg"` are excluded from final CSV
- These are artifacts from NovaSeq/NextSeq platforms
- Fix planned: `fastp --trim_poly_g` in preprocessing

