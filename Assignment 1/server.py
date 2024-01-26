import socket
from request import Request
from  encoder import decode_request, encode_response
from middleware import logging, required_headers, static_files, compose
from router import router

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(("127.0.0.1", 8000))
    s.listen()
    print("listening on port 8000")

    while True:
        connection, addr = s.accept()
        with connection:
            data = connection.recv(8192)
            if not data:
                connection.close()
                continue
            request = decode_request(data)
            res = "HTTP/1.1 200 Ok\nConnection: close\n\n<h1>Hello, world!</h1>"
            middleware_list = [logging, required_headers, static_files]
            middleware_chain = compose(router, middleware_list)
            response = middleware_chain(request)
            encoded_response = encode_response(response)
            connection.send(bytes(encoded_response, "UTF-8"))
            