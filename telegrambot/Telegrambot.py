from ast import Str
import os
import telebot
import json

API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['Greet'])
def greet(message):
    bot.reply_to(message, "Hey")
    print(message.chat.id)

@bot.message_handler(commands=['Token'])
def greet(message):
    bot.send_message(message.chat.id, "STFY")
    user_id = message.from_user.id
    # print(bot.get_chat_member(message.chat.id, 1590974596))
    userIdJohn = bot.get_chat_member(message.chat.id, 1590974596)
    # print(bot.get_chat_member(message.chat.id, 1236443148))
    useridJasper = bot.get_chat_member(message.chat.id, 1236443148)
    struserIdJohn = str(userIdJohn)
    struserIdJasper = str(useridJasper)
    print(struserIdJasper)
    with open('data.json', 'a') as outfile:
        outfile.write(struserIdJasper + "\n")
    


def username(message):
    if(message.text == "test"):
        return True
    else:
        return False


@bot.message_handler(func=username)
def send_username(message):
    bot.send_message(message.chat.id, message.from_user.id)
    print(bot.get_chat_members_count(message.chat.id))
    get_members = bot.get_chat_members_count(message.chat.id)
    # for i in range (get_members):
    #     print(i)
    # print(bot.get_chat_member(-619751024, 1236443148))

@bot.message_handler(content_types=['new_chat_members', 'left_chat_member'])
def bot_func(message):
    User_id = message.from_user.id
    bot.send_message(message.chat.id, message.from_user.id)
    
    




bot.polling() 