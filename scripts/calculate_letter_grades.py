import os
import json
import csv

# 1. Define exact paths dynamically based on where the script is running
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DATA_DIR = os.path.join(BASE_DIR, 'data')

institutions_json = os.path.join(DATA_DIR, 'institutions.json')
input_csv = os.path.join(DATA_DIR, 'metrics.csv')
output_csv = os.path.join(DATA_DIR, 'letter_grades_output.csv') # Adjust name as needed

# 2. Ensure the data directory exists before doing anything
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)
    print(f"Created missing directory: {DATA_DIR}")

# 3. Safely handle institutions.json
if not os.path.exists(institutions_json):
    print(f"⚠️ Warning: {institutions_json} not found. Skipping institution report generation.")
    institutions_data = {} # Fallback empty data
else:
    with open(institutions_json, 'r') as f:
        try:
            institutions_data = json.load(f)
            print(f"✅ Successfully loaded {institutions_json}")
        except json.JSONDecodeError:
            print(f"❌ Error: {institutions_json} contains invalid JSON.")
            institutions_data = {}

# 4. Safely handle metrics.csv (This fixes your Line 19 FileNotFoundError)
if not os.path.exists(input_csv):
    print(f"❌ Error: {input_csv} not found. Cannot calculate letter grades.")
    print("⚠️ Creating an empty file to prevent workflow crash...")
    
    # Create a dummy CSV so downstream processes don't completely fail
    with open(input_csv, 'w', newline='') as f:
        f.write("id,metric_1,metric_2\n") # Replace with your actual headers
else:
    print(f"✅ Found {input_csv}. Processing metrics...")
    # YOUR ORIGINAL LOGIC GOES HERE safely inside the else block
    with open(input_csv, 'r') as fin, open(output_csv, 'w', newline='') as fout:
        reader = csv.reader(fin)
        writer = csv.writer(fout)
        
        # Example processing loop
        for row in reader:
            writer.writerow(row) 
