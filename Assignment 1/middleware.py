import datetime
from response import Response

def logging(next):
    def middleware(req):

        print(f"REQUEST: {req.method}  {req.uri}")
        res = next(req)

        print(f"RESPONSE: {req.uri} {res.code} {res.reason}")
        return res
    
    return middleware

def static_files(next):
    def middleware(req):
        if "." in req.uri:
            if ".js" in req.uri:
                content_type = 'application/javascript'
            elif ".css" in req.uri:
                content_type = 'text/css'
            else:
                return Response(
                    version='HTTP/1.1',
                    code=404,
                    reason='Not Found',
                    headers={
                        'Connection' : 'close',
                    },
                    text='404 Not Found'
                )
            with open(f'static{req.uri}', 'r') as file:
                file_content = file.read()
            return Response(
                version='HTTP/1.1',
                code=200,
                reason='OK',
                headers={
                    'Content-Type' : content_type,
                    'Connection' : 'close',
                    'Content-Length' : str(len(file_content)),
                },
                text=file_content
            )
        else:
            res = next(req)
            return res
    return middleware

def required_headers(next):
    def middleware(req):
        res = next(req)
        headers = {
            "Connection": "close",
            "Server": "Carson's Server",
            "Cache-Control": "no-cache",
            "Date": str(datetime.datetime.today()),
        }
        headers.update(res.headers)
        res.headers = headers
        return res

    return middleware

def compose(end_result_function, middleware_factory_list):
    for middleware in middleware_factory_list:
        end_result_function = middleware(end_result_function)
    return end_result_function