import json
import socket
from pathlib import Path

# Ports to check: FTP, SSH, Telnet, RDP
PORTS = [21, 22, 23, 3389]

def check_port(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1.5)
        return s.connect_ex((host, port)) == 0

if __name__ == "__main__":
    data_path = Path(__file__).parent.parent / "data" / "institutions.json"
    with open(data_path, 'r') as f:
        institutions = json.load(f)
        
    for inst in institutions:
        domain = inst.get("domain")
        if domain:
            print(f"Scanning {domain}...")
            for port in PORTS:
                is_open = check_port(domain, port)
                if is_open:
                    print(f"  ⚠️ ALERT: Port {port} is OPEN!")
