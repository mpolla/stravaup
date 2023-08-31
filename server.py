#!/usr/bin/env python3
#
# Web server to capture the code provided by the redirect link
# when "Authorize" is pressed in the Strave app authorization form.
#

from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from sys import exit

class CaptureHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        path = parsed_path.path
        query_params = parse_qs(parsed_path.query)

        if path == '/capture':
            # Obtain and report code to stdout
            code_value = query_params.get('code', [''])[0]
            print(code_value)

            # Respond
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"Captured 'code'")

            # Stop server after capturing
            server.server_close()
            exit(0)
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        return  # Suppress log messages


if __name__ == '__main__':
    server = HTTPServer(('localhost', 8080), CaptureHandler)
    server.serve_forever()
