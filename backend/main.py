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
        "publishedAfter": "2026-08-14T00:00:00Z"
    }

    all_items = []

    while True:
        response = requests.get(url, params=params)
        data = response.json()

        all_items.extend(data["items"])

        if "nextPageToken" not in data:
            break

        params["pageToken"] = data["nextPageToken"]

    videos = []
    ids = []
    seen = set()

    for item in all_items:

        video_id = item["id"]["videoId"]

        if video_id in seen:
            continue

        seen.add(video_id)

        date = item["snippet"]["publishedAt"]

        ids.append(video_id)

        video = {
            "id": video_id,
            "title": item["snippet"]["title"],
            "published_at": date
        }

        videos.append(video)

    videos.sort(key=lambda video: video["published_at"], reverse = True)

    all_statistics = []

    for i in range(0, len(ids), 50):

        batch = ids[i:i + 50]

        video_params = {
            "part": "statistics",
            "id": ",".join(batch),
            "key": API_KEY
        }

        vid_response = requests.get(video_url, params=video_params)
        dataID = vid_response.json()

        all_statistics.extend(dataID["items"])

    for video in videos:

        for item in all_statistics:

            if video["id"] == item["id"]:

                video["viewCount"] = item["statistics"]["viewCount"]

    print(len(videos))

    return videos