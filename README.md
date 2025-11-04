# invest
Investment related work with free stock price API

## Stock Price API

This repository provides a simple, free stock price API using the `yfinance` library. It allows you to fetch real-time and historical stock data without any API keys or authentication.

## Features

- Get current stock prices
- Fetch detailed stock information (market cap, P/E ratio, dividends, etc.)
- Retrieve historical price data
- Compare multiple stocks
- Calculate price changes over time
- Support for all stocks available on Yahoo Finance

## Installation

1. Clone this repository:
```bash
git clone <your-repo-url>
cd invest
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

Or install directly:
```bash
pip install yfinance pandas
```

## Quick Start

### Get Current Stock Price

```python
from stock_api import quick_price

# Quick price lookup
price = quick_price('AAPL')
print(f"Apple stock price: ${price}")
```

### Using the StockAPI Class

```python
from stock_api import StockAPI

api = StockAPI()

# Get current price
price = api.get_current_price('TSLA')
print(f"Tesla: ${price}")

# Get detailed stock information
info = api.get_stock_info('MSFT')
print(info)

# Get historical data
historical = api.get_historical_data('GOOGL', period='1mo', interval='1d')
print(historical)

# Compare multiple stocks
comparison = api.compare_stocks(['AAPL', 'MSFT', 'GOOGL'])
print(comparison)

# Calculate price change
change = api.get_price_change('AMZN', days=7)
print(f"Change: ${change['change']} ({change['change_percent']}%)")
```

## API Methods

### `get_current_price(ticker: str) -> float`
Get the current price of a stock.

**Parameters:**
- `ticker`: Stock ticker symbol (e.g., 'AAPL', 'GOOGL')

**Returns:** Current stock price as float

### `get_stock_info(ticker: str) -> dict`
Get detailed information about a stock.

**Returns:** Dictionary containing:
- `symbol`: Stock ticker
- `name`: Company name
- `current_price`: Current price
- `market_cap`: Market capitalization
- `pe_ratio`: Price-to-earnings ratio
- `dividend_yield`: Dividend yield
- `52_week_high`: 52-week high price
- `52_week_low`: 52-week low price
- `currency`: Trading currency

### `get_historical_data(ticker: str, period: str, interval: str) -> DataFrame`
Get historical price data.

**Parameters:**
- `ticker`: Stock ticker symbol
- `period`: Time period ('1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max')
- `interval`: Data interval ('1m', '2m', '5m', '15m', '30m', '60m', '90m', '1h', '1d', '5d', '1wk', '1mo', '3mo')

**Returns:** pandas DataFrame with OHLCV data

### `get_multiple_prices(tickers: List[str]) -> dict`
Get current prices for multiple stocks.

**Parameters:**
- `tickers`: List of stock ticker symbols

**Returns:** Dictionary mapping tickers to prices

### `compare_stocks(tickers: List[str]) -> DataFrame`
Compare multiple stocks with key metrics.

**Returns:** pandas DataFrame with comparison data

### `get_price_change(ticker: str, days: int) -> dict`
Calculate price change over specified days.

**Parameters:**
- `ticker`: Stock ticker symbol
- `days`: Number of days to look back

**Returns:** Dictionary with change information

## Example Usage

Run the example script to see all features in action:

```bash
python example_usage.py
```

## Supported Stock Symbols

The API supports all stock symbols available on Yahoo Finance, including:
- US stocks (AAPL, GOOGL, MSFT, TSLA, AMZN, etc.)
- International stocks (add exchange suffix, e.g., 'BMW.DE' for BMW on Frankfurt)
- Cryptocurrencies (BTC-USD, ETH-USD, etc.)
- Currencies (EURUSD=X, GBPUSD=X, etc.)
- Indices (^GSPC for S&P 500, ^DJI for Dow Jones, etc.)

## Notes

- This API is completely free and doesn't require API keys
- Data is sourced from Yahoo Finance
- Real-time quotes may have a 15-minute delay for some exchanges
- For high-frequency trading or production use, consider a paid API service

## License

MIT License - feel free to use this for your investment projects!
