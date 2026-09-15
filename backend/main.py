import os
import requests
from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()

API_KEY = os.getenv("YOUTUBE_API_KEY")

app = FastAPI()

@app.get("/channel")
def get_channel_videos():
    url = "https://www.googleapis.com/youtube/v3/search"

    params = {
        "part": "snippet",
        "channelId": "UCNAf1k0yIjyGu3k9BwAg3lg",
        "type": "video",
        "maxResults": 10,
        "key": API_KEY
    }

    response = requests.get(url, params = params)

    data = response.json()

    titles = []

    for item in data["items"]:
        titles.append(item["snippet"]["title"])

    return titles