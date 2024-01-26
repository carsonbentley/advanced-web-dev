from request import Request
from response import Response

def decode_request(http_string):
    http_string = http_string.decode('utf-8')
    lines = http_string.split('\r\n')
    start_line = lines[0].split(" ")
    req = Request(
        method=start_line[0],
        uri=start_line[1],
        version=start_line[2],
        headers={
            
        },
        text=""
    )
    for i in range(3, (len(lines) - 3)):
        key_value_pair = lines[i].split(" ")
        key = key_value_pair[0].replace(":", "")
        req.headers.update({key : key_value_pair[1]})
    
    return req
    

def encode_response(res):
    response = res.version + " " + str(res.code) + " " + res.reason
    for key in res.headers:
        response = response + key + ": " + str(res.headers[key]) + "\r\n"
    response = response + "\r\n\n" + res.text


    return response