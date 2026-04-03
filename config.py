import os
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(BASE_DIR, ".env")

load_dotenv(env_path)

BOT_TOKEN = os.getenv("BOT_TOKEN")