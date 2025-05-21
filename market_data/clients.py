# market_data/clients.py
import ccxt
from market_data.credentials import BINANCE_API_KEY, BINANCE_SECRET_KEY, KRAKEN_API_KEY, KRAKEN_SECRET_KEY

# ——— BINANCE TESTNET/SANDBOX ———
binance = ccxt.binance({
    "apiKey":          BINANCE_API_KEY,
    "secret":          BINANCE_SECRET_KEY,
    "enableRateLimit": True,
    "options": {
        "defaultType": "spot",
    },
    # override all of CCXT’s default URLs to hit testnet instead of api.binance.com
    "urls": {
        "api": {
            "public":  "https://testnet.binance.vision/api",
            "private": "https://testnet.binance.vision/api",
        },
    },
})
# tell CCXT to append “/sandbox” where needed & sign appropriately
binance.set_sandbox_mode(True)

# ——— KRAKEN (public data only) ———
kraken = ccxt.kraken({
    # you can omit apiKey/secret here, or include your real keys if you have them
    "enableRateLimit": True,
})

exchanges = {
    "binance": binance,
    "kraken":  kraken,
}
