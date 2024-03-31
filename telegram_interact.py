import telegram
import asyncio
import os
import text_to_speech

chat_message='Ladd and Lala want to chat! Give us a call!'

# send a message to a user
def message_user(api_key, chat_id):
    bot = telegram.Bot(token=api_key)
    asyncio.run(bot.send_message(chat_id=chat_id, text=chat_message))

def send_message(api_key, id, message):
    message_user(api_key, id)
    text_to_speech.speak(message)