import requests
import time

SEEN_TOKENS = set()

def fetch_latest_tokens():
    url = "https://client-api-2-0.prod.pump.fun/tokens/trending"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            for token in data:
                address = token.get("address")
                if address not in SEEN_TOKENS:
                    SEEN_TOKENS.add(address)
                    name = token.get("name", "Unknown")
                    liquidity = token.get("liquidity", 0) / 1e9
                    created_time = token.get("created_at")
                    print(f"🆕 {name} | 💧{liquidity:.3f} SOL | 🕐 {created_time}")
                    print(f"https://pump.fun/{address}\n")
    except Exception as e:
        print(f"Error fetching tokens: {e}")

if __name__ == "__main__":
    fetch_latest_tokens()
