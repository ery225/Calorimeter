# run py app.py
# http://localhost:8000/
from http.server import BaseHTTPRequestHandler, HTTPServer

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('index.html', 'rb') as file:
                self.wfile.write(file.read())
        elif self.path == '/2d_implementations.html':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('2d_implementations.html', 'rb') as file:
                self.wfile.write(file.read())
        elif self.path == '/3d_implementations.html':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('3d_implementations.html', 'rb') as file:
                self.wfile.write(file.read())
        elif self.path == '/style.css':
            self.send_response(200)
            self.send_header('Content-type', 'text/css')
            self.end_headers()
            with open('style.css', 'rb') as file:
                self.wfile.write(file.read())
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'404 Not Found')


    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        
        # Parse the form data to extract user inputs
        form_data = urllib.parse.parse_qs(post_data)
        
        # Access user inputs from form_data dictionary
        search_item = form_data.get('search_item', [''])[0]

        # Process user inputs as needed (e.g., perform search)
        print('Search Item:', search_item)

        # Respond to the client
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Form submitted successfully')

def run_server(port=8000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, RequestHandler)
    print('Server running on port', port)
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()