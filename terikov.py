import sys
import markovify
import telepot
import json
import random
import os
import time
import datetime
from telepot.loop import MessageLoop

bot = telepot.Bot('5484813771:AAHjwPr70E7lNBUj1GBsHN6XvpUJQuFHy0s')

if not os.path.exists('luzy.json'):
    with open('luzy.json', 'w') as f:
        json.dump({}, f)

swears = []
drug_names = []
last_used_loli = {}
def on_msg(msg):
    content_type, chat_type, chat_id, msg_date, msg_id = telepot.glance(msg, long=True)
    global last_used_loli
    '''
    if content_type != "text":
        return
    '''
    if "text" in msg:
        for drug_name in drug_names:
            if drug_names is not None and content_type == "text" and drug_name in msg["text"].lower():
                bot.sendMessage(chat_id, "DUDE WEED LMAO", reply_to_message_id=msg_id)
                return
        if content_type == "text" and "love live" in msg["text"].lower():
            bot.sendMessage(chat_id, "rabu rabu grr", reply_to_message_id=msg_id)
            return
        if content_type == "text" and "honkai impact" in msg["text"].lower():
            bot.sendMessage(chat_id, "honki honki grr", reply_to_message_id=msg_id)
            return
        if content_type == "text" and "under" in msg["text"].lower():
            bot.sendMessage(chat_id, "undertale", reply_to_message_id=msg_id)
            return
        if content_type == "text" and "loli" in msg["text"].lower():
            from_id = msg["from"]["id"]              # get the ID of message sender
            cooldown = datetime.timedelta(minutes=1) # the cooldown as a deltatime object (difference between two times)

            # if the last command use by this user happened less than <cooldown> ago, ignore the command
            if from_id in last_used_loli and last_used_loli[from_id] > (datetime.datetime.now() - cooldown):
                return
            last_used_loli[from_id] = datetime.datetime.now() # store the current time in the dictionary for later use
            bot.sendMessage(chat_id, "una *LOLI* \U0001F440 ", parse_mode='Markdown', reply_to_message_id=msg_id)
            return
        if content_type == "text" and "nigger" in msg["text"].lower():
            if msg["from"]["username"] == "tsuchitsu":
                bot.sendMessage(chat_id, "hello", reply_to_message_id=msg_id)
            else:
                bot.sendMessage(chat_id, "No niggers please", reply_to_message_id=msg_id)
        #print(msg["from"]["username"]+": "+msg["text"])
        if msg["text"].lower() == "teri cuantos mensajes?":
            with open("luzy.json", "r") as f:
                luzyjson = json.loads(f.read())
                bot.sendMessage(chat_id, "uhh son "+str(len(luzyjson["messages"])))
            return
    if content_type == 'text':
        if "username" in msg["from"] and msg['from']['username'] == 'tsuchitsu':
            with open('luzy.json', "r+") as f:
                luzyjson = json.loads(f.read())
                if "messages" not in luzyjson:
                    luzyjson["messages"] = []
                luzyjson["messages"].append(msg["text"])
                f.seek(0)
                f.truncate()
                json.dump(luzyjson, f, indent=2)
        if random.uniform(0.0, 1.0) < 0.00:
            random.choice([luzytf,luzymeme])(msg)
        elif msg['text'].lower() == 'teri' or msg['text'].lower() == 'blort':
            luzymeme(msg)

def luzytf(msg):
    content_type, chat_type, chat_id, msg_date, msg_id = telepot.glance(msg, long=True)
    bot.sendMessage(chat_id, 'teri', reply_to_message_id=msg_id)

def luzymeme(msg):
    print(msg)
    content_type, chat_type, chat_id = telepot.glance(msg)
    luzylist = []
    with open('luzy.json') as l:
        luzylist = json.loads(l.read())["messages"]
        # print(f"luzylist equals {luzylist}")
    luzystring = '\n'.join(luzylist)
    print(f"luzystring equals {luzystring}")
    for i in range(0, 10):
        luzy_model = markovify.NewlineText(luzystring, state_size=2)
        print(f"luzy_model equals {luzy_model}")
        if luzy_model is not None:
            break
    luzy_message = luzy_model.make_short_sentence(300)
    print(f"luzy_message equals {luzy_message}")
    if luzy_message is not None:
        bot.sendMessage(chat_id, luzy_message+"\n"+" - Casio")
        print(luzy_message)

MessageLoop(bot, on_msg).run_as_thread()
print('Started...')
while 1:
    time.sleep(10)
