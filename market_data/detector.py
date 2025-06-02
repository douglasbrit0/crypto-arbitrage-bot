def get_top(order_book, side="bid"):
    """
    Return the top bid or ask price from a ccxt order_book.
    side="bid" returns best bid; side="ask" returns best ask.
    """
    levels = order_book["bids"] if side == "bid" else order_book["asks"]
    return float(levels[0][0]) if levels else None

def compute_tradable_spreads(ob_bin, ob_krk):
    """
    Returns two tradable spreads:
      A → B: ask_binance – bid_kraken
      B → A: ask_kraken  – bid_binance
    """
    ask_b = get_top(ob_bin,   "ask")
    bid_b = get_top(ob_bin,   "bid")
    ask_k = get_top(ob_krk,   "ask")
    bid_k = get_top(ob_krk,   "bid")

    spread_A_to_B = ask_b - bid_k   # buy on Kraken, sell on Binance
    spread_B_to_A = ask_k - bid_b   # buy on Binance, sell on Kraken

    return spread_A_to_B, spread_B_to_A
