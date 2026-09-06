import json
import socket
from pathlib import Path

def check_ipv6(domain):
    try:
        # getaddrinfo returns a list of tuples containing socket info
        results = socket.getaddrinfo(domain, None, socket.AF_INET6)
        return bool(results)
    except socket.gaierror:
        return False

if __name__ == "__main__":
    data_path = Path(__file__).parent.parent / "data" / "institutions.json"
    with open(data_path, 'r') as f:
        institutions = json.load(f)
        
    for inst in institutions:
        domain = inst.get("domain")
        if domain:
            has_ipv6 = check_ipv6(domain)
            print(f"[{domain}] IPv6 Support: {'✅' if has_ipv6 else '❌'}")
