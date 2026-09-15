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
    video_url = "https://www.googleapis.com/youtube/v3/videos"

    params = {
        "part": "snippet",
        "channelId": "UCNAf1k0yIjyGu3k9BwAg3lg",
        "type": "video",
        "maxResults": 50,
        "key": API_KEY,
        "publishedAfter": "2025-08-15T00:00:00Z",
        }

    response = requests.get(url, params = params)

    data = response.json()

    videos = []
    ids = []

    for item in data["items"]:
        ids.append(item["id"]["videoId"])

    ids = ",".join(ids)

    for item in data["items"]:
        video = {
            "id": item["id"]["videoId"],
            "title": item["snippet"]["title"],
            "published_at": item["snippet"]["publishedAt"]
        }
        videos.append(video)

    video_params = {
            "part": "statistics",
            "id": ids,
            "key": API_KEY
        }

    vid_response = requests.get(video_url, params = video_params)
    dataID = vid_response.json()

    for video in videos:
        for item in dataID["items"]:
            if video["id"] == item["id"]:
                #print(video["id"])
                video["viewCount"] = item["statistics"]["viewCount"]

    for item in data["items"]:
        date = item["snippet"]["publishedAt"]

        if date <= "2026-09-24T23:59:59Z":
            print(item["snippet"]["title"])

    return videos