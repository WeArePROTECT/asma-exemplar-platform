# run_isolate_pipeline.py
import os
import argparse
import subprocess
from datetime import datetime

def is_isolate_folder(path):
    return os.path.isdir(path) and not path.endswith(".csv")

def run_pipeline_for_isolate(isolate_path):
    isolate_id = os.path.basename(isolate_path)
    print(f"\n🚀 Running pipeline for {isolate_id}")
    isolate_scripts_path = "/app/scripts/isolate"
    try:
        subprocess.run(["python", "isolate_validate_structure.py"], check=True, cwd=isolate_scripts_path)
        subprocess.run(["python", "isolate_parse_busco.py"], check=True, cwd=isolate_scripts_path)
        subprocess.run(["python", "isolate_parse_faa.py"], check=True, cwd=isolate_scripts_path)
        subprocess.run(["python", "isolate_parse_gff.py"], check=True, cwd=isolate_scripts_path)
        subprocess.run(["python", "isolate_parse_amr_vf.py"], check=True, cwd=isolate_scripts_path)
        subprocess.run(["python", "isolate_build_summary.py"], check=True, cwd=isolate_scripts_path)
        print(f"✅ Completed: {isolate_id}")
        return isolate_id, "OK"
    except subprocess.CalledProcessError as e:
        print(f"❌ Error processing {isolate_id}: {e}")
        return isolate_id, "ERROR"

def main(base_dir):
    log = []
    for item in os.listdir(base_dir):
        full_path = os.path.join(base_dir, item)
        if is_isolate_folder(full_path):
            result = run_pipeline_for_isolate(full_path)
            log.append(result)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = os.path.join("/app/data/asma_exemplar_data/processed/isolates", f"isolate_pipeline_log_{timestamp}.csv")
    with open(log_file, "w") as f:
        f.write("isolate_id,status\n")
        for row in log:
            f.write(f"{row[0]},{row[1]}\n")

    print(f"\n📄 Pipeline run log saved to: {log_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run full isolate QC pipeline")
    parser.add_argument("--input", required=True, help="Path to isolates folder")
    args = parser.parse_args()
    main(args.input)