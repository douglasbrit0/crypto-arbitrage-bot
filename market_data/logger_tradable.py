# market_data/logger_tradable.py
import csv
import time
import os
from datetime import datetime
from market_data.clients import exchanges

# 1. Make OUTPUT_CSV point to project root
ROOT_DIR   = os.path.dirname(os.path.dirname(__file__))
OUTPUT_CSV = os.path.join(ROOT_DIR, "spreads_tradable.csv")
DEPTH_LIMIT = 5  # how many levels of bids/asks to fetch

def normalize(ob):
    """
    Return (best_bid, best_ask) from a CCXT order book dict.
    """
    bid = ob["bids"][0][0] if ob["bids"] else None
    ask = ob["asks"][0][0] if ob["asks"] else None
    return float(bid), float(ask)

def log_header():
    print(f"[tradable_logger] creating {OUTPUT_CSV}")
    with open(OUTPUT_CSV, mode="w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "timestamp",
            # raw top‐of-book bids and asks
            "binance_bid", "binance_ask",
            "kraken_bid",  "kraken_ask",
            # mid‐prices & mid‐spread
            "mid_binance", "mid_kraken",
            "mid_spread",
            # tradable spreads
            "spread_buyB_sellK",  # buy on Binance.ask, sell on Kraken.bid
            "spread_buyK_sellB"   # buy on Kraken.ask, sell on Binance.bid
        ])

def log_snapshot():
    # 1. Fetch order books from both exchanges
    ob_b = exchanges["binance"].fetch_order_book("BTC/USDT", DEPTH_LIMIT)
    ob_k = exchanges["kraken"].fetch_order_book("BTC/USD",  DEPTH_LIMIT)

    # 2. Normalize to (bid, ask)
    bid_b, ask_b = normalize(ob_b)
    bid_k, ask_k = normalize(ob_k)

    # 3. Compute mid‐prices & mid‐spread
    mid_b = (bid_b + ask_b) / 2
    mid_k = (bid_k + ask_k) / 2
    mid_spread = mid_b - mid_k

    # 4. Compute “tradable” spreads:
    #buy Binance.ask, sell Kraken.bid
    spread_buyB_sellK = bid_k - ask_b
    #buy Kraken.ask, sell Binance.bid
    spread_buyK_sellB = bid_b - ask_k

    # 5. Timestamp (UTC)
    ts = datetime.utcnow().isoformat()

    # 6. Print to console for quick feedback
    print(
        f"[tradable_logger] {ts} | mid_spread={mid_spread:.2f} "
        f"| buyB→sellK={spread_buyB_sellK:.2f} "
        f"| buyK→sellB={spread_buyK_sellB:.2f}"
    )

    # 7. Append a row to CSV
    with open(OUTPUT_CSV, mode="a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            ts,
            bid_b, ask_b,
            bid_k, ask_k,
            mid_b, mid_k,
            mid_spread,
            spread_buyB_sellK,
            spread_buyK_sellB
        ])

def run_logger(interval_seconds=5):
    """
    Run the logger every interval_seconds until interrupted.
    """
    log_header()
    try:
        while True:
            log_snapshot()
            time.sleep(interval_seconds)
    except KeyboardInterrupt:
        print("[tradable_logger] stopped by user")

if __name__ == "__main__":
    run_logger()
