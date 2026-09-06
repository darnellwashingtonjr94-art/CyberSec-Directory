import json
import csv
from pathlib import Path
from datetime import datetime

def generate_markdown_report(institutions_path, metrics_path, output_path):
    report_content = [
        "# Cybersecurity Evaluation Report",
        f"*Generated on: {datetime.now().strftime('%Y-%m-%d')}*\n",
        "## Monitored Institutions"
    ]
    
    try:
        # Parse Institutions
        with open(institutions_path, 'r', encoding='utf-8') as f:
            institutions = json.load(f)
            report_content.append(f"Total institutions evaluated: **{len(institutions)}**\n")
            
        # Parse Metrics
        report_content.append("## Key Metrics Summary")
        with open(metrics_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
            report_content.append(f"Total data points processed: **{len(rows)}**\n")
            
        # Write Output
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(report_content))
            
        print(f"✅ Report successfully generated at {output_path.relative_to(output_path.parent.parent)}")
        
    except Exception as e:
        print(f"❌ Failed to generate report: {e}")

if __name__ == "__main__":
    base_dir = Path(__file__).parent.parent
    data_dir = base_dir / "data"
    docs_dir = base_dir / "docs"
    
    generate_markdown_report(
        data_dir / "institutions.json",
        data_dir / "metrics.csv",
        docs_dir / "evaluation-report.md"
    )
