import time
import telebot

bot = telebot.TeleBot("1241504520:AAFfY_vbAFmfW_BbGwDEFT-NwL_9C9FMl8k")

keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Tell me, what\'s the time?', 'I wanna have time notifications')

keyboard2 = telebot.types.ReplyKeyboardMarkup(True)
keyboard2.row('Stop sending', 'Back')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Hi, " + message.chat.first_name + ", what can I do for you?", reply_markup=keyboard1)

def notifications(message):
    global notifs
    notifs = True
    while notifs == True:
        time.sleep(2)
        bot.send_message(message.chat.id, "Test")
        if notifs == False:
            break

def end_notifications(message):
    global notifs
    notifs = False


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'tell me, what\'s the time?':
        bot.send_message(message.chat.id, time.strftime("%c"))

    elif message.text.lower() == 'i wanna have time notifications':
        bot.send_message(message.chat.id, "Okay than", reply_markup=keyboard2)
        notifications(message)

    elif message.text.lower() == 'stop sending':
        bot.send_message(message.chat.id, "I got you")
        end_notifications(message)
    elif message.text.lower() == 'back':
        bot.send_message(message.chat.id, "You\'re welcome!", reply_markup=keyboard1)

    else:
        bot.send_message(message.chat.id, "I\'m not prepared for it yet")



bot.polling()