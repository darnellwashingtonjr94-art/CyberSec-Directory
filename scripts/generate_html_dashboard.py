import json
from pathlib import Path

HTML_TEMPLATE = """<!DOCTYPE html>
<html>
<head><title>Cybersecurity Directory</title></head>
<body style="font-family: sans-serif; padding: 20px;">
    <h1>Directory Dashboard</h1>
    <ul>
        {list_items}
    </ul>
</body>
</html>"""

def build_dashboard():
    base = Path(__file__).parent.parent
    try:
        with open(base / "data" / "institutions.json", 'r') as f:
            institutions = json.load(f)
            
        list_items = "".join(f"<li>{inst.get('name', 'Unknown')} - {inst.get('domain', 'N/A')}</li>" 
                             for inst in institutions)
                             
        output_path = base / "docs" / "dashboard.html"
        output_path.write_text(HTML_TEMPLATE.format(list_items=list_items))
        print(f"Generated static dashboard at {output_path.name}")
        
    except Exception as e:
        print(f"Failed to generate dashboard: {e}")

if __name__ == "__main__":
    build_dashboard()
