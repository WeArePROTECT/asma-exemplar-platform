#!/usr/bin/env python3
import os
import re
import subprocess
import json
import argparse
import pandas as pd

# === Command-line arguments ===
parser = argparse.ArgumentParser(description="Run full metaG QC pipeline with optional skip of FastQC/MultiQC.")
parser.add_argument("input_dir", help="Path to directory containing FASTQ files.")
parser.add_argument("--skip-qc", action="store_true", help="Skip renaming, FastQC, and MultiQC")
args = parser.parse_args()

os.chdir(args.input_dir)
data_dir = os.getcwd()

qc_dir = "qc"
multiqc_dir = "qc_summary"
os.makedirs(qc_dir, exist_ok=True)
os.makedirs(multiqc_dir, exist_ok=True)

# === Optional: Rename + run FastQC and MultiQC ===
if not args.skip_qc:
    standard_pattern = re.compile(r"^PRO\d+_metaG\.fastq\.gz$")
    extract_pattern = re.compile(r"^(PRO\d+)[A-Z]*_metaG.*\.fq.*\.gz$")

    for fname in os.listdir(data_dir):
        if not fname.endswith(".gz"):
            continue
        full_path = os.path.join(data_dir, fname)
        if os.path.isdir(full_path) or standard_pattern.match(fname):
            continue
        match = extract_pattern.match(fname)
        if match:
            sample_id = match.group(1)
            new_fname = f"{sample_id}_metaG.fastq.gz"
            os.rename(full_path, os.path.join(data_dir, new_fname))
            print(f"Renamed: {fname} → {new_fname}")

    print("\nRunning FastQC...")
    fq_files = [f for f in os.listdir(data_dir) if f.endswith(".fastq.gz")]
    for f in fq_files:
        subprocess.run(["fastqc", f, "-o", qc_dir], check=True)

    print("Running MultiQC...")
    subprocess.run(["multiqc", qc_dir, "-o", multiqc_dir], check=True)
else:
    print("⚠️ Skipping file renaming, FastQC, and MultiQC (--skip-qc used)")

# === Parse MultiQC metrics from 'lines' data ===
multiqc_data_file = os.path.join(multiqc_dir, "multiqc_data", "multiqc_data.json")
if not os.path.exists(multiqc_data_file):
    print("❌ MultiQC JSON not found.")
    exit(1)

with open(multiqc_data_file, "r") as f:
    multiqc = json.load(f)

quality_lines = multiqc["report_plot_data"]["fastqc_per_base_sequence_quality_plot"]["datasets"][0]["lines"]
adapter_lines = multiqc["report_plot_data"]["fastqc_adapter_content_plot"]["datasets"][0]["lines"]
length_lines = multiqc["report_plot_data"]["fastqc_sequence_length_distribution_plot"]["datasets"][0]["lines"]

summary = {}

# Extract metrics
for q in quality_lines:
    if "name" in q and "pairs" in q:
        values = sorted(p[1] for p in q["pairs"])
        summary[q["name"]] = {"Median_QScore": round(values[len(values)//2], 2) if values else 0}

for a in adapter_lines:
    if "name" in a and "pairs" in a:
        max_adapter = max(p[1] for p in a["pairs"])
        summary.setdefault(a["name"], {})["Max_Adapter_Content(%)"] = round(max_adapter, 2)

for l in length_lines:
    if "name" in l and "pairs" in l:
        total_reads = sum(p[1] for p in l["pairs"])
        total_bases = sum(p[0] * p[1] for p in l["pairs"])
        avg_len = total_bases / total_reads if total_reads else 0
        summary.setdefault(l["name"], {})["Avg_Read_Length"] = round(avg_len, 2)

# === Apply thresholds and write QC summary ===
thresholds = {
    "quality": 30,
    "adapter": 5.0,
    "length": 85,
}

results = []
for sample, metrics in summary.items():
    if " - polyg" in sample:
        continue

    q = metrics.get("Median_QScore", 0)
    a = metrics.get("Max_Adapter_Content(%)", 0)
    l = metrics.get("Avg_Read_Length", 0)

    result = {
        "sample_id": sample,
        "median_quality": q,
        "max_adapter_pct": a,
        "avg_read_length": l,
        "pass_quality": q >= thresholds["quality"],
        "pass_adapters": a <= thresholds["adapter"],
        "pass_length": l >= thresholds["length"],
    }
    result["overall_pass"] = all([result["pass_quality"], result["pass_adapters"], result["pass_length"]])
    results.append(result)

df = pd.DataFrame(results)
df.to_csv("qc_flags.csv", index=False)
print("\n✅ QC results written to qc_flags.csv")
