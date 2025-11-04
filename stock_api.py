"""
Stock Price API Module using yfinance

This module provides a simple interface to fetch stock prices and information
using the free yfinance library.
"""

import yfinance as yf
from datetime import datetime, timedelta
from typing import Optional, Dict, Any, List
import pandas as pd


class StockAPI:
    """
    A wrapper class for yfinance to fetch stock market data.
    """

    def __init__(self):
        """Initialize the StockAPI."""
        pass

    def get_current_price(self, ticker: str) -> Optional[float]:
        """
        Get the current price of a stock.

        Args:
            ticker: Stock ticker symbol (e.g., 'AAPL', 'GOOGL')

        Returns:
            Current stock price as float, or None if error occurs
        """
        try:
            stock = yf.Ticker(ticker)
            data = stock.history(period='1d')
            if not data.empty:
                return round(data['Close'].iloc[-1], 2)
            return None
        except Exception as e:
            print(f"Error fetching price for {ticker}: {e}")
            return None

    def get_stock_info(self, ticker: str) -> Dict[str, Any]:
        """
        Get detailed information about a stock.

        Args:
            ticker: Stock ticker symbol

        Returns:
            Dictionary containing stock information
        """
        try:
            stock = yf.Ticker(ticker)
            info = stock.info
            return {
                'symbol': ticker,
                'name': info.get('longName', 'N/A'),
                'current_price': info.get('currentPrice', 'N/A'),
                'market_cap': info.get('marketCap', 'N/A'),
                'pe_ratio': info.get('trailingPE', 'N/A'),
                'dividend_yield': info.get('dividendYield', 'N/A'),
                '52_week_high': info.get('fiftyTwoWeekHigh', 'N/A'),
                '52_week_low': info.get('fiftyTwoWeekLow', 'N/A'),
                'currency': info.get('currency', 'N/A'),
            }
        except Exception as e:
            print(f"Error fetching info for {ticker}: {e}")
            return {}

    def get_historical_data(
        self,
        ticker: str,
        period: str = '1mo',
        interval: str = '1d'
    ) -> pd.DataFrame:
        """
        Get historical price data for a stock.

        Args:
            ticker: Stock ticker symbol
            period: Time period ('1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max')
            interval: Data interval ('1m', '2m', '5m', '15m', '30m', '60m', '90m', '1h', '1d', '5d', '1wk', '1mo', '3mo')

        Returns:
            DataFrame with historical data (Open, High, Low, Close, Volume)
        """
        try:
            stock = yf.Ticker(ticker)
            data = stock.history(period=period, interval=interval)
            return data
        except Exception as e:
            print(f"Error fetching historical data for {ticker}: {e}")
            return pd.DataFrame()

    def get_multiple_prices(self, tickers: List[str]) -> Dict[str, float]:
        """
        Get current prices for multiple stocks.

        Args:
            tickers: List of stock ticker symbols

        Returns:
            Dictionary mapping ticker symbols to their current prices
        """
        prices = {}
        for ticker in tickers:
            price = self.get_current_price(ticker)
            if price:
                prices[ticker] = price
        return prices

    def compare_stocks(self, tickers: List[str]) -> pd.DataFrame:
        """
        Compare multiple stocks with key metrics.

        Args:
            tickers: List of stock ticker symbols

        Returns:
            DataFrame comparing the stocks
        """
        comparison_data = []

        for ticker in tickers:
            info = self.get_stock_info(ticker)
            if info:
                comparison_data.append({
                    'Ticker': ticker,
                    'Name': info.get('name', 'N/A'),
                    'Price': info.get('current_price', 'N/A'),
                    'Market Cap': info.get('market_cap', 'N/A'),
                    'P/E Ratio': info.get('pe_ratio', 'N/A'),
                    '52W High': info.get('52_week_high', 'N/A'),
                    '52W Low': info.get('52_week_low', 'N/A'),
                })

        return pd.DataFrame(comparison_data)

    def get_price_change(self, ticker: str, days: int = 1) -> Optional[Dict[str, Any]]:
        """
        Calculate price change over a specified number of days.

        Args:
            ticker: Stock ticker symbol
            days: Number of days to look back

        Returns:
            Dictionary with price change information
        """
        try:
            stock = yf.Ticker(ticker)
            end_date = datetime.now()
            start_date = end_date - timedelta(days=days+5)  # Extra days for market closures

            data = stock.history(start=start_date, end=end_date)

            if len(data) >= 2:
                current_price = data['Close'].iloc[-1]
                old_price = data['Close'].iloc[0]
                change = current_price - old_price
                change_percent = (change / old_price) * 100

                return {
                    'ticker': ticker,
                    'current_price': round(current_price, 2),
                    'old_price': round(old_price, 2),
                    'change': round(change, 2),
                    'change_percent': round(change_percent, 2),
                    'days': days
                }
            return None
        except Exception as e:
            print(f"Error calculating price change for {ticker}: {e}")
            return None


def quick_price(ticker: str) -> Optional[float]:
    """
    Quick function to get current stock price.

    Args:
        ticker: Stock ticker symbol

    Returns:
        Current price or None
    """
    api = StockAPI()
    return api.get_current_price(ticker)
