import os
import requests

def send_telegram_chat(msg):
    telegram_bot_secret = os.getenv("TELEGRAM_BOT_SECRET")
    telegram_chat_id = os.getenv("TELEGRAM_CHAT_ID")

    telegram_bot_secret_2 = os.getenv("TELEGRAM_BOT_SECRET_2")
    telegram_chat_id_2 = os.getenv("TELEGRAM_CHAT_ID_2")

     # Debugging: Print values to verify they're fetched correctly
    print(f"Telegram Bot Secret: {telegram_bot_secret}")
    print(f"Telegram Chat ID: {telegram_chat_id}")
    
    # Ensure the secrets are fetched correctly
    if not telegram_bot_secret or not telegram_chat_id:
        raise ValueError("Telegram bot secret or chat ID not set in environment variables")
    telegram_send_chat_url_2 = f"https://api.telegram.org/bot{telegram_bot_secret_2}/sendMessage?chat_id={telegram_chat_id_2}&text="
    response_2 = requests.post(telegram_send_chat_url_2 + str(msg))

    telegram_send_chat_url = f"https://api.telegram.org/bot{telegram_bot_secret}/sendMessage?chat_id={telegram_chat_id}&text="
    response = requests.post(telegram_send_chat_url + str(msg))
    if response.status_code != 200:
        print("Something went wrong with sending telegram messages, are the keys correct?")
        print(response.text)
