import os
import json
import urllib.request

def send_slack_alert(message):
    webhook_url = os.environ.get("SLACK_WEBHOOK_URL")
    if not webhook_url:
        print("SLACK_WEBHOOK_URL not set. Skipping notification.")
        return

    payload = json.dumps({"text": f"⚠️ *Security Directory Alert*: {message}"}).encode('utf-8')
    req = urllib.request.Request(webhook_url, data=payload, 
                                 headers={'Content-Type': 'application/json'})
    try:
        urllib.request.urlopen(req)
        print("Alert sent to Slack.")
    except Exception as e:
        print(f"Failed to send Slack alert: {e}")

if __name__ == "__main__":
    # Typically called by other scripts on error
    send_slack_alert("Nightly data validation pipeline failed.")
