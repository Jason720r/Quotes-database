import json
from http.server import BaseHTTPRequestHandler, HTTPServer

class HandleRequests(BaseHTTPRequestHandler):

    def do_GET(self):

        self._set_headers(200)

        print(self.path)

        if self.path == "/quotes":

            response = [
                {"id": 1, "quote": "Hello", "author": "Me"}, 
                {"id": 1, "quote": "Hello", "author": "Me"}
            ]
        else:
            response = []

        self.wfile.write(json.dumps(response).encode())
    def do_POST(self):

        self._set_headers(201)

        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        response = { "payload": post_body}
        self.wfile.write(json.dumps(response).encode())