import config
import telebot

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=["status"])
def provide_status(message):
    bot.send_message(message.chat.id, "I'm OK!")
    bot.send_message(message.chat.id, 'Chat ID is ' + str(message.chat.id))

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, message.text)
    print(message.text)

bot.send_message(config.chat_id, "Re/Started.")

if __name__ == '__main__':
    bot.polling(none_stop=True)

