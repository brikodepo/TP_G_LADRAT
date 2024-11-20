import os
from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleRouter(BaseHTTPRequestHandler):
    def do_GET(self):
        # Utiliser un chemin absolu pour éviter les erreurs de permissions
        path = os.path.join("C:\\Users\\Antony\\Desktop\\epsi_b3_infra_2425\\projets\\webserver\\www", self.path[1:])
        print(f"Trying to access: {path}")

        if os.path.exists(path):
            with open(path, "rb") as file:
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.end_headers()
                self.wfile.write(file.read())
        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"404 Not Found")

server_address = ("", 8088)
httpd = HTTPServer(server_address, SimpleRouter)
print("Server launched on http://localhost:8088")
httpd.serve_forever()
