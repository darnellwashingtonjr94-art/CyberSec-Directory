import csv
from pathlib import Path

def draw_chart():
    data_path = Path(__file__).parent.parent / "data" / "metrics.csv"
    bins = {'90-100': 0, '80-89': 0, '70-79': 0, '60-69': 0, '0-59': 0}
    
    with open(data_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            score = int(row['score'])
            if score >= 90: bins['90-100'] += 1
            elif score >= 80: bins['80-89'] += 1
            elif score >= 70: bins['70-79'] += 1
            elif score >= 60: bins['60-69'] += 1
            else: bins['0-59'] += 1
            
    print("Score Distribution:")
    for label, count in bins.items():
        bar = '█' * count
        print(f"{label:>7} | {bar} ({count})")

if __name__ == "__main__":
    draw_chart()
