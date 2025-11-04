"""
Example usage of the Stock API module.

This script demonstrates various ways to use the stock_api module
to fetch stock market data using yfinance.
"""

from stock_api import StockAPI, quick_price


def main():
    # Initialize the API
    api = StockAPI()

    print("=" * 60)
    print("Stock Price API - Example Usage")
    print("=" * 60)

    # Example 1: Get current price of a single stock
    print("\n1. Getting current price for Apple (AAPL):")
    apple_price = api.get_current_price('AAPL')
    if apple_price:
        print(f"   AAPL Current Price: ${apple_price}")

    # Example 2: Quick price lookup
    print("\n2. Quick price lookup for Microsoft (MSFT):")
    msft_price = quick_price('MSFT')
    if msft_price:
        print(f"   MSFT Current Price: ${msft_price}")

    # Example 3: Get detailed stock information
    print("\n3. Detailed information for Tesla (TSLA):")
    tesla_info = api.get_stock_info('TSLA')
    if tesla_info:
        for key, value in tesla_info.items():
            print(f"   {key}: {value}")

    # Example 4: Get multiple stock prices
    print("\n4. Getting prices for multiple stocks:")
    tickers = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA']
    prices = api.get_multiple_prices(tickers)
    for ticker, price in prices.items():
        print(f"   {ticker}: ${price}")

    # Example 5: Get historical data
    print("\n5. Getting historical data for AAPL (last 5 days):")
    historical = api.get_historical_data('AAPL', period='5d')
    if not historical.empty:
        print(historical[['Open', 'High', 'Low', 'Close', 'Volume']].tail())

    # Example 6: Compare multiple stocks
    print("\n6. Comparing tech stocks:")
    comparison = api.compare_stocks(['AAPL', 'MSFT', 'GOOGL'])
    if not comparison.empty:
        print(comparison.to_string(index=False))

    # Example 7: Calculate price change
    print("\n7. Price change for AAPL over last 7 days:")
    change = api.get_price_change('AAPL', days=7)
    if change:
        print(f"   Ticker: {change['ticker']}")
        print(f"   Current Price: ${change['current_price']}")
        print(f"   Price {change['days']} days ago: ${change['old_price']}")
        print(f"   Change: ${change['change']} ({change['change_percent']}%)")

    print("\n" + "=" * 60)
    print("Examples completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()
