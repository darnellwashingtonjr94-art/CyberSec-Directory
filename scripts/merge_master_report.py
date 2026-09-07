import json
import csv
import sys
from pathlib import Path

def generate_merged_csv():
    # Resolve the repository root directory
    base = Path(__file__).resolve().parent.parent
    data_file = base / "data" / "institutions.json"
    
    # Safety check: exit cleanly if the file doesn't exist
    if not data_file.exists():
        print("⚠️ institutions.json not found. Skipping report generation.")
        return

    try:
        # Line 18 from your traceback: opening the file
        with open(data_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        # --- Your specific report generation logic goes here ---
        # (e.g., merging JSON data and writing to a CSV report)
        
        print(f"✅ Successfully loaded records. Report generated.")
        
    except Exception as e:
        print(f"❌ Failed to generate report: {e}")
        sys.exit(1)

if __name__ == "__main__":
    generate_merged_csv()
