# isolate_build_summary.py
import os
import pandas as pd

base_dir = "/app/data/asma_exemplar_data/processed/isolates"

files = {
    "qc": "isolate_qc_summary.csv",
    "busco": "busco_summary.csv",
    "faa": "faa_summary.csv",
    "gff": "gff_summary.csv",
    "amr": "amr_matrix.csv",
    "vf": "vf_matrix.csv"
}

# Load each file
dfs = {}
for key, fname in files.items():
    fpath = os.path.join(base_dir, fname)
    if os.path.exists(fpath):
        dfs[key] = pd.read_csv(fpath)
    else:
        print(f"[WARNING] Missing file: {fname}")

# Merge starting from QC summary
if "qc" not in dfs:
    raise FileNotFoundError("Missing isolate_qc_summary.csv — cannot build master summary.")

master = dfs["qc"]
for key in ["busco", "faa", "gff", "amr", "vf"]:
    if key in dfs:
        master = master.merge(dfs[key], on="isolate_id", how="left")

# Derived columns
if "amr" in dfs:
    amr_cols = dfs["amr"].columns.drop("isolate_id", errors='ignore')
    master["num_amr_genes"] = dfs["amr"][amr_cols].sum(axis=1)

if "vf" in dfs:
    vf_cols = dfs["vf"].columns.drop("isolate_id", errors='ignore')
    master["num_vf_genes"] = dfs["vf"][vf_cols].sum(axis=1)

if "faa" in dfs and "Short Proteins (<50 aa)" in dfs["faa"].columns:
    master["many_short_proteins"] = master["Short Proteins (<50 aa)"] > 100

# Save full summary
master_out = os.path.join(base_dir, "isolate_master_summary.csv")
master.to_csv(master_out, index=False)
print(f"✅ Master isolate summary saved to: {master_out}")

# Save report summary
report_cols = [
    "isolate_id", "submitter", "status", "Complete (%)", "Missing (%)",
    "CDS", "tRNA", "rRNA", "Total Proteins", "Average Protein Length",
    "num_amr_genes", "num_vf_genes", "many_short_proteins"
]
report = master[[col for col in report_cols if col in master.columns]]
report_out = os.path.join(base_dir, "isolate_report_summary.csv")
report.to_csv(report_out, index=False)
print(f"📄 Report-friendly isolate summary saved to: {report_out}")
