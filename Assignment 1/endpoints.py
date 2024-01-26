from response import Response

def index(req):
    with open('templates/index.html', 'r') as file:
        response_text = file.read()
    return Response(
        version='HTTP/1.1',
                code=200,
                reason='OK',
                headers={
                    'Content-Type' : 'text/html',
                    'Connection' : 'close',
                    'Content-Length' : str(len(response_text)),
                },
                text=response_text
            )

def about(req):
    with open('templates/about.html', 'r') as file:
        response_text = file.read()
    return Response(
        version='HTTP/1.1',
                code=200,
                reason='OK',
                headers={
                    'Content-Type' : 'text/html',
                    'Connection' : 'close',
                    'Content-Length' : str(len(response_text)),
                },
                text=response_text
            )

def experience(req):
    with open('templates/experience.html', 'r') as file:
        response_text = file.read()
    return Response(
        version='HTTP/1.1',
                code=200,
                reason='OK',
                headers={
                    'Content-Type' : 'text/html',
                    'Connection' : 'close',
                    'Content-Length' : str(len(response_text)),
                },
                text=response_text
            )

def projects(req):
    with open('templates/projects.html', 'r') as file:
        response_text = file.read()
    return Response(
        version='HTTP/1.1',
        code=200,
        reason='OK',
        headers={
            'Content-Type' : 'text/html',
            'Connection' : 'close',
            'Content-Length' : str(len(response_text)),
        },
        text=response_text
    )

def info(req):
    return Response(
        version='HTTP/1.1',
        code=301,
        reason='Moved Permanently',
        headers={
            'Location' : '/about',
            'Connection' : 'close',
        },
        text=""
    )
