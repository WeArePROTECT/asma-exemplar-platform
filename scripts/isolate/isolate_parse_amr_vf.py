# isolate_parse_amr_vf.py
import os
import pandas as pd

base_dir = "/app/data/asma_exemplar_data/raw/isolates"
processed_dir = "/app/data/asma_exemplar_data/processed/isolates"

def parse_amr():
    all_genes = set()
    gene_maps = {}

    for isolate_id in os.listdir(base_dir):
        tsv_path = os.path.join(base_dir, isolate_id, "amr", f"{isolate_id}_amr.tsv")
        if not os.path.exists(tsv_path):
            continue
        try:
            df = pd.read_csv(tsv_path, sep="\t")
            if "Element symbol" not in df.columns:
                continue
            genes = set(df["Element symbol"].dropna().astype(str))
            gene_maps[isolate_id] = genes
            all_genes.update(genes)
        except:
            continue

    all_genes = sorted(all_genes)
    matrix = []
    for isolate_id, genes in gene_maps.items():
        row = {"isolate_id": isolate_id}
        for gene in all_genes:
            row[gene] = 1 if gene in genes else 0
        matrix.append(row)

    pd.DataFrame(matrix).to_csv(f"{processed_dir}/amr_matrix.csv", index=False)
    print("✅ AMR matrix saved.")

def parse_vf():
    all_genes = set()
    gene_maps = {}

    for isolate_id in os.listdir(base_dir):
        tsv_path = os.path.join(base_dir, isolate_id, "vf", f"{isolate_id}_vf.tsv")
        if not os.path.exists(tsv_path):
            continue
        try:
            df = pd.read_csv(tsv_path, sep="\t", header=None)
            df["Gene ID"] = df[1].str.extract(r"^([^\(]+)")
            genes = set(df["Gene ID"].dropna().astype(str))
            gene_maps[isolate_id] = genes
            all_genes.update(genes)
        except:
            continue

    all_genes = sorted(all_genes)
    matrix = []
    for isolate_id, genes in gene_maps.items():
        row = {"isolate_id": isolate_id}
        for gene in all_genes:
            row[gene] = 1 if gene in genes else 0
        matrix.append(row)

    pd.DataFrame(matrix).to_csv(f"{processed_dir}/vf_matrix.csv", index=False)
    print("✅ VF matrix saved.")

parse_amr()
parse_vf()
