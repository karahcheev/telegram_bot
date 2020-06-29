#!/usr/bin/env python3

import telebot
import random
import os 
bot = telebot.TeleBot('1271165453:AAGo0GurGxQQX2VhkcWN4afVW5D6Of-LuLc')

phrases_back = [
    "ПАРНИ НУ ВЫ ЧЕГО!",
    "Ух я щас хуёв навтыкаю.",
    "Сделай фото.",
    "ДД!",
    "А кто такой Кочетов?",
    "Какая фамилия у Кузовникова?", 
    "ТАААЧКААА",
    "Ну вот представь ты тачку себе купил, а там что-то не работает…",
    "Вот будет у тебя свой бизнесс.",
    "ПАРНИ!",
    "*Шутка про горшок*",
    "Это же ВИП!!!!",
    "Удели 10 минут своего драгоценного времени.",
    "Сделаем, сегодня!",
    "Мы команда!",
    "Держим планку.",
    "А сколько калорий в курице?..",
    "КТО ТАКОЙ КОЧЕТОВ???",
    "Алкоголь - это как секс, 1 раз попробовал и уже тяжело отказаться.",
    "Возьми в работу.",
    "Чиркани мне все это письмом",
    "Мне нравится как ты кроссируешь.",
    "Я хочу видеть твои губы…",
    "Если я прошу - надо сделать без лишних вопросов.",
    "Развели тут пиздежь!",
    "А где Кирилл?",
    "Много не пейте",
    "Николай, как работается?",
    "Приглашалку закинул.",
    "А давайте вы будете работать на час больше.",
    "Бизнес должен видеть что мы работаем",
    "Владику позвони.",
    "Кроме тебя это никто лучше не сделает.",
    "Сколько времени тебе надо, чтобы ответить сколько времени тебе надо...",
    "Сколько времени тебе надо?",
    "Вы мне нормально можете объяснить??",
    "Автомастерская, слушаю вас!",
    "Нам это даже выгодно",
    "Чудес не бывает, копайте дальше",
    "Напомни мне что там по заявке №?",
    "На тесты возьму.",
    "Кто в теме?",
    "Набери мне срочно!",
    "Ждем расопряжения сверху",
    "Я постоянно пингую по этой теме",
    "Вопрос очень срочный!",
    "Мне Плетнёва ",
 ]

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

@bot.message_handler(content_types=['text'])
def start_message(message):
    rndm_message = randomMessage()
    if 'ромашк' in message.text.lower():
        bot.send_message(message.chat.id, rndm_message)

@bot.message_handler(commands=['update'])
def update_prases(message):
    os.popen('/opt/bot/get_phrases.py')
    bot.send_message(message.chat.id, str(phrases))


@bot.message_handler(commands=['мудак'])
def start_message(message):
    bot.send_message(message.chat.id, "Сам ты мудак %s,иди работать!" % message.from_user.first_name)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if 'хуев' in message.text.lower() or 'хуёв' in message.text.lower():
        bot.send_message(message.chat.id, 'ТААЧКААА')



bot.polling()
