""" nicovideo2discord discord module """

import datetime
import os
import atexit
import functools

import pypresence
import nicovideo.video

from . import savedata

presence_rpc = pypresence.Presence(savedata.DISCORD_CLIENT_ID, connection_timeout=300, response_timeout=300)
presence_rpc.connect()

@functools.cache
def _get_video_with_cache(video_id: str):
    return nicovideo.video.get_metadata(video_id)

def update_video(videoid: str, time: datetime.timedelta, now: datetime.datetime):
    """ Rich Presenceの再生時更新 """
    timesecs = 0
    for record in savedata.records:
        _, start, end = record.split(",")
        start_datetime, end_datetime = (datetime.datetime.fromisoformat(iso) for iso in (start, end))
        if start_datetime.day == datetime.datetime.now().day:
            timesecs += (end_datetime - start_datetime).seconds
    all_time = datetime.timedelta(seconds=timesecs)
    video = _get_video_with_cache(videoid)
    presence_rpc.update(pid=os.getpid(), state=f"本日累計 {all_time}（一時停止時に更新）",
                        details=f"「{video.title}」（{video.cached_uploader.nickname}）を視聴中",
                        start=float((now-time).timestamp()),
                        large_image="tv_chan", large_text="ニコニコテレビちゃん",
                        buttons=[
                            {"label": "視聴する", "url": f"https://www.nicovideo.jp/watch/{video.nicovideo_id}"},
                            {"label": "ニコニコ動画トップ", "url": "https://www.nicovideo.jp/video_top"}
                        ])

def clear():
    """ Rich Presenceのクリア """
    presence_rpc.clear(pid=os.getpid())

def close():
    """ 接続解除 """
    presence_rpc.close()

atexit.register(close)
