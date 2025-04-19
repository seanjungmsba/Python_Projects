import requests
import pandas as pd
from ta.momentum import StochasticOscillator
from ta.trend import MACD
import logging
from typing import List, Optional, Tuple

class MarketAnalyzer:
    """
    Handles market data fetching and signal analysis.
    Fetches market data and performs technical analysis.
    """
    @staticmethod
    def get_krw_tickers() -> List[str]:
        """
        Fetches all KRW market tickers from Upbit.

        Returns:
            List[str]: A list of KRW market tickers.
        """
        url = "https://api.upbit.com/v1/market/all"
        try:
            res = requests.get(url).json()
            return [x['market'] for x in res if x['market'].startswith('KRW-')]
        except Exception as e:
            logging.error(f"Failed to fetch tickers: {e}")
            return []

    @staticmethod
    def get_ohlcv(ticker: str) -> Optional[pd.DataFrame]:
        """
        Fetches OHLCV data for a given ticker.

        Args:
            ticker (str): The ticker symbol to fetch data for.

        Returns:
            Optional[pd.DataFrame]: A DataFrame containing OHLCV data, or None if an error occurs.
        """
        url = f"https://api.upbit.com/v1/candles/days?market={ticker}&count=30"
        try:
            res = requests.get(url, timeout=10).json()
            if not isinstance(res, list) or len(res) == 0:
                logging.warning(f"No OHLCV data for {ticker}")
                return None
            df = pd.DataFrame(res)
            df = df[['candle_date_time_kst', 'opening_price', 'high_price', 'low_price', 'trade_price']]
            df.columns = ['time', 'open', 'high', 'low', 'close']
            df = df.iloc[::-1].reset_index(drop=True)
            return df
        except Exception as e:
            logging.error(f"Failed to fetch OHLCV for {ticker}: {e}")
            return None

    @staticmethod
    def check_signals(df: pd.DataFrame) -> Tuple[bool, bool]:
        """
        Checks for buy and sell signals using Stochastic Oscillator and MACD.

        Args:
            df (pd.DataFrame): A DataFrame containing OHLCV data.

        Returns:
            Tuple[bool, bool]: A tuple (buy_signal, sell_signal).
        """
        try:
            stoch = StochasticOscillator(df['high'], df['low'], df['close'], window=14, smooth_window=3)
            df['stoch_k'] = stoch.stoch()
            df['stoch_d'] = stoch.stoch_signal()
            macd = MACD(df['close'], window_slow=26, window_fast=12, window_sign=9)
            df['macd'] = macd.macd()
            df['macd_signal'] = macd.macd_signal()
            latest = df.iloc[-1]
            previous = df.iloc[-2]
            buy_signal = latest['stoch_k'] > 80 and previous['stoch_k'] <= 80
            sell_signal = latest['macd'] < previous['macd'] and latest['macd'] > latest['macd_signal']
            return buy_signal, sell_signal
        except Exception as e:
            logging.error(f"Signal check failed: {e}")
            return False, False