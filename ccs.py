import time 
from colorama import init
from termcolor import colored
import os

init()

print(colored("=== CCScript 2.0 [beta] ===\n", "magenta"))
print(colored("[1]", "red"), colored("Help", "green"))
print(colored("[2]", "red"), colored("Set matrix", "green"))
print(colored("[3]", "red"), colored("Edit Matrix", "green"))
print(colored("[4]", "red"), colored("Registration\n", "green"))
print(colored("===", "magenta"), colored("WhiteSecurityTeam", "white"), colored("===\n", "magenta"))

command_1 = ["1"]
command_2 = ["2"]
command_3 = ["3"]
command_4 = ["4"]

matrix_start = ["$ start matrix $"]

matrix_end = ["$ matrix end $"]

while True:
            inpt = input(':$ > ')
            inpt = inpt.strip()
            if inpt in command_1:
                print(colored("===", "green"), colored("Help", "magenta"), colored("===\n", "green"))
                print(colored(":$ > commands:", "green"))
                print(colored(":$ > $ start matrix $", "green"))
                print(colored(":$ > $ edit: your text for eding(playing...)", "green"))
                print(colored(":$ > $ matrix end $ ", "green"))
                print(colored(":$ > ctrl + d or ctrl + c and python bot.py", "green"))

            elif inpt in command_2:
                marix_1 = input(":$ > 1 - matrix: ")
                with open("bot.py", "a") as f:
                    f.write(f'   if event.raw_text in event.raw_text:\n')
                with open("bot.py", "a") as f:
                    f.write(f'    await event.edit("{marix_1}")\n')
                marix_2 = input(":$ > 2 - matrix: ")
                with open("bot.py", "a") as f:
                    f.write(f'    await event.edit("{marix_2}")\n')
                marix_3 = input(":$ > 3 - matrix: ")
                with open("bot.py", "a") as f:
                    f.write(f'    await event.edit("{marix_3}")\n')
                marix_4 = input(":$ > 4 - matrix: ")
                with open("bot.py", "a") as f:
                    f.write(f'    await event.edit("{marix_4}")\n')
                with open("bot.py", "a") as f:
                    f.write(f'    time.sleep(1)\n')
                with open("bot.py", "a") as f:
                    f.write(f'    await event.edit(event.raw_text)\n')
                with open('bot.py', "a") as f:
                    f.write("client.start()\nclient.run_until_disconnected()")


                print(colored(":$ > Success! matrix is installed! ", "green"))

            elif inpt in command_3:
                print(colored("[log]: [3] Not working in the beta version", "red"))

            elif inpt in command_4:
                api_id = input(":$ > Api id: ")
                with open('bot.py', 'a') as f:
                    f.write(f"import time\nfrom telethon import TelegramClient, events, sync\napi_id = {api_id}\n")
                api_hash = input(":$ > Api hash: ")
                with open('bot.py', 'a') as f:
                    f.write(f"api_hash = '{api_hash}'\nclient = TelegramClient('anon', api_id, api_hash)\n\n")
                with open("bot.py", "a") as f:
                    f.write(f"@client.on(events.NewMessage)\nasync def my_event_handler(event):\n")
                print(colored(":$ > Success! choose [2]", "green"))
                ### [2] \

            elif inpt in matrix_start:
                with open("bot.py", "a") as f:
                    f.write(f'   if event.raw_text in event.raw_text:\n')

            # elif inpt == "$ elif.text":
            #     with open("bot.py", "a") as f:
            #         f.write(f'   elif event.raw_text in event.raw_text:\n')

            elif inpt.startswith("$ edit: "):
                with open("bot.py", "a") as f:
                    f.write(f'    await event.edit("{inpt[8:]}")\n')


            elif inpt in matrix_end:
              with open("bot.py", "a") as f:
                f.write(f'    time.sleep(1)\n')
              with open("bot.py", "a") as f:
                f.write(f'    await event.edit(event.raw_text)\n')
              with open('bot.py', "a") as f:
                f.write("client.start()\nclient.run_until_disconnected()")
                print(colored(":$ > Success!", "green"))

            elif inpt.startswith(" m end $"):
              with open("bot.py", "a") as f:
                f.write(f'    time.sleep(1)\n')
              with open("bot.py", "a") as f:
                f.write(f'    await event.edit("{inpt[:0]} " + event.raw_text)\n')
              with open('bot.py', "a") as f:
                f.write("client.start()\nclient.run_until_disconnected()")
                print(colored(":$ > Success!", "green"))




                print(f'{inpt[5:]}')
