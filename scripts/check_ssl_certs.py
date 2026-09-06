import json
import ssl
import socket
from datetime import datetime
from pathlib import Path

def get_ssl_expiry(hostname):
    context = ssl.create_default_context()
    try:
        with socket.create_connection((hostname, 443), timeout=3) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
                expiry_date = datetime.strptime(cert['notAfter'], "%b %d %H:%M:%S %Y %Z")
                return (expiry_date - datetime.utcnow()).days
    except Exception:
        return -1

if __name__ == "__main__":
    data_path = Path(__file__).parent.parent / "data" / "institutions.json"
    with open(data_path, 'r') as f:
        institutions = json.load(f)
        
    for inst in institutions:
        domain = inst.get("domain")
        if domain:
            days_left = get_ssl_expiry(domain)
            status = "🔴 Expired/Error" if days_left < 0 else f"🟢 {days_left} days left"
            print(f"[{domain}] SSL Status: {status}")
