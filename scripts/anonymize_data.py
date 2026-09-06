import json
from pathlib import Path

def anonymize_dataset(input_path, output_path):
    safe_data = []
    keys_to_remove = ['contact_email', 'admin_phone', 'internal_notes', 'ip_range']
    
    with open(input_path, 'r') as f:
        data = json.load(f)
        
    for entry in data:
        safe_entry = {k: v for k, v in entry.items() if k not in keys_to_remove}
        safe_data.append(safe_entry)
        
    with open(output_path, 'w') as f:
        json.dump(safe_data, f, indent=2)
    print(f"Anonymized data written to {output_path.name}")

if __name__ == "__main__":
    base = Path(__file__).parent.parent / "data"
    anonymize_dataset(base / "institutions.json", base / "institutions_public.json")
