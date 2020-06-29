#!/usr/bin/env python3

import telebot
import random
import os 


bot = telebot.TeleBot('1271165453:AAGo0GurGxQQX2VhkcWN4afVW5D6Of-LuLc')

phrases = []

with open("./phrases", 'r') as f:
    filecontents = f.readlines()
    for line in filecontents:
        current_place = line[:-1]
        phrases.append(current_place)
print(phrases)

def randomMessage():
    max = len(phrases)
    message = phrases[random.randrange(0, max + 1)]
    return message

@bot.message_handler(commands=['start', 'ромашка', 'romashka', 'цветок', 'кактус'])
def start_message(message):
    rndm_message = randomMessage()
    bot.send_message(message.chat.id, rndm_message)

@bot.message_handler(commands=['update'])
def update_prases(message):
    os.popen('/opt/bot/get_phrases.py')
    bot.send_message(message.chat.id, str(phrases))

@bot.message_handler(content_types=['text'])
def start_message(message):
    rndm_message = randomMessage()
    if 'ромашк' in message.text.lower():
        bot.send_message(message.chat.id, rndm_message)
    if 'мудак' in message.text.lower():
        bot.send_message(message.chat.id, "Сам ты мудак %s,иди работать!" % message.from_user.first_name)
    if 'хуев' in message.text.lower() or 'хуёв' in message.text.lower():
        bot.send_message(message.chat.id, 'ТААЧКААА')

bot.polling()
