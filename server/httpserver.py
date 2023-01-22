import http.server
import socketserver
import socket

PORT = 8080
DIRECTORY = "."


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)


with socketserver.TCPServer((socket.gethostbyname(socket.gethostbyname()), PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()