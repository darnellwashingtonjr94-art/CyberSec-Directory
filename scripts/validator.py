import json
import csv
import sys
from pathlib import Path

def validate_json(filepath):
    if not filepath.exists():
        print(f"⚠️ Skipping {filepath.name}: File does not exist.")
        return True
        
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if not isinstance(data, list):
            raise ValueError("JSON root must be a list of institutions.")
        print(f"✅ {filepath.name} is valid JSON with {len(data)} entries.")
        return True
    except Exception as e:
        print(f"❌ Error validating {filepath.name}: {e}")
        return False

def validate_csv(filepath):
    if not filepath.exists():
        print(f"⚠️ Skipping {filepath.name}: File does not exist.")
        return True
        
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            headers = next(reader)
        if not headers:
            raise ValueError("CSV is missing headers.")
        print(f"✅ {filepath.name} is valid CSV with columns: {', '.join(headers)}")
        return True
    except Exception as e:
        print(f"❌ Error validating {filepath.name}: {e}")
        return False

if __name__ == "__main__":
    # .resolve() ensures absolute path resolution regardless of where the script is run from
    data_dir = Path(__file__).resolve().parent.parent / "data"

    if not data_dir.exists():
        print("Data directory not found. Skipping validation to prevent crash.")
        sys.exit(0)

    json_valid = validate_json(data_dir / "institutions.json")
    csv_valid = validate_csv(data_dir / "metrics.csv")

    if not (json_valid and csv_valid):
        print("Build failed: Data validation errors detected.")
        sys.exit(1)
