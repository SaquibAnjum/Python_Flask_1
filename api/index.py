import sys
from pathlib import Path

# Add the 'src' directory to Python path
SRC_DIR = Path(__file__).resolve().parent.parent / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from api_prac import app

# WSGI Middleware to handle any Vercel path prefix rewriting
class VercelPathMiddleware:
    def __init__(self, wsgi_app):
        self.wsgi_app = wsgi_app

    def __call__(self, environ, start_response):
        path_info = environ.get("PATH_INFO", "")
        # Normalize /api/index.py or /api/index prefix if present in PATH_INFO
        if path_info.startswith("/api/index.py"):
            environ["PATH_INFO"] = path_info[len("/api/index.py"):] or "/"
        elif path_info.startswith("/api/index"):
            environ["PATH_INFO"] = path_info[len("/api/index"):] or "/"
        return self.wsgi_app(environ, start_response)

app.wsgi_app = VercelPathMiddleware(app.wsgi_app)
