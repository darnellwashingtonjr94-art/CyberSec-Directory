import csv
from pathlib import Path

def get_grade(score):
    try:
        score = int(score)
        if score >= 90: return 'A'
        if score >= 80: return 'B'
        if score >= 70: return 'C'
        if score >= 60: return 'D'
        return 'F'
    except ValueError:
        return 'N/A'

if __name__ == "__main__":
    base = Path(__file__).parent.parent
    input_csv = base / "data" / "metrics.csv"
    output_csv = base / "docs" / "grades.csv"
    
    with open(input_csv, 'r') as fin, open(output_csv, 'w', newline='') as fout:
        reader = csv.DictReader(fin)
        writer = csv.DictWriter(fout, fieldnames=reader.fieldnames + ['grade'])
        writer.writeheader()
        
        for row in reader:
            row['grade'] = get_grade(row.get('score', 0))
            writer.writerow(row)
            
    print(f"✅ Generated letter grades at {output_csv.name}")
