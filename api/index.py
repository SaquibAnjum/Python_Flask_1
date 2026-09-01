import sys
from pathlib import Path

# Add the 'src' directory to Python path
SRC_DIR = Path(__file__).resolve().parent.parent / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from api_prac import app

# For Vercel Serverless Function entry point
app = app
