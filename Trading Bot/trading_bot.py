import os
import time
import threading
from datetime import datetime
from telegram_bot import TelegramBot
from market_analyzer import MarketAnalyzer
from user_settings import UserSettings

class Season2UpBot:
    """
    Orchestrates the trading bot's functionality.
    """
    def __init__(self, telegram_bot: TelegramBot, market_analyzer: MarketAnalyzer, user_settings: UserSettings):
        self.telegram_bot = telegram_bot
        self.market_analyzer = market_analyzer
        self.user_settings = user_settings

    def scan_markets(self) -> None:
        """
        Scans markets for buy signals and sends alerts.
        """
        tickers = self.market_analyzer.get_krw_tickers()
        now = datetime.now().strftime('%Y-%m-%d %H:%M')

        for user_id, settings in self.user_settings.settings.items():
            mode = settings.get("mode", "단타")
            symbols = settings.get("symbols", [])
            min_level = len(settings.get("levels", ["🔔"]))

            filtered_tickers = [t for t in tickers if not symbols or t.split('-')[1] in symbols]
            for ticker in filtered_tickers:
                df = self.market_analyzer.get_ohlcv(ticker, mode)
                if df is None or df.empty:
                    continue

                level = self.market_analyzer.check_signal(df)
                if level and level >= min_level:
                    price = int(df.iloc[-1]['close'])
                    message = f"🚨 Signal detected for {ticker.split('-')[1]} at ₩{price:,} (Level {level})\n🕒 {now}"
                    self.telegram_bot.send_message(user_id, message)

    def handle_commands(self, text: str, user_id: str) -> None:
        """
        Handles Telegram commands.
        """
        # Command handling logic here (similar to the original implementation)
        pass

    def start(self) -> None:
        """
        Starts the trading bot.
        """
        def scan_loop():
            while True:
                self.scan_markets()
                time.sleep(300)

        threading.Thread(target=scan_loop, daemon=True).start()

if __name__ == '__main__':
    TOKEN = os.getenv('TELEGRAM_TOKEN', 'your-telegram-token')
    SETTINGS_FILE = 'season2_settings.json'

    telegram_bot = TelegramBot(TOKEN)
    market_analyzer = MarketAnalyzer()
    user_settings = UserSettings(SETTINGS_FILE)
    user_settings.load()

    trading_bot = TradingBot(telegram_bot, market_analyzer, user_settings)
    trading_bot.start()

    while True:
        time.sleep(1)