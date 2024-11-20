import os
from dotenv import load_dotenv

load_dotenv()

BINANCE_API_KEY = os.getenv('BINANCE_API_KEY')
BINANCE_SECRET_KEY = os.getenv('BINANCE_SECRET_KEY')

TRADING_PAIRS = ['BTC/USDT']
UPDATE_INTERVAL = 60  # seconds > config.py