""" nicovideo2discord savedata module """

import pathlib
import logging
import datetime
import typing

SAVEDATA_FILE = pathlib.Path("./savedata.n2dsave")
logger = logging.getLogger()

if not SAVEDATA_FILE.exists():
    with open(SAVEDATA_FILE, encoding="utf-8", mode="w") as h:
        write_data = f'N2DSAVE: {int(input("Discord client id: "))}\n'
        h.write(write_data)

with open(SAVEDATA_FILE, encoding="utf-8", mode="r") as h:
    savedata = h.read()

discord_client_id = int(savedata.split("\n")[0][9:])
now_playing: typing.Optional[tuple[str, datetime.datetime]] = None
now_playing_time_update: typing.Optional[tuple[datetime.timedelta, datetime.datetime]] = None

records = []
for record in savedata.split("\n")[3:]:
    records.append(record)

async def append_record(value: str):
    """ recordsリストにvalueを追加した後、更にSAVEDATA_FILEに記録する。 """
    with open(SAVEDATA_FILE, encoding="utf-8", mode="a") as h:
        h.write("\n" + value)
    records.append(value)
