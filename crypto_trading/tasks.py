from celery import shared_task
import pandas as pd
from .exchange_client import ExchangeClient
from .config import TRADING_PAIRS

client = ExchangeClient()

@shared_task
def update_market_data():
    data = {}
    for pair in TRADING_PAIRS:
        ticker = client.get_ticker(pair)
        data[pair] = {
            'last_price': ticker['last'],
            'volume': ticker['baseVolume'],
            'bid': ticker['bid'],
            'ask': ticker['ask']
        }
    return data

@shared_task
def analyze_market(data):
    signals = {}
    for pair, info in data.items():
        # Simple price-based signal
        if info['bid'] > info['last_price'] * 1.02:  # 2% increase
            signals[pair] = 'SELL'
        elif info['ask'] < info['last_price'] * 0.98:  # 2% decrease
            signals[pair] = 'BUY'
        else:
            signals[pair] = 'HOLD'
    return signals

@shared_task
def execute_trades(signals):
    for pair, signal in signals.items():
        if signal in ['BUY', 'SELL']:
            try:
                amount = 0.01  # Example fixed amount
                client.place_order(pair, signal.lower(), amount)
            except Exception as e:
                print(f"Error executing {signal} order for {pair}: {e}")