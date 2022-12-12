from http.server import HTTPServer, CGIHTTPRequestHandler
server_address = ("127.0.0.2", 8004)
httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
httpd.serve_forever()