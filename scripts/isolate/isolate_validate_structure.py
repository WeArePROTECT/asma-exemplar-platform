# isolate_validate_structure.py
import os
import yaml
import pandas as pd

# Base directory containing isolate folders
base_dir = "/app/data/asma_exemplar_data/raw/isolates"

# Required subfolders and expected file suffixes
required_structure = {
    "raw_reads": ["_R1.fastq.gz", "_R2.fastq.gz"],
    "assembly": [".fna"],
    "annotation": [".gff", ".faa"],
    "quality": ["BUSCO_short_summary.txt"],
    "amr": [".tsv"],
    "vf": [".tsv"],
}

summary = []

for isolate_id in os.listdir(base_dir):
    isolate_path = os.path.join(base_dir, isolate_id)
    if not os.path.isdir(isolate_path):
        continue

    metadata_file = os.path.join(isolate_path, "metadata.yaml")
    if not os.path.exists(metadata_file):
        continue

    with open(metadata_file, "r") as f:
        metadata = yaml.safe_load(f)

    isolate_report = {
        "isolate_id": isolate_id,
        "submitter": metadata.get("submitter", "unknown"),
        "status": "OK",
        "missing": []
    }

    for subfolder, expected_suffixes in required_structure.items():
        subdir = os.path.join(isolate_path, subfolder)
        if not os.path.exists(subdir):
            isolate_report["status"] = "Missing subfolder"
            isolate_report["missing"].append(subfolder)
            continue

        present_suffixes = []
        for f in os.listdir(subdir):
            present_suffixes.extend([suf for suf in expected_suffixes if f.endswith(suf)])

        if len(set(expected_suffixes) - set(present_suffixes)) > 0:
            isolate_report["status"] = "Missing files"
            isolate_report["missing"].append(f"{subfolder}: {set(expected_suffixes) - set(present_suffixes)}")

    summary.append(isolate_report)

# Convert to DataFrame and save
out_path = "/app/data/asma_exemplar_data/processed/isolates/isolate_qc_summary.csv"
df = pd.DataFrame(summary)
df.to_csv(out_path, index=False)
print(f"✅ Validation complete. Summary saved to '{out_path}'")

