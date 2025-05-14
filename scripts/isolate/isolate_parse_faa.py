# isolate_parse_faa.py
from Bio import SeqIO
import os
import pandas as pd

base_dir = "/app/data/asma_exemplar_data/raw/isolates"
out_path = "/app/data/asma_exemplar_data/processed/isolates/faa_summary.csv"

records = []

for isolate_id in os.listdir(base_dir):
    faa_path = os.path.join(base_dir, isolate_id, "annotation", f"{isolate_id}.faa")
    if not os.path.exists(faa_path):
        continue

    protein_lengths = []
    for record in SeqIO.parse(faa_path, "fasta"):
        length = len(record.seq)
        protein_lengths.append(length)

    if not protein_lengths:
        continue

    total_proteins = len(protein_lengths)
    total_aa = sum(protein_lengths)
    avg_length = round(total_aa / total_proteins, 2)
    short_proteins = sum(1 for l in protein_lengths if l < 50)

    records.append({
        "isolate_id": isolate_id,
        "Total Proteins": total_proteins,
        "Total Amino Acids": total_aa,
        "Average Protein Length": avg_length,
        "Short Proteins (<50 aa)": short_proteins
    })

pd.DataFrame(records).to_csv(out_path, index=False)
print(f"✅ .faa summaries saved to '{out_path}'")
