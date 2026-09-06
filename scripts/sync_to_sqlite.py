import sqlite3
import json
import csv
from pathlib import Path

def build_database(db_path, json_path, csv_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Institutions table
    cursor.execute('''CREATE TABLE IF NOT EXISTS institutions 
                      (id TEXT PRIMARY KEY, name TEXT, region TEXT)''')
    with open(json_path, 'r') as f:
        for item in json.load(f):
            cursor.execute('INSERT OR IGNORE INTO institutions VALUES (?, ?, ?)', 
                           (item.get('id'), item.get('name'), item.get('region')))
            
    # Metrics table
    cursor.execute('''CREATE TABLE IF NOT EXISTS metrics 
                      (inst_id TEXT, score INTEGER, audit_date TEXT)''')
    with open(csv_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            cursor.execute('INSERT INTO metrics VALUES (?, ?, ?)', 
                           (row.get('inst_id'), row.get('score'), row.get('audit_date')))
            
    conn.commit()
    conn.close()
    print(f"Database successfully synced at {db_path.name}")

if __name__ == "__main__":
    base = Path(__file__).parent.parent
    build_database(base / "data" / "directory.db", 
                   base / "data" / "institutions.json", 
                   base / "data" / "metrics.csv")
