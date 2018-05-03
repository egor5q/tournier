# -*- coding: utf-8 -*-
import os
import telebot
import time
import telebot
import random
import threading
from emoji import emojize
from telebot import types

token = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['rules'])
def rules(m):
  bot.send_message(m.chat.id, 'Правила проведения турнира:\nВ каждой партии играют 3 команды по 4 человека, у которых для удобства есть свои чат и капитан. Выигрывает та команда, чьи игроки остались в конце партии в живых (или чьих игроков больше), или та команда, чьего суика линчевали. Таким образом, всевозможный руин, как линч пруфа и кросфак - обязательны для данного вида турнира, так как побеждает именно команда, а не один игрок.')


@bot.message_handler(commands=['addteam'])
def dd(m):
  pass
  
  
if __name__ == '__main__':
  bot.polling(none_stop=True)

