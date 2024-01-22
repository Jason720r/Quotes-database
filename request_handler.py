import json
from http.server import BaseHTTPRequestHandler, HTTPServer

class HandleRequests(BaseHTTPRequestHandler):

    def do_GET(self):

        self._set_headers(200)

        print(self.path)

        if self.path == "/workouts":

            response = [
                {"id": 1, "quote": "Hello", "author": "Me"}, 
                {"id": 1, "quote": "Hello", "author": "Me"}
            ]
        else:
            response = []

        self.wfile.write(json.dumps(response).encode())
    def do_POST(self):