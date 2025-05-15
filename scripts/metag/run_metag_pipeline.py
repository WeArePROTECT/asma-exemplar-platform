import argparse
import subprocess

def main():
    parser = argparse.ArgumentParser(description="Run metaG pipeline on a directory of FASTQ files")
    parser.add_argument("--input", required=True, help="Path to metaG fastq files")
    args = parser.parse_args()

    subprocess.run(["python3", "metag_full_qc_pipeline.py", args.input], check=True, cwd="/app/scripts/metag")

if __name__ == "__main__":
    main()