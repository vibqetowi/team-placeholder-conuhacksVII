import http.server
import socket
import socketserver
import sys
from qr_code import QR_Code

PORT = 8000
DIRECTORY = "."
class handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,direcory = DIRECTORY, **kwargs)

    def getIP(PORT):
        global clientsocket
        ip = socket.gethostbyname(socket.gethostname())
        with socketserver.TCPServer((ip, PORT), handler) as httpd:
            print("serving at port", PORT)
            httpd.serve_forever()



ip = socket.gethostbyname(socket.gethostname())
print(ip)









    