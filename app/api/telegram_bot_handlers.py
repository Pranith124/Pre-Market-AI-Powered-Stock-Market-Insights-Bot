import telebot
from app.services.get_us_index_ticket import get_us_summary_ticket
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import sys
import time
import logging
import json
from requests.exceptions import RequestException
from telebot.apihelper import ApiTelegramException

def tel_bot_handling(telegram_api_key):
    bot = telebot.TeleBot(telegram_api_key)
    ids_file_location="app/core/user_ids.json"
    def save_Id(user_id):
        chat_ids=load_Id()
        if user_id not in chat_ids:
            chat_ids.append(user_id)
            try:
                with open(ids_file_location,"w") as f:
                    json.dump(chat_ids,f)
            except FileNotFoundError:
                print("File is not Found at given Location so it can save the id in the file")
    def Remove_Id(user_id):
        chat_ids=load_Id()
        if user_id in chat_ids:
            chat_ids.remove(user_id)
            try:
                with open(ids_file_location,"w") as f:
                    json.dump(chat_ids,f)
            except FileNotFoundError:
                print("File Location is Incorrect error is occuring while removeing the ids")
            return True
        return False

    def load_Id():
        try:
            with open(ids_file_location, "r") as f:
                content = f.read().strip()
                if content:
                    return json.loads(content)
                else:
                    return []
        except FileNotFoundError:
            print("File is not found at given location. Returning empty list.")
            return []
        except json.JSONDecodeError:
            print("File exists but contains invalid JSON. Returning empty list.")
            return []
    def subscribe_user(user_id):
        chat_ids=load_Id()
        if user_id not in chat_ids:
            save_Id(user_id=user_id)
            return True
        return False

    
        

    @bot.message_handler(commands=['start',"Subscribe"])
    def start(message):
        try:
            chat_id=message.chat.id
            subscribed = subscribe_user(message.chat.id)
            if subscribed:
                bot.reply_to(message, "✅ You have subscribed successfully!  you will Get the Daily Updates on Stock at schedulding timeings")
            else:
                bot.reply_to(message, "📬 You are already subscribed.")
        except Exception as e:
            print(f"Exception is occured due to  {e}")
    
    @bot.message_handler(commands=['Unsubscribe','stop'])
    def stop(message):
        try:
            chat_id=message.chat.id
            if Remove_Id(chat_id):
                bot.reply_to(message,"❌ You have unsubscribed from stock updates.")
            else:
                bot.reply_to(message,"⚠️ You were not subscribed.")
        except Exception as e:
            print(f"Exception is occured due to  {e}")

    def US_index():
        try:
            print("Scheduled task running at", datetime.now())
            summary = get_us_summary_ticket(type="US",interval="1m", lookback_days=1)
            try:
                for id in load_Id():
                    bot.send_message(id, text=summary if summary else "No Updates Due to yesterday US Markets Holiday")
                    print(f"message is succesfully sended to {id} at ",datetime.now())
                print("ALL US market Updates are Succesfully sended to subcribed users")
            except ApiTelegramException as e:
                print(f"[Telegram API Error] {e}")
            except RequestException as e:
                print(f"[Network Error] Could not reach Telegram servers: {e}")
        except Exception as e:
            print(f"[Unhandled Error] in scheduled task: {e}")

    def Global_index():
        try:
            print("Scheduled task running at", datetime.now())
            summary = get_us_summary_ticket(type="GLOBAL",interval="1m", lookback_days=1)
            try:
                for id in load_Id():
                    bot.send_message(id, text=summary if summary else "No Updates Due to yesterday GLOBAL Markets Holiday")
                    print(f"message is succesfully sended to {id} at ",datetime.now())
                print("ALL GLOBAL market Updates are Succesfully sended to subcribed users")
            except ApiTelegramException as e:
                print(f"[Telegram API Error] {e}")
            except RequestException as e:
                print(f"[Network Error] Could not reach Telegram servers: {e}")
        except Exception as e:
            print(f"[Unhandled Error] in scheduled task: {e}")

    def India_index():
        try:
            print("Scheduled task running at", datetime.now())
            summary = get_us_summary_ticket(type="INDIA",interval="1m", lookback_days=1)
            try:
                for id in load_Id():
                    bot.send_message(id, text=summary if summary else "No Updates Due to yesterday Indian Markets Holiday")
                    print(f"message is succesfully sended to {id} at ",datetime.now())
                print("ALL Indian market Updates are Succesfully sended to subcribed users")
            except ApiTelegramException as e:
                print(f"[Telegram API Error] {e}")
            except RequestException as e:
                print(f"[Network Error] Could not reach Telegram servers: {e}")
        except Exception as e:
            print(f"[Unhandled Error] in scheduled task: {e}")
            
    
    # Use BackgroundScheduler
    scheduler = BackgroundScheduler()
    scheduler.add_job(US_index, 'cron', hour=7, minute=00)  # Change to near-time for testing
    scheduler.add_job(Global_index,'cron',hour=8,minute=00)
    scheduler.add_job(India_index,'cron',hour=8,minute=30)
    scheduler.start()
    

    print("Scheduler started in background. Bot polling started. Press Ctrl+C to stop.")

    try:
        bot.polling(non_stop=True, interval=0)
        print("Polling started")
    except KeyboardInterrupt:
        print("\nShutdown requested. Stopping scheduler and bot.")
        scheduler.shutdown()
        sys.exit(0)
    except Exception as e:
        print(f"[Polling Error] {e}")
        scheduler.shutdown()
        sys.exit(1)
