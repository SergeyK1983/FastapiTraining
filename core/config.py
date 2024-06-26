import os
from pathlib import Path
from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(dotenv_path=os.path.join(BASE_DIR, '.env'))

DB_NAME = os.getenv('DB_NAME', )
DB_USER = os.getenv('DB_USER', )
DB_PASS = os.getenv('DB_PASS', )
DB_HOST = os.getenv('DB_HOST', )
DB_PORT = os.getenv('DB_PORT', )
