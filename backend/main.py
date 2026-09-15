import os
import requests
from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()

API_KEY = os.getenv("YOUTUBE_API_KEY")

app = FastAPI()

@app.get("/video")
def get_video():
    url = "https://www.googleapis.com/youtube/v3/videos"

    params = {
        "part": "snippet",
        "id": "63iIZppXB_4",
        "key": API_KEY
    }

    response = requests.get(url, params = params)

    return response.json()
