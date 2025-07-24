
# ASMA Project - Zengler Lab MetaT-Specific Metadata Template

This repository contains the standardized **metaT-specific metadata** for Zengler Lab contributions to the **ASMA** (Airway Synthetic Microbial Atlas) project.

The file [`zengler_lab_metat_metadata_template.csv`](./zengler_lab_metat_metadata_template.csv) captures information specific to the **metatranscriptomics (metaT)** workflow, including RNA extraction, library preparation, and quality-related metadata.

This metadata supports:
- Internal ASMA platform integration
- Downstream reproducibility and documentation
- Transparency in how raw metatranscriptomic data were generated

---

## 📁 File Overview

- **Filename**: `zengler_lab_metat_metadata_template.csv`
- **Each row = one metaT protocol instance**
- Structured for per-sample or per-batch metadata, depending on lab processing
- Designed to complement sample-level metadata in other ASMA templates

---

## 🧬 Metadata Field Dictionary

| Column Name                  | Description                                                                 | Example Value                         | Required?  |
|------------------------------|-----------------------------------------------------------------------------|---------------------------------------|------------|
| `rna_extraction_kit`         | Name of the kit or method used for RNA extraction                          | `Qiagen RNeasy Micro Kit`             | Yes        |
| `input_sample_vol`           | Volume of biological material used for RNA extraction (include units)      | `100 µL`                              | Yes        |
| `depth_target`               | Target sequencing depth for the sample or run                              | `20 million reads`                    | Yes        |
| `rrna_depletion_kit`         | Name of the rRNA depletion kit or method used                              | `Ribo-Zero Plus`                      | Yes        |
| `library_preparation_protocol` | Library prep protocol or kit used for cDNA synthesis                     | `NEBNext Ultra II RNA Library Prep`   | Yes        |
| `cdna_conversion_method`     | Reverse transcription method or kit                                        | `SuperScript IV`                      | Optional   |
| `strand_specific`            | Whether library prep preserves strand orientation                          | `Yes` or `No`                         | Optional   |
| `fragment_size`              | Average size (in bp) of cDNA fragments post-shearing                       | `300`                                 | Optional   |
| `rRNA_content_percent`       | Percent of reads mapping to rRNA after depletion (QC metric)               | `2.5`                                 | Optional   |
| `mapping_rate_to_db`         | Percent of reads successfully mapping to reference databases (QC metric)   | `85.4`                                | Optional   |

---

## 🛠️ Notes

- Fields marked **Optional** are not required for submission but are useful for troubleshooting or downstream interpretation.
- If values are not applicable or unknown, use `"NA"` or leave blank with explanation.
- `rRNA_content_percent` and `mapping_rate_to_db` are downstream quality control metrics and can be populated after sequencing, if available.

---

## 🔗 Related Resources

- [ASMA Project Overview (UCB internal)](https://your.internal.link)

---

## 📤 Contributions

This metadata format was developed by the ASMA Data Integration Team in collaboration with the Zengler Lab.  
Please contact the ASMA metadata team for suggestions, revisions, or questions.
