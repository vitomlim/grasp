import os
from dotenv import load_dotenv, find_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

RIOT_API_KEY = os.getenv("RIOT_API_KEY")
REGION = "americas"