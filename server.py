

from http.server import HTTPServer, CGIHTTPRequestHandler

host = "localhost"
port = 8000
CGIHTTPRequestHandler.cgi_directories = ["/cgi-bin"]

server = HTTPServer((host, port), CGIHTTPRequestHandler)

print(f"Servidor iniciado en http://{host}:{port}")
print("Accede a tu calculadora en: http://localhost:8000/index.html")
print("Presiona Ctrl+C para detenerlo")

try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\nServidor detenido por el usuario.")
    server.server_close()