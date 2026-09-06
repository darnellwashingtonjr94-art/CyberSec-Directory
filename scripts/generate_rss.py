import csv
from pathlib import Path
from email.utils import formatdate
from datetime import datetime

RSS_TEMPLATE = """<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">
<channel>
    <title>Cybersecurity Directory Updates</title>
    <link>https://github.com/org/Ncr-cybersecurity-directory</link>
    <description>Latest security audits and metric updates.</description>
    {items}
</channel>
</rss>"""

ITEM_TEMPLATE = """
    <item>
        <title>Audit Update: {inst_id}</title>
        <description>Score updated to {score}</description>
        <pubDate>{date}</pubDate>
    </item>"""

def generate_feed():
    base = Path(__file__).parent.parent
    items = []
    
    with open(base / "data" / "metrics.csv", 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Convert YYYY-MM-DD to RFC 822 format required by RSS
            dt = datetime.strptime(row.get('audit_date', '2020-01-01'), '%Y-%m-%d')
            pub_date = formatdate(dt.timestamp())
            
            items.append(ITEM_TEMPLATE.format(
                inst_id=row.get('inst_id', 'Unknown'),
                score=row.get('score', 'N/A'),
                date=pub_date
            ))
            
    rss_content = RSS_TEMPLATE.format(items="".join(items))
    output = base / "docs" / "feed.xml"
    output.write_text(rss_content)
    print(f"RSS feed generated at {output.name}")

if __name__ == "__main__":
    generate_feed()
