import json
import urllib.request
from pathlib import Path

def get_txt_records(domain):
    # Using Google's DNS-over-HTTPS API
    url = f"https://dns.google/resolve?name={domain}&type=TXT"
    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
            answers = data.get('Answer', [])
            return [ans['data'] for ans in answers]
    except Exception:
        return []

if __name__ == "__main__":
    data_path = Path(__file__).parent.parent / "data" / "institutions.json"
    with open(data_path, 'r') as f:
        institutions = json.load(f)
        
    for inst in institutions:
        domain = inst.get("domain")
        if domain:
            dmarc_records = get_txt_records(f"_dmarc.{domain}")
            has_dmarc = any("v=DMARC1" in r for r in dmarc_records)
            
            spf_records = get_txt_records(domain)
            has_spf = any("v=spf1" in r for r in spf_records)
            
            print(f"[{domain}] DMARC: {'✅' if has_dmarc else '❌'} | SPF: {'✅' if has_spf else '❌'}")
