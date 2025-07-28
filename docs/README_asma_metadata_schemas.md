# 🧬 ASMA Metadata Schemas

This directory contains standardized schema definitions for all metadata templates submitted to the **ASMA (Airway Synthetic Microbial Atlas)** project. These schemas support structured ingestion into the **KBase Delta Lakehouse**, enable reproducible data processing, and ensure consistency across contributing research teams.

---

## 📁 Contents

Each metadata file has two accompanying schema definitions:
- **SQL Schema** – for relational databases and general tabular structure
- **Delta Table Schema** – for Spark/Databricks-based pipelines using PySpark's `StructType`

| Metadata Template | SQL Schema | Delta Table Schema |
|-------------------|------------|--------------------|
| `conrad_lab_metadata_template.csv` | ✅ [`conrad_lab_metadata_sql_schema.sql`](./conrad_lab_metadata_sql_schema.sql) | ✅ [`conrad_lab_metadata_delta_schema.py`](./conrad_lab_metadata_delta_schema.py) |
| `zengler_lab_additional_core_metadata_template.csv` | ✅ [`zengler_additional_core_sql_schema.sql`](./zengler_additional_core_sql_schema.sql) | ✅ [`zengler_additional_core_delta_schema.py`](./zengler_additional_core_delta_schema.py) |
| `zengler_lab_metag_metadata_template.csv` | ✅ [`zengler_metag_sql_schema.sql`](./zengler_metag_sql_schema.sql) | ✅ [`zengler_metag_delta_schema.py`](./zengler_metag_delta_schema.py) |
| `zengler_lab_metars_metadata_template.csv` | ✅ [`zengler_metars_sql_schema.sql`](./zengler_metars_sql_schema.sql) | ✅ [`zengler_metars_delta_schema.py`](./zengler_metars_delta_schema.py) |
| `zengler_lab_metat_metadata_template.csv` | ✅ [`zengler_metat_sql_schema.sql`](./zengler_metat_sql_schema.sql) | ✅ [`zengler_metat_delta_schema.py`](./zengler_metat_delta_schema.py) |
| `zengler_lab_sra_metadata_template.csv` | ✅ [`zengler_sra_sql_schema.sql`](./zengler_sra_sql_schema.sql) | ✅ [`zengler_sra_delta_schema.py`](./zengler_sra_delta_schema.py) |

---

## 📘 Unified Metadata Dictionary

A human-readable dictionary that lists all columns and their inferred data types across each metadata file is available here:

👉 [`unified_metadata_dictionary.md`](./unified_metadata_dictionary.md)

---

## ⚠️ Note on Conrad Lab Metadata

The **Conrad Lab metadata schema** is a preliminary draft.  
While we have defined expected column names and potential field types, **actual outputs for each entry cannot be confirmed** until we receive the first exemplar data submission.

> 🔄 This schema **will be updated** once finalized metadata is delivered from the Conrad team and reviewed.

---

## 🧩 Integration Plans

These schemas will serve as the foundation for:
- Validating incoming metadata from collaborators
- Building ingest pipelines for KBase and Delta Lakehouse
- Supporting long-term interoperability across ASMA datasets

---

## 📬 Questions or Updates?

Please contact the ASMA data science team or open an issue in this repository if updates are needed or if your lab plans to submit new metadata formats.

