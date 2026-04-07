from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps({"status": "running"}).encode())

    def do_POST(self):
        if self.path == "/reset":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"message": "env reset ok"}).encode())
        else:
            self.send_response(404)
            self.end_headers()

def main():
    server = HTTPServer(("0.0.0.0", 7860), Handler)
    print("Server running on port 7860...")
    server.serve_forever()

if __name__ == "__main__":
    main()
