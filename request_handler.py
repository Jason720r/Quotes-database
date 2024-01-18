import json
from http.server import BaseHTTPRequestHandler, HTTPServer

class HandleRequests(BaseHTTPRequestHandler):

    def do_GET(self):

        self._set_headers(200)

        print(self.path)

        if self.path == "/quotes":

            response = [
                {}
            ]