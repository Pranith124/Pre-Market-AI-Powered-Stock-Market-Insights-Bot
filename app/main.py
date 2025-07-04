import json
import threading
import uvicorn

from app.core import telegram_api_key
from app.api import app,tel_bot_handling # assuming both are in api.py


def start_telegram_bot():
    tel_bot_handling(telegram_api_key)



if __name__ == "__main__":
    # Start bot in background
    threading.Thread(target=start_telegram_bot, daemon=True).start()

    # Start FastAPI server
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)

