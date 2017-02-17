import config
import telebot
import psutil
import re
import os

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=["status"])
def provide_status(message):
    bot.send_message(message.chat.id, "I'm OK!")
    bot.send_message(message.chat.id, 'Chat ID is ' + str(message.chat.id))

@bot.message_handler(commands=["sys"])
def provide_status(message):
    cpu = psutil.cpu_percent(5.0, True)
    mem = psutil.virtual_memory()
    bot.send_message(message.chat.id, "CPU - {0}%".format(str(cpu)))
    bot.send_message(message.chat.id, "MEM (U/A/T) - {0}M/{1}M/{2}M".format(str(round(mem.used / 1024 / 1024, 2)),
                                                                    str(round(mem.available / 1024 / 1024, 2)),
                                                                    str(round(mem.total / 1024 / 1024, 2))))

@bot.message_handler(commands=["bash"])
def provide_status(message):
    cmd = re.search('\/bash (.*)', message.text).group(1)
    res = os.popen(cmd).read()
    bot.send_message(message.chat.id, "Command: " + cmd)
    bot.send_message(message.chat.id, res)


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
   bot.send_message(message.chat.id, message.text)
   print(message.text)

bot.send_message(config.chat_id, "Re/Started.")

if __name__ == '__main__':
    bot.polling(none_stop=True)