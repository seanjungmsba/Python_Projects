import requests
import logging

class TelegramBot:
    """
    Handles Telegram bot communication.
    """
    def __init__(self, token: str, chat_id: str):
        self.token = token
        self.chat_id = chat_id

    def send_message(self, message: str) -> None:
        """
        Sends a message to the Telegram bot.

        Args:
            message (str): The message to send.
        """
        url = f"https://api.telegram.org/bot{self.token}/sendMessage"
        data = {"chat_id": self.chat_id, "text": message}
        try:
            requests.post(url, data=data)
        except Exception as e:
            logging.error(f"Failed to send Telegram message: {e}")