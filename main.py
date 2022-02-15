import requests
import telebot
from time import sleep
token = ('5101939611:AAEEzDh10igGYqLebPa3C4f36F4uFyj7UuA')
sudo = ("232431305")
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    first = message.from_user.first_name
    bot.send_message(message.chat.id,text=f"<strong>اهلا بك في بوت سايت ارسل رسالتك الان. \n\nBy @EngM9 - @lwolfl</strong>",parse_mode="html")
@bot.message_handler(func=lambda m: True)
def Get(message):
    msg = message.text 
    bot.send_message(message.chat.id,f"<strong>تم ارسال رسالتك للأدمن.</strong>",parse_mode="html")
    bot.forward_message(sudo,message.chat.id,message.message_id)
    
pass

bot.polling(True)