# 🪙 Crypto Arbitrage Bot

A real-time cryptocurrency arbitrage bot written in Python that monitors bid/ask spreads across major exchanges and logs spread data for analysis. Built using [CCXT](https://github.com/ccxt/ccxt) and designed with modular components to support future trade execution and backtesting.

## 🚀 Features

- Fetches live order books from Binance and Kraken
- Logs raw bid/ask and mid-price spreads to CSV
- Computes "tradable" spreads between exchanges
- Separate logging modes for raw mid-prices and tradable opportunities
- Asynchronous-ready structure and configurable polling interval
- Sandbox mode enabled for Binance (safe testing)

## 🧠 Technologies Used

- Python 3.10+
- [CCXT](https://github.com/ccxt/ccxt)
- `asyncio`, `csv`, `pandas`, `numpy`
- `python-dotenv` for credential management

## 📁 Project Structure

crypto-arbitrage-bot/
│
├── main.py # Entry point (fetches single snapshot from both exchanges)
├── requirements.txt # Python dependencies
├── spreads.csv # Mid-price spreads (output)
├── spreads_tradable.csv # Tradable spreads (output)
│
├── market_data/
│ ├── clients.py # CCXT exchange clients setup (Binance + Kraken)
│ ├── credentials.py # Loads API credentials from .env
│ ├── detector.py # Functions to calculate tradable spreads
│ ├── logger_mid.py # Logs mid-price spreads to CSV
│ ├── logger_tradable.py # Logs tradable spreads to CSV


## ⚙️ Setup Instructions

1. **Clone the repository:**
```bash
git clone https://github.com/douglasbrit0/crypto-arbitrage-bot.git
cd crypto-arbitrage-bot
```

2. **Create a virtual environment:**

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
Create a .env file in the root directory:
```

4. **Create a .env file in the root directory:**

```env
BINANCE_API_KEY=your_binance_key
BINANCE_SECRET_KEY=your_binance_secret
KRAKEN_API_KEY=your_kraken_key
KRAKEN_SECRET_KEY=your_kraken_secret
```

5. **Run the bot:**

To fetch a snapshot once (for testing):

```bash
python main.py
```

To start logging mid-price spreads:

```bash
python market_data/logger_mid.py
```

To start logging tradable spreads:

```bash
python market_data/logger_tradable.py
```

📈 Future Plans
Implement live trading logic using CCXT

Add support for more exchanges (e.g., Coinbase, Bitfinex)

Create backtesting engine from CSV logs

Streamlit dashboard for real-time monitoring

Telegram/email alert system for threshold breaches

🤝 Contributing
Pull requests and feature suggestions are welcome! Open an issue to start a discussion.

© 2025 Douglas Brito

```yaml

---
Let me know if you'd like a badge (e.g., Python version, MIT license) or a visual architecture diagram added!
```

