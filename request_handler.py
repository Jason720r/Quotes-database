import json
from urllib.parse import urlparse, parse_qs
from http.server import BaseHTTPRequestHandler, HTTPServer
from views import get_all_products, get_single_product, create_product, delete_product, update_product, get_all_categories, get_single_category, create_category, delete_category, update_category, get_all_users

class HandleRequests(BaseHTTPRequestHandler):
    def _set_headers(self, status_code):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type, Accept, Authorization')
        self.end_headers()
    def parse_url(self, path):
        """Parse the url into the resource and id"""
        parsed_url = urlparse(path)
        path_params = parsed_url.path.split('/')  # ['', 'animals', 1]
        resource = path_params[1]

        if parsed_url.query:
            query = parse_qs(parsed_url.query)
            return (resource, query)

        pk = None
        try:
            pk = int(path_params[2])
        except (IndexError, ValueError):
            pass
        return (resource, pk)

    def do_GET(self):

        self._set_headers(200)
        response = {}

        # Parse URL and store entire tuple in a variable
        parsed = self.parse_url(self.path)

        # If the path does not include a query parameter, continue with the original if block
        if '?' not in self.path:
            ( resource, id ) = parsed

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
        if resource == "users":
            response = get_all_users()
        else: # There is a ? in the path, run the query param functions
            (resource, query) = parsed

        # see if the query dictionary has an email key
        # if query.get('email') and resource == 'users':
        #     response = get_user_by_email(query['email'][0])

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
        
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        success = False

        # Delete a single animal from the list
        if resource == "products":
            update_product(id, post_body)
        if resource == "categories":
            update_category(id, post_body)
        if success:
            self._set_headers(204)
        else:
            self._set_headers(404)

     # Encode the new animal and send in response
        self.wfile.write("".encode())
    
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type, Accept, Authorization')  # Include Authorization here
        self.end_headers()

def main():

    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()

if __name__ == "__main__":
    main()