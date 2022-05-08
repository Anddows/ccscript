import time 
from colorama import init
from termcolor import colored
import os

init()

create_t = ["{c = telethon.python}", 'c = telethon.python']
i_time = ["{i = time}", "i = time"]
t_sleep = ["{t = sleep}", "t = sleep"]
apiid = ["{bot == api > id}", "bot == api > id"]
apihash = ["{bot == api > hash}", "bot == api > hash"]
write2 = ["{*write}", "*write"]
class1 = ["{c = class}", "c = class"]
func1 = ["{c = func}", "c = func"]
variable1 = ["{c = variable}", "c = variable"]
client = ["{bot == client}", "bot == client"]
client2 = ["{bot == on.client}", "bot == on.client"]
bot_if = ['{bot == if}', 'bot == if']
bot_send = ["{bot == send}", "bot == send"]
bot_reply = ["{bot == reply}", "bot == reply"]
bot_edit = ["{bot == edit}", "bot == edit"]
bot_elif = ["{bot == elif}", "bot == elif"]
bot_photo = ["{bot == photo}", "bot == photo"]
bot_photo_caption = ["{bot == photo.caption}", "bot == photo.caption"]
run = ["{bot.client > start}", "bot.client > start"]
bot_if_message = ["{bot == if.message}", "bot == if.message"]
bot_elif_message = ["{bot == elif.message}", "bot == elif.message"]

with open("colors.txt", "w") as f:
  f.write('green')
with open("colors.txt", "r+") as f:
  list = f.read()
print(colored("\n\nTelegram userbot creator\nCool Code Script 2.0\nby Code Idea\n\n", list))
while True:
            inpt = input('C*>_ ')
            inpt = inpt.strip()
            if inpt in create_t:
              try:
                os.mkdir("files")
              except:
                with open("colors.txt", "r+") as f:
                 list = f.read()
                print(colored('C*>_  Scanning...', list))
                with open("colors.txt", "r+") as f:
                 list = f.read()
              apiid1 = input("C*>_ your api id > ")    
              print(colored('{*>_} Scanning...', list))
              time.sleep(3)
              with open('bot.py', 'a') as f:
                 f.write(f"import time\nfrom telethon import TelegramClient, events, sync\napi_id = {apiid1}\n")
              apihash1 = input("C*>_  your api hash > ")
              with open('bot.py', 'a') as f:
                 f.write(f"api_hash = '{apihash1}'\nclient = TelegramClient('anon', api_id, api_hash)\n\n")

            elif inpt in client:
              with open("bot.py", "a") as f:
                f.write(f"@client.on(events.NewMessage)\nasync def my_event_handler(event):\n")

            elif inpt in bot_if:
              commandif = input("C*>_ ")
              with open("bot.py", "a") as f:
                f.write(f'   if "{commandif}" in event.raw_text:\n')

            elif inpt in bot_elif:
              commandelif = input("C*>_ ")
              with open("bot.py", "a") as f:
                f.write(f'   elif "{commandelif}" in event.raw_text:\n')

            elif inpt in bot_send:
              commandsend = input("C*>_ ")
              with open("bot.py", "a") as f:
                f.write(f'    await event.respond("{commandsend}")\n')

            elif inpt in bot_photo_caption:
              commandsendphotoid = input("C*>_ ")
              with open("bot.py", "a") as f:
               f.write(f'    await client.send_file({commandsendphotoid}, ')
              commandsendphoto = input("C*>_ ")
              with open("bot.py", "a") as f:
                f.write(f'"files/{commandsendphoto}",')
              commandcaption = input("C*>_ ")
              with open("bot.py", "a") as f:
                f.write(f'caption = "{commandcaption}")\n')

            elif inpt in bot_photo:
              commandsendphotoid = input("C*>_ ")
              with open("bot.py", "a") as f:
               f.write(f'   await client.send_file({commandsendphotoid}, ')
              commandsendphoto = input("C*>_ ")
              with open("bot.py", "a") as f:
                f.write(f'"files/{commandsendphoto}")')

              # caption = "CyberSecurity")\n'

            elif inpt in bot_edit:
              commandedit = input("C*>_ ")
              with open("bot.py", "a") as f:
                f.write(f'    await event.edit("{commandedit}")\n')

            elif inpt in bot_reply:
              commandreply = input("C*>_ ")
              with open("bot.py", "a") as f:
                f.write(f'    await event.reply("{commandreply}")\n')

            elif inpt in run:
              with open('bot.py', "a") as f:
                f.write("client.start()\nclient.run_until_disconnected()")


            else:
              with open("colors.txt", "r+") as f:
                list = f.read()
              print(colored(f'C*>_ CommandError: command <{inpt}> not defined', list))






