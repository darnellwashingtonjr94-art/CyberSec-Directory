import re
from pathlib import Path

# Common patterns for hardcoded credentials
SECRET_PATTERNS = [
    re.compile(r'(?i)(api_key|apikey|secret|password|token)[\s:=]+[\'"]([a-zA-Z0-9_\-]{12,})[\'"]'),
    re.compile(r'(?i)ghp_[a-zA-Z0-9]{36}')  # GitHub Personal Access Token
]

def scan_for_secrets(directory):
    found_secrets = False
    
    for filepath in directory.rglob("*"):
        if filepath.is_file() and filepath.suffix in ['.json', '.csv', '.py', '.yml', '.md']:
            try:
                content = filepath.read_text(encoding='utf-8')
                for pattern in SECRET_PATTERNS:
                    matches = pattern.findall(content)
                    if matches:
                        print(f"🚨 Potential secret found in: {filepath.relative_to(directory)}")
                        found_secrets = True
            except UnicodeDecodeError:
                pass # Skip binary files if accidentally caught
                
    if not found_secrets:
        print("✅ No hardcoded secrets found.")

if __name__ == "__main__":
    scan_for_secrets(Path(__file__).parent.parent)
