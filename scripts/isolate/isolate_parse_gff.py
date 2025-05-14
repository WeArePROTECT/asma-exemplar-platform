# isolate_parse_gff.py
import os
import pandas as pd

base_dir = "/app/data/asma_exemplar_data/raw/isolates"
out_path = "/app/data/asma_exemplar_data/processed/isolates/gff_summary.csv"

records = []

for isolate_id in os.listdir(base_dir):
    gff_path = os.path.join(base_dir, isolate_id, "annotation", f"{isolate_id}.gff")
    if not os.path.exists(gff_path):
        continue

    counts = {
        "CDS": 0,
        "tRNA": 0,
        "rRNA": 0,
        "pseudogene": 0,
        "other_features": 0
    }

    with open(gff_path, "r") as f:
        for line in f:
            if line.startswith("#") or "\t" not in line:
                continue
            parts = line.strip().split("\t")
            if len(parts) < 3:
                continue
            feature_type = parts[2]
            if feature_type in counts:
                counts[feature_type] += 1
            else:
                counts["other_features"] += 1

    counts["isolate_id"] = isolate_id
    records.append(counts)

pd.DataFrame(records)[["isolate_id", "CDS", "tRNA", "rRNA", "pseudogene", "other_features"]].to_csv(out_path, index=False)
print(f"✅ .gff summaries saved to '{out_path}'")