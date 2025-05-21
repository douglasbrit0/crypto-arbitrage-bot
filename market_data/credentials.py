# market_data/credentials.py
from dotenv import load_dotenv
import os

# 1. Load .env from project root
load_dotenv()

# 2. Retrieve your keys
BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
BINANCE_SECRET_KEY = os.getenv("BINANCE_SECRET_KEY")

KRAKEN_API_KEY = os.getenv("KRAKEN_API_KEY")
KRAKEN_SECRET_KEY = os.getenv("KRAKEN_SECRET_KEY")

# 3. Simple check
if not all([BINANCE_API_KEY, BINANCE_SECRET_KEY, KRAKEN_API_KEY, KRAKEN_SECRET_KEY]):
    raise EnvironmentError("One or more API credentials are missing. Check your .env file.")
