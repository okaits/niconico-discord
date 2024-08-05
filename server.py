""" nicovideo2discord server module """

import uvicorn
import modules.httpserver

uvicorn.run(modules.httpserver.app, host="127.0.0.1", port=36201)
