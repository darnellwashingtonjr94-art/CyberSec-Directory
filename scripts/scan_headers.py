import json
import urllib.request
from pathlib import Path

def check_security_headers(url):
    if not url.startswith('http'):
        url = f"https://{url}"
    
    headers_to_check = ['Strict-Transport-Security', 'Content-Security-Policy', 'X-Frame-Options']
    req = urllib.request.Request(url, method='HEAD', headers={'User-Agent': 'SecDir-Bot'})
    
    try:
        with urllib.request.urlopen(req, timeout=5) as response:
            headers = response.info()
            results = {h: (h in headers) for h in headers_to_check}
            return results
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    data_path = Path(__file__).parent.parent / "data" / "institutions.json"
    with open(data_path, 'r') as f:
        institutions = json.load(f)
        
    for inst in institutions:
        domain = inst.get("domain")
        if domain:
            print(f"Scanning headers for {domain}...")
            status = check_security_headers(domain)
            print(f"  Result: {status}")
