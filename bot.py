import requests
import json
import os

USERNAME = "streams.clip"
WEBHOOK_URL = os.environ["DISCORD_WEBHOOK"]

API_URL = f"https://www.tikwm.com/api/user/posts?unique_id={USERNAME}"

r = requests.get(API_URL).json()
latest = r["data"]["videos"][0]

video_url = f"https://www.tiktok.com/@{USERNAME}/video/{latest['video_id']}"

with open("last.txt", "r") as f:
    last = f.read().strip()

if latest["video_id"] != last:
    requests.post(WEBHOOK_URL, json={
        "content": f"🔥 New TikTok posted!\n{video_url}"
    })
    with open("last.txt", "w") as f:
        f.write(latest["video_id"])
