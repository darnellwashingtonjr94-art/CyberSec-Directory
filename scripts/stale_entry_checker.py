import json
import csv
from datetime import datetime
from pathlib import Path

def find_stale_audits(days_threshold=90):
    base = Path(__file__).parent.parent / "data"
    
    # Load institutions
    with open(base / "institutions.json", 'r') as f:
        institutions = {inst['id']: inst['name'] for inst in json.load(f)}
        
    # Track latest audit per institution
    latest_audits = {}
    with open(base / "metrics.csv", 'r') as f:
        for row in csv.DictReader(f):
            inst_id = row['inst_id']
            audit_date = datetime.strptime(row['audit_date'], '%Y-%m-%d')
            
            if inst_id not in latest_audits or audit_date > latest_audits[inst_id]:
                latest_audits[inst_id] = audit_date
                
    # Evaluate staleness
    now = datetime.now()
    stale_count = 0
    
    for inst_id, name in institutions.items():
        last_audit = latest_audits.get(inst_id)
        if not last_audit:
            print(f"⚠️ {name} has NO audit records.")
            stale_count += 1
            continue
            
        days_since = (now - last_audit).days
        if days_since > days_threshold:
            print(f"⏰ {name} is stale. Last audit was {days_since} days ago.")
            stale_count += 1
            
    print(f"\nTotal stale or unaudited entities: {stale_count}")

if __name__ == "__main__":
    find_stale_audits()
