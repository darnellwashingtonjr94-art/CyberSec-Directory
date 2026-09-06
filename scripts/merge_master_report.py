import json
import csv
from pathlib import Path

def generate_merged_csv():
    base = Path(__file__).parent.parent
    
    with open(base / "data" / "institutions.json", 'r') as f:
        institutions = {inst['id']: inst for inst in json.load(f)}
        
    merged_data = []
    with open(base / "data" / "metrics.csv", 'r') as f:
        for row in csv.DictReader(f):
            inst_id = row['inst_id']
            if inst_id in institutions:
                combined = {**institutions[inst_id], **row}
                merged_data.append(combined)
                
    if not merged_data:
        print("No intersecting data found.")
        return

    output_path = base / "docs" / "master_report.csv"
    headers = list(merged_data[0].keys())
    
    with open(output_path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(merged_data)
        
    print(f"Master CSV report generated at {output_path.name}")

if __name__ == "__main__":
    generate_merged_csv()
