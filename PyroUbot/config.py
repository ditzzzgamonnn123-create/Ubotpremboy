import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "200"))

DEVS = list(map(int, os.getenv("DEVS", "7843883316").split()))

API_ID = int(os.getenv("API_ID", "37169072"))

API_HASH = os.getenv("API_HASH", "03c6ff4de8758a6cc2227b501c167ddd")

BOT_TOKEN = os.getenv("BOT_TOKEN", "8966731365:AAHZTQitBvJDAFWAOBMd-ZtZSr2rDas9QKc")

OWNER_ID = int(os.getenv("OWNER_ID", "7843883316"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1003992129460").split()))

RMBG_API = os.getenv("RMBG_API", "L6EYpgV4UNCZ8jyM1cwdNxkU")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://Apalakapalak:Apalakapalak@apalakapalak.84vdobg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1003992129460"))
