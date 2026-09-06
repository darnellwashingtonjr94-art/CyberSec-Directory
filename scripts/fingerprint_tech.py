import json
import urllib.request
from pathlib import Path

def fingerprint_server(url):
    if not url.startswith('http'):
        url = f"https://{url}"
        
    req = urllib.request.Request(url, method='HEAD', headers={'User-Agent': 'SecDir-Bot'})
    try:
        with urllib.request.urlopen(req, timeout=5) as response:
            headers = response.info()
            tech_stack = {}
            for header in ['Server', 'X-Powered-By', 'X-AspNet-Version']:
                if header in headers:
                    tech_stack[header] = headers[header]
            return tech_stack
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    data_path = Path(__file__).parent.parent / "data" / "institutions.json"
    with open(data_path, 'r') as f:
        for inst in json.load(f):
            domain = inst.get("domain")
            if domain:
                tech = fingerprint_server(domain)
                if tech and "error" not in tech:
                    print(f"[{domain}] Stack: {tech}")
