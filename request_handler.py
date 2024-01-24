import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from views import get_all_products, get_single_product, get_all_categories, get_single_category

class HandleRequests(BaseHTTPRequestHandler):
    def parse_url(self, path):

        path_params = path.split("/")
        resource = path_params[1]
        id = None

        try:
            id = int(path_params[2])
        except IndexError:
            pass
        except ValueError:
            pass
        return (resource, id)

    def do_GET(self):

        self._set_headers(200)
        response = {}

        (resource, id) = self.parse_url(self.path)

        if resource == "products":
            if id is not None:
                response = get_single_product(id)
            else:
                response = get_all_products()
        
        if resource == "categories":
            if id is not None:
                response = get_single_category(id)
            else:
                response = get_all_categories()

        self.wfile.write(json.dumps(response).encode())
    def do_POST(self):

        self._set_headers(201)

        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        response = { "payload": post_body}
        self.wfile.write(json.dumps(response).encode())

    def do_PUT(self):

        self.do_PUT()
    def _set_headers(self, status):

        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
    
    def do_OPTIONS(self):

        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type, Accept')
        self.end_headers()

def main():

    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()

if __name__ == "__main__":
    main()