# run_exemplar_pipeline.py
import argparse
import subprocess
import os

def run_pipeline(data_type, input_path):
    script_map = {
        "isolates": "/app/scripts/isolate/run_isolate_pipeline.py",
        "metag": "/app/scripts/metag/run_metag_pipeline.py",
        "mag": "/app/scripts/mag/run_mag_pipeline.py",
        "metat": "/app/scripts/metat/run_metat_pipeline.py"
    }

    if data_type not in script_map:
        print(f"❌ Unsupported data type: {data_type}")
        print("Supported types are: isolates, metag, mag, metat")
        return

    script = script_map[data_type]
    if not os.path.exists(script):
        print(f"❌ Script not found: {script}")
        return

    print(f"🚀 Dispatching {data_type} pipeline for {input_path}")
    subprocess.run(["python", script, "--input", input_path], check=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run exemplar data pipeline by type")
    parser.add_argument("--type", required=True, help="Data type: isolates, metag, mag, metat")
    parser.add_argument("--input", required=True, help="Path to raw data folder")
    args = parser.parse_args()
    run_pipeline(args.type, args.input)
