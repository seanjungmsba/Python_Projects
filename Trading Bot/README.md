# **Trading Bot**

This project is a cryptocurrency trading bot that monitors the market, analyzes trading signals, and sends alerts via Telegram. It is built using Python and follows Object-Oriented Programming (OOP) principles for modularity and maintainability.

---

## **Features**
- Fetches cryptocurrency market data from the Upbit API.
- Analyzes market data using technical indicators like **Stochastic Oscillator** and **MACD**.
- Sends buy/sell alerts to users via Telegram.
- Supports user-specific settings for monitoring preferences.

---

## **Project Structure**
The project is divided into three main components:

### **1. `MarketAnalyzer`**
Handles market data fetching and technical analysis.

#### **Key Methods**
- **`get_krw_tickers()`**
  - Fetches all KRW market tickers from Upbit.
  - **Returns**: A list of KRW market tickers.

- **`get_ohlcv(ticker: str) -> Optional[pd.DataFrame]`**
  - Fetches OHLCV (Open, High, Low, Close, Volume) data for a given ticker.
  - **Args**:
    - `ticker`: The ticker symbol to fetch data for.
  - **Returns**: A Pandas DataFrame containing OHLCV data or `None` if an error occurs.

- **`check_signals(df: pd.DataFrame) -> Tuple[bool, bool]`**
  - Analyzes OHLCV data for buy and sell signals using **Stochastic Oscillator** and **MACD**.
  - **Args**:
    - `df`: A Pandas DataFrame containing OHLCV data.
  - **Returns**: A tuple `(buy_signal, sell_signal)` indicating whether buy or sell signals are detected.

---

### **2. `TelegramBot`**
Handles communication with the Telegram API.

#### **Key Methods**
- **`send_message(chat_id: str, message: str) -> None`**
  - Sends a message to a specific Telegram chat.
  - **Args**:
    - `chat_id`: The chat ID to send the message to.
    - `message`: The message to send.

- **`get_updates(offset: int = None) -> list`**
  - Fetches updates (e.g., messages) from the Telegram bot.
  - **Args**:
    - `offset`: The offset for updates (optional).
  - **Returns**: A list of updates.

---

### **3. `TradingBot`**
Orchestrates the bot's functionality, including market scanning and Telegram communication.

#### **Key Methods**
- **`scan_markets()`**
  - Scans all KRW tickers for buy and sell signals and sends alerts via Telegram.

- **`handle_commands(text: str, user_id: str)`**
  - Handles Telegram commands sent by users.
  - **Args**:
    - `text`: The command text.
    - `user_id`: The ID of the user who sent the command.

- **`start()`**
  - Starts the trading bot in a separate thread for continuous monitoring.

---

## **Setup Instructions**

### **1. Prerequisites**
- Python 3.8 or higher
- Install required libraries:
  ```bash
  pip install requests pandas ta
  ```

### **2. Environment Variables**
Store sensitive information like the Telegram bot token in environment variables:
- `TELEGRAM_TOKEN`: Your Telegram bot token.
- `TELEGRAM_CHAT_ID`: The chat ID to send messages to.

You can set these variables in a `.env` file or directly in your system.

### **3. Running the Bot**
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/trading-bot.git
   cd trading-bot
   ```

2. Run the bot:
   ```bash
   python season2upbot.py
   ```

---

## **Usage**

### **Telegram Commands**
The bot supports the following commands via Telegram:
- **`/start`**: Starts the bot.
- **`/status`**: Displays the current bot status.
- **`/settings`**: Updates user-specific settings (e.g., symbols to monitor, signal levels).
- **`/help`**: Displays a list of available commands.

---

## **Technical Indicators Used**
1. **Stochastic Oscillator**:
   - Detects overbought and oversold conditions.
   - Used to identify potential buy/sell signals.

2. **MACD (Moving Average Convergence Divergence)**:
   - Identifies trend reversals and momentum changes.

3. **ADX (Average Directional Index)**:
   - Measures the strength of a trend.

---

## **Logging**
The bot uses Python's `logging` module to log errors and warnings. Logs are printed to the console and can be redirected to a file for debugging.

---

## **Future Improvements**
- Add support for more exchanges (e.g., Binance, Coinbase).
- Implement advanced strategies using machine learning.
- Add a web interface for easier configuration and monitoring.

---

## **License**
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## **Contributing**
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

---

