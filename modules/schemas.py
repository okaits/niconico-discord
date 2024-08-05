""" nicovideo2discord schemas module """

import datetime
import pydantic

class ClientRequest:
    """ クライアントのリクエストボディ """
    class APIv1StartWatch(pydantic.BaseModel):
        """ /api/v1/start_watch のリクエストボディ """
        video_id: str

    class APIv1Seek(pydantic.BaseModel):
        """ /api/v1/seek のリクエストボディ """
        time: datetime.timedelta

class ServerResponse:
    """ サーバのレスポンスボディ """
    class ResponseMessage(pydantic.BaseModel):
        """ 汎用レスポンスボディ """
        message: str
