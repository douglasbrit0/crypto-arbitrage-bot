# market_data/logger.py
import csv, time, os
from datetime import datetime
from market_data.clients import exchanges

# === ensure spreads.csv lives in the project root ===
ROOT_DIR    = os.path.dirname(os.path.dirname(__file__))
OUTPUT_CSV  = os.path.join(ROOT_DIR, 'spreads.csv')
DEPTH_LIMIT = 5

def normalize(ob):
    bid = ob["bids"][0][0] if ob["bids"] else None
    ask = ob["asks"][0][0] if ob["asks"] else None
    return float(bid), float(ask)

def log_header():
    print(f"[logger] creating {OUTPUT_CSV}")
    with open(OUTPUT_CSV, mode="w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "timestamp",
            "binance_bid", "binance_ask",
            "kraken_bid",  "kraken_ask",
            "mid_binance", "mid_kraken",
            "spread"
        ])

def log_snapshot():
    ob_b = exchanges["binance"].fetch_order_book("BTC/USDT", DEPTH_LIMIT)
    ob_k = exchanges["kraken"].fetch_order_book("BTC/USD",  DEPTH_LIMIT)
    bid_b, ask_b = normalize(ob_b)
    bid_k, ask_k = normalize(ob_k)
    mid_b = (bid_b + ask_b) / 2
    mid_k = (bid_k + ask_k) / 2
    spread = mid_b - mid_k
    ts = datetime.utcnow().isoformat()
    print(f"[logger] {ts} | spread={spread:.2f}")
    with open(OUTPUT_CSV, mode="a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([ts, bid_b, ask_b, bid_k, ask_k, mid_b, mid_k, spread])

def run_logger(interval_seconds=5):
    log_header()
    try:
        while True:
            log_snapshot()
            time.sleep(interval_seconds)
    except KeyboardInterrupt:
        print("[logger] stopped by user")

if __name__ == "__main__":
    run_logger()
