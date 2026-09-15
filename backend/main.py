from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "YouTube Team Analytics API"}

@app.get("/videos")
def get_videos():
    return [
        {
            "title": "test1",
            "team": "team1",
            "views": 500000
        },
        {
            "title": "test2",
            "team": "team2",
            "views": 750000
        }
    ]