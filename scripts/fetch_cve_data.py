import urllib.request
import json

CVE_API_URL = "https://services.nvd.nist.gov/rest/json/cves/2.0?resultsPerPage=5"

def fetch_latest_cves():
    print("Fetching latest CVEs from NVD...")
    req = urllib.request.Request(CVE_API_URL, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            vulnerabilities = data.get("vulnerabilities", [])
            for v in vulnerabilities:
                cve_id = v["cve"]["id"]
                desc = v["cve"]["descriptions"][0]["value"]
                print(f"🚨 {cve_id}: {desc[:80]}...")
    except Exception as e:
        print(f"Failed to fetch CVEs: {e}")

if __name__ == "__main__":
    fetch_latest_cves()
