import requests
from urllib.parse import quote

from config import RIOT_API_KEY, REGION


def get_puuid(gameName: str, tagLine: str) -> str:
    url = f"https://{REGION}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{quote(gameName)}/{quote(tagLine)}"
    r = requests.get(url, headers={"X-Riot-Token": RIOT_API_KEY})
    r.raise_for_status()
    account = r.json()
    return account["puuid"]
