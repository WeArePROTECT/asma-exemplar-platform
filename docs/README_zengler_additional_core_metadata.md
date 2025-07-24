# ASMA Project - Zengler Lab Additional Core Metadata Template

This repository contains the standardized **Additional Core Metadata** format for Zengler Lab contributions to the **ASMA** (Airway Synthetic Microbial Atlas) project.

The file [`zengler_lab_additional_core_metadata_template.csv`](./zengler_lab_additional_core_metadata_template.csv) captures key metadata necessary for internal data integration, downstream quality control, and multi-omics alignment across the ASMA platform.

---

## 📁 File Overview

- **Filename**: `zengler_lab_additional_core_metadata_template.csv`
- **Each row = one biological sample**
- Supports multiple omics data types: `metaG`, `metaT`, `metaRS`, etc.
- Focused on structured, machine-readable metadata to support automation, validation, and reproducibility.

---

## 🧬 Metadata Field Dictionary

| Column Name                 | Description                                                                                       | Example Value                        |
|-----------------------------|---------------------------------------------------------------------------------------------------|--------------------------------------|
| `sample_id`                 | Unique identifier for the biological sample. Used across all ASMA metadata.                      | `PRO15_metaG`                        |
| `subject_id`                | Identifier for the subject or patient. Leave blank unless de-identified and approved.             | `ZENG001`                            |
| `sample_type`              | Type of sample collected (e.g., sputum, swab).                                                    | `sputum`                             |
| `collection_site`          | Anatomical site where the sample was collected.                                                   | `lower respiratory tract`           |
| `collection_method`        | How the sample was collected (e.g., expectoration, BAL).                                          | `spontaneous expectoration`         |
| `collection_date`          | Date of sample collection. Retained in full form for now.                                         | `2025-07-23`                         |
| `storage_conditions`       | Description of how the sample was stored (e.g., -80°C, RNAlater).                                 | `-80C, no preservative`              |
| `project_id`               | Study/project the sample belongs to. Defaults to `PROTECT`, but supports future entries.          | `PROTECT`                            |
| `sequencing_platform`      | Technology used for sequencing (e.g., Illumina).                                                  | `Illumina`                           |
| `read_length`              | Sequencing read length and layout.                                                                | `PE 100 bp`                          |
| `adapter_sequence`         | Adapter used in library prep. Optional.                                                           | `AGATCGGAAGAGCACACGTCTGAACTCCAGTCAC` |
| `rRNA_depletion_protocol`  | Method used to deplete rRNA. Structured, searchable field.                                        | `Ribo-Zero`                          |
| `host_depletion_method`    | Method used to remove host (e.g., human) DNA or RNA. Structured field.                            | `saponin lysis`                      |
| `submitted_by`             | Name or lab submitting the sample.                                                                | `Zengler Lab`                        |
| `processing_protocol`      | Narrative description of processing steps. Can link to protocols.io.                              | `RNA extraction and rRNA removal...`|
| `file_type`                | Type of file associated with the sample.                                                          | `fastq`                              |
| `data_type`                | Omics type for this sample (e.g., metaG, metaT, metaRS).                                          | `metaG`                              |

---

## 🛠️ Notes

- `adapter_sequence`: Optional. Populate only if non-standard adapter sequences were used or if relevant to analysis.
- `rRNA_depletion_protocol` and `host_depletion_method` should use **controlled vocabularies** to ensure consistency and filterability.
- `project_id`: Defaults to `PROTECT`, but future datasets may use other identifiers (e.g., `CAMP`, `ZENG2026`).
- `collection_date` and `subject_id` may be PHI-sensitive. Retained in full for internal use; masking or removal may be required before public release.
- This metadata template is intended for internal ASMA data integration. External versions may require redaction or transformation of certain fields.

---

## 🔗 Related Resources

- [ASMA Project Overview (UCB internal)](https://your.internal.link)
- [Protocols.io](https://www.protocols.io/)

---

## 📤 Contributions

This template was developed by the ASMA Data Integration Team in collaboration with the Zengler Lab.  
For feedback or contributions, please reach out to the ASMA metadata curation team.
