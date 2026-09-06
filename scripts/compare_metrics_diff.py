import csv
import sys
from pathlib import Path

def load_metrics(filepath):
    metrics = {}
    with open(filepath, 'r') as f:
        for row in csv.DictReader(f):
            metrics[row['inst_id']] = int(row['score'])
    return metrics

if __name__ == "__main__":
    base = Path(__file__).parent.parent
    current_file = base / "data" / "metrics.csv"
    
    # Assuming latest backup is passed as an argument or found in backups dir
    # For this script, we'll look for a dummy 'metrics_old.csv'
    old_file = base / "backups" / "metrics_old.csv"
    
    if not old_file.exists():
        print("No previous backup found to compare against.")
        sys.exit(0)
        
    current_metrics = load_metrics(current_file)
    old_metrics = load_metrics(old_file)
    
    print("📈 Score Changes:")
    for inst_id, current_score in current_metrics.items():
        if inst_id in old_metrics:
            diff = current_score - old_metrics[inst_id]
            if diff > 0:
                print(f"  🟢 {inst_id}: +{diff} (Now {current_score})")
            elif diff < 0:
                print(f"  🔴 {inst_id}: {diff} (Now {current_score})")
