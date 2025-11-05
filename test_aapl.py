"""
Quick test to fetch AAPL stock price without yfinance.
Using requests to directly query Yahoo Finance API.
"""

import requests
import json
from datetime import datetime

def get_stock_price_direct(ticker):
    """
    Fetch stock price directly from Yahoo Finance using requests.
    This is a backup method when yfinance isn't installed.
    """
    try:
        # Yahoo Finance query API
        url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}"

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }

        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        data = response.json()

        # Extract current price
        chart = data['chart']['result'][0]
        meta = chart['meta']

        current_price = meta.get('regularMarketPrice')
        previous_close = meta.get('previousClose')
        currency = meta.get('currency', 'USD')

        # Get quote data
        quotes = chart['indicators']['quote'][0]
        timestamps = chart['timestamp']

        if timestamps:
            latest_close = quotes['close'][-1]
            latest_time = datetime.fromtimestamp(timestamps[-1])
        else:
            latest_close = current_price
            latest_time = datetime.now()

        return {
            'ticker': ticker,
            'current_price': current_price,
            'latest_close': latest_close,
            'previous_close': previous_close,
            'currency': currency,
            'timestamp': latest_time.strftime('%Y-%m-%d %H:%M:%S'),
            'change': current_price - previous_close if current_price and previous_close else None,
            'change_percent': ((current_price - previous_close) / previous_close * 100) if current_price and previous_close else None
        }

    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        return None

if __name__ == "__main__":
    print("=" * 60)
    print("Testing Stock Price Fetch for AAPL")
    print("=" * 60)

    result = get_stock_price_direct('AAPL')

    if result:
        print(f"\nTicker: {result['ticker']}")
        print(f"Current Price: ${result['current_price']:.2f} {result['currency']}")
        print(f"Latest Close: ${result['latest_close']:.2f}")
        print(f"Previous Close: ${result['previous_close']:.2f}")

        if result['change'] is not None:
            change_symbol = "+" if result['change'] >= 0 else ""
            print(f"Change: {change_symbol}${result['change']:.2f} ({change_symbol}{result['change_percent']:.2f}%)")

        print(f"Last Updated: {result['timestamp']}")
        print("\n" + "=" * 60)
        print("✓ Test successful! Stock API is working.")
        print("=" * 60)
    else:
        print("\n✗ Test failed - Could not fetch stock data")
