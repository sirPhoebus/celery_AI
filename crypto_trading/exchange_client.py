import ccxt
from .config import BINANCE_API_KEY, BINANCE_SECRET_KEY

class ExchangeClient:
        def __init__(self):
                self.exchange = ccxt.binance({
                'apiKey': BINANCE_API_KEY,
                'secret': BINANCE_SECRET_KEY,
                'enableRateLimit': True
                })

        def get_ticker(self, symbol):
                return self.exchange.fetch_ticker(symbol)

        def place_order(self, symbol, side, amount, price=None):
                return self.exchange.create_order(
                symbol=symbol,
                type='limit' if price else 'market',
                side=side,
                amount=amount,
                price=price
                )

        def get_balance(self, currency):
                return self.exchange.fetch_balance()[currency] 