# ASMA Project - Zengler Lab metaRS-Specific Metadata Template

This repository contains the standardized **metaRS-specific metadata** for Zengler Lab contributions to the **ASMA** (Airway Synthetic Microbial Atlas) project.

The file [`zengler_lab_metars_metadata_template.csv`](./zengler_lab_metars_metadata_template.csv) captures information specific to the **metagenomic ribosome profiling (metaRS)** workflow, including library preparation methods and sequencing depth targets.

This metadata supports:
- Internal ASMA platform integration
- Downstream reproducibility and documentation
- Transparency in how ribosome profiling data were generated

---

## 📁 File Overview

- **Filename**: `zengler_lab_metars_metadata_template.csv`
- **Each row = one metaRS protocol instance**
- Structured for per-sample or per-batch metadata, depending on pipeline setup
- Designed to complement sample-level metadata in other ASMA templates

---

## 🧬 Metadata Field Dictionary

| Column Name                  | Description                                                         | Example Value                   |
|-----------------------------|---------------------------------------------------------------------|---------------------------------|
| `library_preparation_protocol` | Kit or protocol used for ribosome profiling library prep             | `NEBNext Small RNA Library Prep` |
| `depth_target`              | Target sequencing depth for the sample or run                        | `20 million reads`             |

---

## 🛠️ Notes

- This metadata is **specific to ribosome profiling (metaRS)** workflows and complements core metadata tables.
- Additional metadata fields may be added in the future as protocols are finalized.

---

## 🔗 Related Resources

- [ASMA Project Overview (UCB internal)](https://your.internal.link)

---

## 📤 Contributions

This metadata format was developed by the ASMA Data Integration Team in collaboration with the Zengler Lab.  
Please contact the ASMA metadata team for suggestions, revisions, or questions.
