import re
from pathlib import Path

LINK_REGEX = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')

def lint_markdown_links(docs_dir):
    broken_links = 0
    for md_file in docs_dir.glob("*.md"):
        content = md_file.read_text()
        links = LINK_REGEX.findall(content)
        
        for text, target in links:
            if not target.startswith("http"):
                target_path = (md_file.parent / target).resolve()
                if not target_path.exists():
                    print(f"Broken link in {md_file.name}: {target}")
                    broken_links += 1
                    
    if broken_links == 0:
        print("✅ All relative Markdown links are valid.")
    else:
        print(f"❌ Found {broken_links} broken links.")

if __name__ == "__main__":
    lint_markdown_links(Path(__file__).parent.parent / "docs")
