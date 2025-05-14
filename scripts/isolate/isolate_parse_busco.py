# isolate_parse_busco.py
import os
import re
import pandas as pd

base_dir = "/app/data/asma_exemplar_data/raw/isolates"
out_path = "/app/data/asma_exemplar_data/processed/isolates/busco_summary.csv"

records = []

for isolate_id in os.listdir(base_dir):
    busco_path = os.path.join(base_dir, isolate_id, "quality", "BUSCO_short_summary.txt")
    if not os.path.exists(busco_path):
        continue

    with open(busco_path, "r") as f:
        text = f.read()

    record = {"isolate_id": isolate_id}

    match = re.search(r'C:(\d+\.\d+)%\[S:(\d+\.\d+)%,D:(\d+\.\d+)%\],F:(\d+\.\d+)%.*,M:(\d+\.\d+)%.*,n:(\d+)', text)
    if match:
        record.update({
            "Complete (%)": float(match.group(1)),
            "Single (%)": float(match.group(2)),
            "Duplicated (%)": float(match.group(3)),
            "Fragmented (%)": float(match.group(4)),
            "Missing (%)": float(match.group(5)),
            "Total BUSCOs": int(match.group(6))
        })

    scaffold_match = re.search(r'(\d+)\s+Number of scaffolds', text)
    contig_match = re.search(r'(\d+)\s+Number of contigs', text)
    length_match = re.search(r'(\d+)\s+Total length', text)
    gap_match = re.search(r'([\d\.]+%)\s+Percent gaps', text)
    scaffold_n50_match = re.search(r'(\d+)\s+KB\s+Scaffold N50', text)
    contig_n50_match = re.search(r'(\d+)\s+KB\s+Contigs N50', text)

    record["Scaffolds"] = int(scaffold_match.group(1)) if scaffold_match else None
    record["Contigs"] = int(contig_match.group(1)) if contig_match else None
    record["Genome Length (bp)"] = int(length_match.group(1)) if length_match else None
    record["Gap %"] = gap_match.group(1) if gap_match else None
    record["Scaffold N50 (kb)"] = int(scaffold_n50_match.group(1)) if scaffold_n50_match else None
    record["Contig N50 (kb)"] = int(contig_n50_match.group(1)) if contig_n50_match else None

    records.append(record)

pd.DataFrame(records).to_csv(out_path, index=False)
print(f"✅ BUSCO + Assembly summaries saved to '{out_path}'")