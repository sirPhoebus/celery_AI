from crypto_trading.celery_config import celery_app
from crypto_trading.tasks import update_market_data, analyze_market, execute_trades
from celery import chain
import time

def main():
    while True:
        workflow = chain(
            update_market_data.s(),
            analyze_market.s(),
            execute_trades.s()
        )
        workflow.apply_async()
        time.sleep(10)  # in seconds

if __name__ == '__main__':
    main()