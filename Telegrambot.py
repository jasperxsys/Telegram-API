import os
import telebot
import csv
import datetime

API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)
    
@bot.message_handler(content_types=['new_chat_members'])
def welcome_function(message):
    status = "Joined"
    bot_func(message, status)

@bot.message_handler(content_types=['left_chat_member'])
def leave_function(message):
    status = "Left"
    bot_func(message, status)

@bot.message_handler(content_types=['new_chat_members', 'left_chat_member'])
def bot_func(message, status):
    user_id = message.from_user.id
    user_firstname = message.from_user.first_name
    user_lastname = message.from_user.last_name
    user_username = message.from_user.username
    user_timestamp = datetime.datetime.now()
    user_timestamp_string = user_timestamp.strftime("%d-%b-%Y (%H:%M:%S)")
    arrayuser = [user_id,user_username, user_firstname, user_lastname, status, user_timestamp_string]
    for i in range(len(arrayuser)):
        if arrayuser[i] == None:
            arrayuser[i] = "N/A"
    header = ["id", "username", "firstname", "lastname", "status", "timestamp"]
    with open('data.csv', 'a') as file:
        writer = csv.writer(file)
        if file.tell() == 0:
            writer.writerow(header)
        writer.writerow(arrayuser)  
        file.close()

bot.infinity_polling(timeout=10, long_polling_timeout = 5) 