import requests
import os
import json

USERNAME = "streams.clip"
WEBHOOK_URL = os.environ["DISCORD_WEBHOOK"]

API_URL = f"https://r.jina.ai/https://www.tiktok.com/@{USERNAME}"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(API_URL, headers=headers, timeout=20)

if response.status_code != 200:
    print("Failed to fetch TikTok page")
    exit(0)

text = response.text

# Find latest video ID in page
import re
matches = re.findall(r'"id":"(\d{19})"', text)

if not matches:
    print("No videos found")
    exit(0)

latest_id = matches[0]
video_url = f"https://www.tiktok.com/@{USERNAME}/video/{latest_id}"

# Read last posted ID
try:
    with open("last.txt", "r") as f:
        last = f.read().strip()
except:
    last = ""

if latest_id != last:
    requests.post(WEBHOOK_URL, json={
        "content": f"🔥 **New TikTok Posted!**\n{video_url}"
    })
    with open("last.txt", "w") as f:
        f.write(latest_id)
    print("Posted new video")
else:
    print("No new video")
