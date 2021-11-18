import os
import telebot
import csv

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
    else:
        bot.send_message(message.chat.id, "Welcome " + message.from_user.first_name)

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
    
@bot.message_handler(commands=['test'])
def test(message):
    # bot.send_message(message.chat.id, "testtest")
    user_id = message.from_user.id
    user_firstname = message.from_user.first_name
    user_lastname = message.from_user.last_name
    user_username = message.from_user.username
    arrayuser = [user_id,user_username, user_firstname, user_lastname]
    for i in range(len(arrayuser)):
        if arrayuser[i] == None:
            arrayuser[i] = "None"
    header = ["id", "username", "firstname", "lastname"]
    with open('data.csv', 'a') as file:
        writer = csv.writer(file)
        if file.tell() == 0:
            writer.writerow(header)
        writer.writerow(arrayuser)  
        file.close()



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
@bot.message_handler(content_types=['new_chat_members'])
def welcome_function(message):
    print("joined")
    status = "Joined"
    if message.from_user.username != None:
        bot.send_message(message.chat.id, "Welcome " + message.from_user.username)
    else:
        bot.send_message(message.chat.id, "Welcome " + message.from_user.first_name)
    bot_func(message, status)

@bot.message_handler(content_types=['left_chat_member'])
def welcome_function(message):
    print("left")
    status = "Left"
    bot_func(message, status)

@bot.message_handler(content_types=['new_chat_members', 'left_chat_member'])
def bot_func(message, status):
    print("csv func")
    print(status)
    user_id = message.from_user.id
    user_firstname = message.from_user.first_name
    user_lastname = message.from_user.last_name
    user_username = message.from_user.username
    arrayuser = [user_id,user_username, user_firstname, user_lastname, status]
    for i in range(len(arrayuser)):
        if arrayuser[i] == None:
            arrayuser[i] = "None"
    header = ["id", "username", "firstname", "lastname", "status"]
    with open('data.csv', 'a') as file:
        writer = csv.writer(file)
        if file.tell() == 0:
            writer.writerow(header)
        writer.writerow(arrayuser)  
        file.close()


bot.infinity_polling(timeout=10, long_polling_timeout = 5) 