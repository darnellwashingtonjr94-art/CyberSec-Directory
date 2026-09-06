import json
import urllib.request
from pathlib import Path

def check_security_txt(domain):
    url = f"https://{domain}/.well-known/security.txt"
    req = urllib.request.Request(url, method='HEAD', headers={'User-Agent': 'SecDir-Bot'})
    try:
        with urllib.request.urlopen(req, timeout=5) as response:
            return response.status == 200
    except Exception:
        # Fallback to root directory check as per older RFC draft
        url_root = f"https://{domain}/security.txt"
        req_root = urllib.request.Request(url_root, method='HEAD', headers={'User-Agent': 'SecDir-Bot'})
        try:
            with urllib.request.urlopen(req_root, timeout=5) as res:
                return res.status == 200
        except Exception:
            return False

if __name__ == "__main__":
    data_path = Path(__file__).parent.parent / "data" / "institutions.json"
    with open(data_path, 'r') as f:
        institutions = json.load(f)
        
    for inst in institutions:
        domain = inst.get("domain")
        if domain:
            has_sec_txt = check_security_txt(domain)
            print(f"[{domain}] security.txt: {'✅ Found' if has_sec_txt else '❌ Missing'}")
