""" nicovideo2discord httpserver module """

import datetime
import nest_asyncio

import fastapi
import fastapi.responses
import fastapi.middleware.cors

from . import savedata
from . import schemas
from . import discord

app = fastapi.FastAPI()
app.add_middleware(fastapi.middleware.cors.CORSMiddleware, allow_origins=[
    "https://www.nicovideo.jp",
    "http://localhost:36201",
    "http://127.0.0.1:36201"
], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
nest_asyncio.apply() #fastapiのasyncioとpypresenceのasyncioが衝突するのを防ぐ

@app.post("/api/v1/update_watch", response_model=schemas.ServerResponse.ResponseMessage,
          status_code=200, response_class=fastapi.responses.ORJSONResponse)
def api_v1_update_watch(videodata: schemas.ClientRequest.APIv1UpdateWatch):
    """ /api/v1/update_watch: Update video."""
    if savedata.now_playing:
        savedata.append_record(
            f"{savedata.now_playing[0]},"
            f"{savedata.now_playing[1].isoformat()},"
            f"{datetime.datetime.now().isoformat()}"
        )
    savedata.now_playing = (videodata.video_id, datetime.datetime.now())
    savedata.now_playing_time_update = (videodata.time, datetime.datetime.now())
    discord.update_video(savedata.now_playing[0], savedata.now_playing_time_update[0],
                               savedata.now_playing_time_update[1])
    return fastapi.responses.ORJSONResponse({"message": "ok"}, status_code=200)

@app.post("/api/v1/stop_watch", response_model=schemas.ServerResponse.ResponseMessage,
          status_code=200, response_class=fastapi.responses.ORJSONResponse)
def api_v1_stop_watch():
    """ /api/v1/stop_watch: Stop watching video. """
    if savedata.now_playing:
        savedata.append_record(
            f"{savedata.now_playing[0]},"
            f"{savedata.now_playing[1].isoformat()},"
            f"{datetime.datetime.now().isoformat()}"
        )
    savedata.now_playing = None
    savedata.now_playing_time_update = None
    discord.clear()
    return fastapi.responses.ORJSONResponse({"message": "ok"}, status_code=200)
