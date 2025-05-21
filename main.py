# main.py
from market_data.clients import exchanges

def main():
    # Example usage:
    btc_usdt = "BTC/USDT"
    bin_ticker = exchanges["binance"].fetch_ticker(btc_usdt)
    kr_ticker = exchanges["kraken"].fetch_ticker("BTC/USD")
    print("Binance:", bin_ticker["bid"], "/", bin_ticker["ask"])
    print("Kraken:",  kr_ticker["bid"], "/", kr_ticker["ask"])

if __name__ == "__main__":
    main()
