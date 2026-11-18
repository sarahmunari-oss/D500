import re
import requests

TOPIC = "d500-koeln-8f3k29x"   # dein ntfy-Thema
PRODUCT_URL = "https://www.decathlon.de/p/rollentrainer-d500-interaktiv-mit-zwift-cog-und-click/301243/c1m8551028"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/124.0 Safari/537.36",
    "Accept-Language": "de-DE,de;q=0.9",
}

def notify(text, url):
    requests.post(
        f"https://ntfy.sh/{TOPIC}",
        data=text.encode("utf-8"),
        headers={"Title": "Decathlon D500", "Priority": "high", "Click": url},
        timeout=30,
    )

r = requests.get(PRODUCT_URL, headers=HEADERS, timeout=30)
r.raise_for_status()          # bei Blockade (403) schlägt der Lauf fehl
html = r.text

online_verfuegbar = "InStock" in html

print("Online verfügbar:", online_verfuegbar)

if online_verfuegbar:
    notify("D500 ist online wieder verfügbar!", PRODUCT_URL)
