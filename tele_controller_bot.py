from telegram import *
from telegram.ext import *
import pyautogui as pg
import screen_brightness_control as sb
import os
import time
import requests

updater = Updater(token="2130495697:AAHtKcjz1pl2WKDuJ_go0l_f7OYuHKruyz8")
dispatcher = updater.dispatcher

allowedUsernames = ["roco_colaco"]


def startCommand(update: Update, context: CallbackContext):
    buttons = [[KeyboardButton("/SMART_LIGHTS")], [KeyboardButton("/Scroll")], [KeyboardButton("/Prime")],
               [KeyboardButton("/Netflix")], [KeyboardButton("▶/⏸")], [KeyboardButton("⟳")], [KeyboardButton("⟲")],
               [KeyboardButton("recent")], [KeyboardButton("Full Screen")], [KeyboardButton("Max")],
               [KeyboardButton("Min")], [KeyboardButton("Mute")], [KeyboardButton("Close")], [KeyboardButton("Unmute")]]
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to my bot!",
                             reply_markup=ReplyKeyboardMarkup(buttons))


def scroll(update: Update, context: CallbackContext):
    buttons = [[KeyboardButton("/start")], [KeyboardButton("▼")], [KeyboardButton("▲")]]
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome",
                             reply_markup=ReplyKeyboardMarkup(buttons))


def Netflix(update: Update, context: CallbackContext):
    buttons = [[KeyboardButton("/start")], [KeyboardButton("▶/⏸")], [KeyboardButton("⟳")], [KeyboardButton("⟲")]]
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome",
                             reply_markup=ReplyKeyboardMarkup(buttons))


def Prime(update: Update, context: CallbackContext):
    buttons = [[KeyboardButton("/start")], [KeyboardButton("▶/⏸")], [KeyboardButton("⟳")], [KeyboardButton("⟲")]]
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to Prime!",
                             reply_markup=ReplyKeyboardMarkup(buttons))


def smart_lights(update: Update, context: CallbackContext):
    buttons = [[KeyboardButton("/start")], [KeyboardButton("Off")], [KeyboardButton("On")]]
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to Prime!",
                             reply_markup=ReplyKeyboardMarkup(buttons))


def messageHandler(update: Update, context: CallbackContext):
    t = update.message.text
    if update.effective_chat.username not in allowedUsernames:
        context.bot.send_message(chat_id=update.effective_chat.id, text="You are not allowed to use this bot")

    elif "Off" == t:
        requests.get('https://api.voicemonkey.io/trigger?access_token=348b6dafd3a3329975f338103e71581a&secret_token'
                     '=66c4310a0ece27e097726b6856c5b4bd&monkey=lightsoff&announcement=Hello%20monkey')
    elif "SS" in t:
        if "show" in t.lower():
            pg.press('Win')
            pg.typewrite('C:\\Users\91967\Pictures\TG_BOT_SCREENSHOTS')
            pg.sleep(1)
            pg.press('enter')
        else:
            name = t.split()[1]
            try:
                pg.screenshot("C:/Users\91967\Pictures\TG_BOT_SCREENSHOTS/" + name)
            except:
                pg.screenshot("C:/Users\91967\Pictures\TG_BOT_SCREENSHOTS/" + name + ".png")

    elif "On" == t:
        requests.get('https://api.voicemonkey.io/trigger?access_token=348b6dafd3a3329975f338103e71581a&secret_token'
                     '=66c4310a0ece27e097726b6856c5b4bd&monkey=lights-on&announcement=Hello%20monkey')
    elif "▲" in t or "▼" in t:
        if "▲" == t:
            pg.vscroll(200)
        else:
            pg.vscroll(-200)

    elif "v" == t.lower()[0] and len(t.split()) == 2:
        v = t.split()[len(t.split()) - 1]
        os.system('SetVol ' + v)

    elif "b" == t.lower()[0] and len(t.split()) == 2:
        v = t.split()[len(t.split()) - 1]
        sb.set_brightness(v)

    elif "o " == t.lower()[0:2]:
        pg.press('win')
        time.sleep(2)
        pg.write(t.lower()[1:])
        pg.press('enter')
        time.sleep(10)
        if ('prime' in t.lower()):
            for i in range(4):
                pg.press('tab')

    elif "recent" in t:
        pg.keyDown('alt')
        pg.press('tab')
        pg.keyUp('alt')

    elif "▶/⏸" in t:
        pg.click()

    elif "Close" in t:
        pg.keyDown('alt')
        pg.press('f4')
        pg.keyUp('alt')
        pg.moveTo(850, 500)

    elif t == "shutdown":
        os.system('shutdown /s')
    elif t == "RESTART":
        os.system('shutdown /r')
    elif t == "SLEEP":
        os.system('rundll32.exe powrprof.dll, SetSuspendState Sleep')

    elif "Full Screen" in t:
        pg.press('f')

    elif "Min" in t:
        pg.keyDown('win')
        pg.press('down')
        pg.keyUp('win')

    elif "Max" in t:
        pg.keyDown('win')
        pg.press('up')
        pg.keyUp('win')


    elif "⟳" in t:
        pg.press("right")

    elif "⟲" in t:
        pg.press("left")

    elif "Mute" in t:
        os.system('SetVol 0')

    elif "Unmute" in t:
        os.system('SetVol 100')

    elif "enter" == t.lower() or "space" == t.lower() or "tab" == t.lower() or "win" == t.lower():
        pg.press(t.lower())

    elif "sw" in t.lower():
        pg.click(500, 330)
        pg.click(500, 330)


    else:
        pg.typewrite(t)
        time.sleep(1)
        pg.press('enter')


def queryHandler(update: Update, context: CallbackContext):
    query = update.callback_query.data
    update.callback_query.answer()


dispatcher.add_handler(CommandHandler("start", startCommand))
dispatcher.add_handler(CommandHandler("Netflix", Netflix))
dispatcher.add_handler(CommandHandler("Prime", Prime))
dispatcher.add_handler(CommandHandler("SMART_LIGHTS", smart_lights))
dispatcher.add_handler(CommandHandler("Scroll", scroll))
dispatcher.add_handler(MessageHandler(Filters.text, messageHandler))
dispatcher.add_handler(CallbackQueryHandler(queryHandler))

updater.start_polling()
