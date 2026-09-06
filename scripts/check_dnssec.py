import json
import urllib.request
from pathlib import Path

def check_dnssec(domain):
    # Type 48 is DNSKEY
    url = f"https://dns.google/resolve?name={domain}&type=48"
    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
            return 'Answer' in data and len(data['Answer']) > 0
    except Exception:
        return False

if __name__ == "__main__":
    data_path = Path(__file__).parent.parent / "data" / "institutions.json"
    with open(data_path, 'r') as f:
        institutions = json.load(f)
        
    for inst in institutions:
        domain = inst.get("domain")
        if domain:
            is_secure = check_dnssec(domain)
            print(f"[{domain}] DNSSEC: {'✅ Active' if is_secure else '❌ Disabled'}")
