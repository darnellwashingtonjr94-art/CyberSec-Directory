import json
import urllib.request
from datetime import datetime
from pathlib import Path

def get_domain_expiry(domain):
    url = f"https://rdap.org/domain/{domain}"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'SecDir-Bot'})
        with urllib.request.urlopen(req, timeout=5) as response:
            data = json.loads(response.read().decode())
            events = data.get('events', [])
            for event in events:
                if event.get('eventAction') == 'expiration':
                    return event.get('eventDate')
    except Exception:
        return None
    return None

if __name__ == "__main__":
    data_path = Path(__file__).parent.parent / "data" / "institutions.json"
    with open(data_path, 'r') as f:
        institutions = json.load(f)
        
    for inst in institutions:
        domain = inst.get("domain")
        if domain:
            expiry_str = get_domain_expiry(domain)
            if expiry_str:
                # Parse basic ISO 8601 date format returned by most RDAP servers
                expiry_date = datetime.strptime(expiry_str[:10], "%Y-%m-%d")
                days_left = (expiry_date - datetime.utcnow()).days
                status = "🔴 AT RISK" if days_left < 30 else "🟢 Safe"
                print(f"[{domain}] Expires: {expiry_str[:10]} ({days_left} days) - {status}")
