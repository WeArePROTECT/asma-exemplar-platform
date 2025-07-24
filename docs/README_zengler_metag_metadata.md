# ASMA Project - Zengler Lab metaG-Specific Metadata Template

This repository contains the standardized **metaG-specific metadata** for Zengler Lab contributions to the **ASMA** (Airway Synthetic Microbial Atlas) project.

The file [`zengler_lab_metag_metadata_template.csv`](./zengler_lab_metag_metadata_template.csv) captures information specific to the **metagenomics (metaG)** workflow, including DNA extraction methods, library preparation, and host read removal tools.

This metadata supports:
- Internal ASMA platform integration
- Downstream reproducibility and documentation
- Transparency in how raw metagenomic data were generated

---

## 📁 File Overview

- **Filename**: `zengler_lab_metag_metadata_template.csv`
- **Each row = one metaG protocol instance**
- Structured for per-sample or per-batch metadata, depending on pipeline setup
- Designed to complement sample-level metadata in other ASMA templates

---

## 🧬 Metadata Field Dictionary

| Column Name                    | Description                                                                 | Example Value                         |
|--------------------------------|-----------------------------------------------------------------------------|---------------------------------------|
| `dna_extraction_kit`           | Name of the kit or method used for DNA extraction                          | `Qiagen PowerSoil`                    |
| `input_sample_vol`             | Volume of biological material used for DNA extraction (include units)      | `250 µL`                              |
| `depth_target`                 | Target sequencing depth for the sample or run                              | `10 million reads`                    |
| `library_preparation_protocol` | Library prep protocol or kit used                                          | `Nextera XT`                          |
| `human_read_removal_tool`      | Name of the tool or pipeline used to remove host/human reads               | `KnightLab-HRR`                       |
| `human_read_removal_tool_link` | URL to GitHub repo or protocol documentation for host read removal         | `https://github.com/knightlab-ucsd/human-read-removal` |

---

## 🛠️ Notes

- This metadata is **specific to metagenomic (metaG) processing protocols** and complements core metadata tables that describe biological samples.
- `human_read_removal_tool` and `human_read_removal_tool_link` are designed to decouple tool names from documentation sources.
- If values in this table are consistent across all metaG samples, consider storing this metadata once and referencing it using a `protocol_id`.

---

## 🔗 Related Resources

- [ASMA Project Overview (UCB internal)](https://your.internal.link)
- [Knight Lab - Host Read Removal GitHub](https://github.com/knightlab-ucsd/human-read-removal)
- [Protocols.io](https://www.protocols.io/)

---

## 📤 Contributions

This metadata format was developed by the ASMA Data Integration Team in collaboration with the Zengler Lab.  
Please contact the ASMA metadata team for suggestions, revisions, or questions.
