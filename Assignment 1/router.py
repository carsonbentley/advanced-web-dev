import datetime
from endpoints import *


def router(req):
    if req.uri == "/" or req.uri == "/index":
        return index(req)
    if req.uri == "/about":
        return about(req)
    if req.uri == "/experience":
        return experience(req)
    if req.uri == "/projects":
        return projects(req)
    if req.uri == "/info":
        return info(req)
    else:
        return Response(
        version="HTTP/1.1",
        code="404",
        reason="Not found",
        headers={
            "Connection": "close",
            "Server": "Joseph's Server",
            "Cache-Control": "no-cache",
            "Date": str(datetime.datetime.today()),
            "Content-Type": "text/html",
            "Content-Length": "23"
        },
        text="<h1>Page not found</h1>"
    )