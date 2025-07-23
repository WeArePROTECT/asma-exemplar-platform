# ASMA Project - Zengler Lab SRA Metadata Template

This repository contains the standardized metadata format for Zengler Lab contributions to the **ASMA** (Airway Synthetic Microbial Atlas) project.

The file [`zengler_lab_sra_metadata_template.csv`](./zengler_lab_sra_metadata_template.csv) captures detailed metadata for each sequencing library submitted by the Zengler lab, formatted to support:

- SRA (Sequence Read Archive) submission via NCBI
- Integration into ASMA’s data pipeline and KBase backend
- Cross-omics traceability and reproducibility

---

## 📁 File Overview

- **Filename**: `zengler_lab_sra_metadata_template.csv`
- **Each row = one sequencing library**
- Supports multiple omics types: `metaG`, `metaT`, `metaRS`

---

## 🧬 What is SRA?

**SRA** stands for **Sequence Read Archive**, a public repository managed by NCBI that stores raw sequencing data. Submitting to SRA ensures reproducibility, accessibility, and long-term preservation of experimental data.

---

## 📋 Metadata Field Dictionary

| Column Name         | Description                                                                                      | Example Value                                 |
|---------------------|--------------------------------------------------------------------------------------------------|-----------------------------------------------|
| `sample_name`       | Unique identifier for the biological sample collected from a subject.                           | `PRO15`                                       |
| `library_ID`        | Identifier for the specific sequencing library derived from the sample. Typically includes omics type. | `PRO15_metaG`                                 |
| `library_number`    | Internal lab identifier for the sequencing library, useful for tracking prep and submission order. | `L1`                                          |
| `omics_type`        | Type of omics data represented by the library (e.g., metaG = metagenomics, metaT = metatranscriptomics, metaRS = MetaRiboSeq). | `metaG`     |
| `title`             | Descriptive title for the sequencing experiment, used in SRA submissions.                       | `DNAseq-PRO15-patient-sputum`                 |
| `library_strategy`  | The sequencing strategy used (e.g., WGS for whole genome shotgun).                               | `WGS`                                         |
| `library_source`    | The biological source material, such as 'Metagenomic'.                                           | `Metagenomic`                                 |
| `library_selection` | Method used to enrich or select the library content (e.g., PCR, random, polyA).                 | `PCR`                                         |
| `library_layout`    | Indicates whether reads are single-end or paired-end.                                           | `paired`                                      |
| `platform`          | Sequencing platform used, such as Illumina.                                                     | `Illumina`                                    |
| `instrument_model`  | Specific model of the sequencing instrument (e.g., NovaSeq X Plus 10B).                         | `NovaSeq X Plus 10B`                          |
| `design_description`| Brief protocol summary used in sequencing, detailing sample prep and processing.               | `DNA was extracted from sputum using HostZERO Microbial DNA Kit (Zymo Research)...` |
| `protocols_io_id`   | Link to full protocol on Protocols.io for reproducibility.                                      | `https://www.protocols.io/view/xyz123`        |
| `filetype`          | Format of the sequencing data file (e.g., fastq).                                               | `fastq`                                       |
| `filename`          | Name of the R1 FASTQ file for paired-end reads.                                                 | `PRO15_metaG_S6_L005_R1_001.fastq.gz`         |
| `filename2`         | Name of the R2 FASTQ file for paired-end reads.                                                 | `PRO15_metaG_S6_L005_R2_001.fastq.gz`         |

---

## 🛠️ Notes

- Fields like `filename` and `filename2` must match real FASTQ files delivered with each dataset.
- Protocol summaries should be brief. Full protocol details should be linked via `protocols_io_id`.
- We recommend storing a canonical copy of this template in the ASMA GitHub repo.

---

## 🔗 Related Resources

- [NCBI SRA Submission Portal](https://www.ncbi.nlm.nih.gov/sra/docs/submit/)
- [Protocols.io](https://www.protocols.io/)
- [ASMA Project Overview (UCB internal)](https://your.internal.link)

---

## 📤 Contributions

This format was developed in collaboration with the Zengler Lab and the ASMA data integration team. For questions, updates, or to suggest changes, please contact the ASMA Data Scientist team.

