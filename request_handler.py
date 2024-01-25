import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from views import get_all_products, get_single_product, create_product, delete_product, update_product, get_all_categories, get_single_category, create_category, delete_category

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

        post_body = json.loads(post_body)

        (resource, id) = self.parse_url(self.path)

        new_product = None

        if resource == "products":
            new_product = create_product(post_body)
        if resource == "categories":
            new_category = create_category(post_body)

        self.wfile.write(json.dumps(new_product).encode())
        self.wfile.write(json.dumps(new_category).encode())
    
    def do_DELETE(self):

        self._set_headers(204)

        (resource, id) = self.parse_url(self.path)

        if resource == "products":
            delete_product(id)
        if resource == "categories":
            delete_category(id)

        self.wfile.write("".encode())



    def do_PUT(self):
        
        self._set_headers(204)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        # Delete a single animal from the list
        if resource == "animals":
            update_product(id, post_body)

     # Encode the new animal and send in response
        self.wfile.write("".encode())
    
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