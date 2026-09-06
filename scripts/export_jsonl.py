import json
from pathlib import Path

def export_to_jsonl(input_path, output_path):
    try:
        with open(input_path, 'r') as f_in, open(output_path, 'w') as f_out:
            data = json.load(f_in)
            for entry in data:
                f_out.write(json.dumps(entry) + '\n')
        print(f"✅ Exported JSON Lines to {output_path.name}")
    except Exception as e:
        print(f"❌ Failed to export JSONL: {e}")

if __name__ == "__main__":
    base = Path(__file__).parent.parent / "data"
    export_to_jsonl(base / "institutions.json", base / "institutions.jsonl")
