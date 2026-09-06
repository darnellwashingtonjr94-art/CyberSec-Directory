import json
import urllib.request
from urllib.error import URLError, HTTPError
from pathlib import Path

def check_alive(domain):
    url = f"https://{domain}"
    req = urllib.request.Request(url, method='HEAD', headers={'User-Agent': 'SecDir-Bot'})
    try:
        with urllib.request.urlopen(req, timeout=5) as response:
            return response.status
    except HTTPError as e:
        return e.code
    except URLError as e:
        return str(e.reason)
    except Exception:
        return "Timeout/Error"

if __name__ == "__main__":
    data_path = Path(__file__).parent.parent / "data" / "institutions.json"
    with open(data_path, 'r') as f:
        institutions = json.load(f)
        
    for inst in institutions:
        domain = inst.get("domain")
        if domain:
            status = check_alive(domain)
            if status in [200, 301, 302]:
                print(f"🟢 [{domain}] Alive (Status: {status})")
            else:
                print(f"🔴 [{domain}] Unreachable (Status: {status})")
