import platform
from crypto_trading.celery_config import celery_app
from crypto_trading.tasks import update_market_data, analyze_market, execute_trades
from celery import chain
import time

def main():
    print("Starting crypto trading bot...")
    print(f"Python version: {platform.python_version()}")
    print("Connecting to Redis and starting Celery tasks...")
    
    while True:
        try:
            workflow = chain(
                update_market_data.s(),
                analyze_market.s(),
                execute_trades.s()
            )
            workflow.apply_async()
            time.sleep(10)  # in seconds
        except Exception as e:
            print(f"Error in main loop: {e}")
            time.sleep(10)  # Wait before retrying

if __name__ == '__main__':
    main()