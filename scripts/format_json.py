import json
from pathlib import Path

def format_json_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        # Sort items by 'id' if present, otherwise by 'name'
        data.sort(key=lambda x: x.get('id', x.get('name', '')))
        
        with open(filepath, 'w', encoding='utf-8') as f:
            # sort_keys=True alphabetizes the keys within each dictionary
            json.dump(data, f, indent=2, sort_keys=True)
            f.write('\n')
            
        print(f"✅ Formatted {filepath.name}")
    except Exception as e:
        print(f"❌ Failed to format JSON: {e}")

if __name__ == "__main__":
    data_path = Path(__file__).parent.parent / "data" / "institutions.json"
    format_json_file(data_path)
