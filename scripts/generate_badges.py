from pathlib import Path
import json

SVG_TEMPLATE = """<svg xmlns="http://www.w3.org/2000/svg" width="120" height="20">
    <rect width="60" height="20" fill="#555"/>
    <rect x="60" width="60" height="20" fill="{color}"/>
    <text x="30" y="14" fill="#fff" text-anchor="middle" font-family="Arial" font-size="11">{label}</text>
    <text x="90" y="14" fill="#fff" text-anchor="middle" font-family="Arial" font-size="11">{value}</text>
</svg>"""

def create_badge(label, value, color, output_path):
    svg = SVG_TEMPLATE.format(label=label, value=value, color=color)
    output_path.write_text(svg)

if __name__ == "__main__":
    base = Path(__file__).parent.parent
    with open(base / "data" / "institutions.json", 'r') as f:
        count = len(json.load(f))
        
    create_badge("Entities", str(count), "#4c1", base / "docs" / "entities_badge.svg")
    print("Generated entities_badge.svg")
