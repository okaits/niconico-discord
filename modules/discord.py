""" nicovideo2discord discord module """

import datetime
import os
import atexit
import functools

import pypresence
import nicovideo.video

from . import savedata

presence_rpc = pypresence.Presence(savedata.discord_client_id)
presence_rpc.connect()

@functools.cache
def _get_video_with_cache(video_id: str):
    return nicovideo.video.get_metadata(video_id)

async def update_video(videoid: str, time: datetime.timedelta, now: datetime.datetime):
    """ Rich Presenceの再生時更新 """
    timesecs = 0
    for record in savedata.records:
        _, start, end = record.split(",")
        start_datetime, end_datetime = (datetime.datetime.fromisoformat(iso) for iso in (start, end))
        if start_datetime.day == datetime.datetime.now().day:
            timesecs += (end_datetime - start_datetime).seconds
    time = datetime.timedelta(seconds=timesecs)
    video = _get_video_with_cache(videoid)
    presence_rpc.update(pid=os.getpid(), state=f"本日累計 {time}",
                        details=f"「{video.title}」（{video.cached_uploader.nickname}）を視聴中",
                        start=float((now-time).timestamp()),
                        large_image="tv_chan", large_text="ニコニコテレビちゃん",
                        buttons=[
                            {"label": "視聴する", "url": f"https://www.nicovideo.jp/{video.nicovideo_id}"},
                            {"label": "ニコニコ動画トップ", "url": "https://www.nicovideo.jp/video_top"}
                        ])

async def clear():
    """ Rich Presenceのクリア """
    presence_rpc.clear(pid=os.getpid())

def close():
    """ 接続解除 """
    presence_rpc.close()

atexit.register(close)
