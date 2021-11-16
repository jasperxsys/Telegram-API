import os
import telebot
import json

API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['greet'])
def greet(message):
    bot.reply_to(message, "Hey")
    print(message.chat.id)

@bot.message_handler(commands=['website'])
def greet(message):
    bot.reply_to(message, "www.example.nl")
    print(message.chat.id)

@bot.message_handler(commands=['members'])
def greet(message):
    if message.from_user.username != None:
        bot.send_message(message.chat.id, "Welcome " + message.from_user.username)
    elif message.from_user.first_name != None:
        bot.send_message(message.chat.id, "Welcome " + message.from_user.first_name)
    else:
        bot.send_message(message.chat.id, "Welcome " + message.from_user.last_name)


@bot.message_handler(commands=['token'])
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
    # print(struserIdJasper)
    # replaced_stridjasper = struserIdJasper.replace("False", "false")
    with open('data.json', 'a') as outfile:
        outfile.write(struserIdJasper + "\n")
        # outfile.write(replaced_stridjasper + "\n")
    


def username(message):
    if(message.text == "test"):
        return True
    else:
        return False


@bot.message_handler(func=username)
def send_username(message):
    bot.send_message(message.chat.id, message.from_user.id)
    get_members = bot.get_chat_members_count(message.chat.id)
    # for i in range (get_members):
    #     print(i)
    # print(bot.get_chat_member(-619751024, 1236443148))

@bot.message_handler(content_types=['new_chat_members', 'left_chat_member'])
def bot_func(message):
    user_id = message.from_user.id
    bot.send_message(message.chat.id, message.from_user.id)
    joined_user_id = bot.get_chat_member(message.chat.id, user_id)
    string_joined_user_id = str(joined_user_id)
    print(string_joined_user_id)
    with open('data.json', 'a') as outfile:
        outfile.write(string_joined_user_id + "\n")

@bot.message_handler(content_types=['new_chat_members'])
def welcome_function(message):
    bot.send_message(message.chat.id)


bot.polling() 