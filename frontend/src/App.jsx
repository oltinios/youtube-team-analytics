import { useEffect, useState } from "react";

function App() {
    const [videos, setVideos] = useState([]);

    useEffect(() => {
        fetch("http://localhost:8000/videos")
            .then(response => response.json())
            .then(data => setVideos(data));
    }, []);

    return (
        <div>
            <h1>YouTube Team Analytics</h1>

            {videos.map((video) => (
                <div key={video.title}>
                    <h2>{video.title}</h2>
                    <p>{video.team}</p>
                    <p>{video.views} views</p>
                </div>
            ))}
        </div>
    );
}

export default App;