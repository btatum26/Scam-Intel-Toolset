import http.server
import socketserver
from datetime import datetime
import json
import os

PORT = 8080
LOG_FILE = "private/visitor_logs.txt"
TEMPLATE_FILE = "index.html"

class TrackingHandler(http.server.SimpleHTTPRequestHandler):
    def load_template(self):
        if os.path.exists(TEMPLATE_FILE):
            with open(TEMPLATE_FILE, "r") as f:
                return f.read()
        return "<html><body><h1>Loading...</h1></body></html>"

    def do_GET(self):
        # Initial capture of headers
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        client_ip = self.client_address[0]
        headers = dict(self.headers)
        
        log_entry = {
            "type": "INITIAL_GET",
            "timestamp": timestamp,
            "ip": client_ip,
            "user_agent": headers.get("User-Agent"),
            "headers": headers
        }
        
        with open(LOG_FILE, "a") as f:
            f.write(json.dumps(log_entry) + "\n")
            
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(self.load_template().encode())

    def do_POST(self):
        if self.path == '/log':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            fingerprint = json.loads(post_data.decode('utf-8'))
            
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            client_ip = self.client_address[0]
            
            log_entry = {
                "type": "FINGERPRINT_DATA",
                "timestamp": timestamp,
                "ip": client_ip,
                "fingerprint": fingerprint
            }
            
            print(f"\n[!!!] DEEP FINGERPRINT RECEIVED from {client_ip}")
            print(f"    Timezone: {fingerprint.get('timezone')}")
            print(f"    Platform: {fingerprint.get('navigator', {}).get('platform')}")

            with open(LOG_FILE, "a") as f:
                f.write(json.dumps(log_entry) + "\n")
            
            self.send_response(204)
            self.end_headers()

print(f"[*] Advanced Tracking Server starting on port {PORT}...")
with socketserver.TCPServer(("", PORT), TrackingHandler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[!] Keyboard interrupt received. Stopping server...")
    finally:
        httpd.server_close()
        print("[*] Server stopped.")
