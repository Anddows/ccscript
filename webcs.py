import time 
from colorama import init
from termcolor import colored
import os

init()

c_web = ['{c = post}', "c = post"]
s_image = ['{s == image}', "s == image"]
s_text1 = ['{s == text1}', "s == text1"]
s_text1_bold = ['{s == text1.bold}', "s == text1.bold"]
s_text = ["{s == text}", 's == text']


with open("colors.txt", "w") as f:
  f.write('green')
with open("colors.txt", "r+") as f:
  list = f.read()
print(colored("\nWeb post creator\nWeb Code Script 1.0\nby Code Idea\n\n", list))

time.sleep(5)

try:
    clear = lambda: os.system('cls')
    clear()
except:
    clear = lambda: os.system('clear')
    clear()

while True:
            inpt = input('w*>_ ')
            inpt = inpt.strip()
            if inpt == 'deploy':
                deploy = lambda: os.system('git init')
                deploy()
                time.sleep(5)
                commandfilename = input('w*>_ ')
                deploy2 = lambda: os.system(f'git add {commandfilename}')
                deploy2()
                time.sleep(5)
                deploy3 = lambda: os.system('git commit -m "deploy"')
                deploy3()

                time.sleep(5)
                deploy4 = lambda: os.system('git remote add origin https://github.com/Anddows/Anddows.github.io.git')
                deploy4()

                time.sleep(5)
                deploy5 = lambda: os.system('git push -u origin master')
                deploy5()

                time.sleep(5)
                deploy6 = lambda: os.system('git pull --rebase origin master')
                deploy6()

                time.sleep(5)
                deploy7 = lambda: os.system('git commit "deploy"')
                deploy7()

                time.sleep(5)
                deploy8 = lambda: os.system('git push origin master')
                deploy8()

                time.sleep(5)
                deploy9 = lambda: os.system('git status')
                deploy9()

                time.sleep(5)
                deploy10 = lambda: os.system('git reflog')
                deploy10()

            elif inpt == 'deploy image':
                deploy = lambda: os.system('git init')
                deploy()
                time.sleep(5)
                commandimagename = input('w*>_ ')
                deploy2 = lambda: os.system(f'git add {commandimagename}')
                deploy2()
                time.sleep(5)
                deploy3 = lambda: os.system('git commit -m "deploy"')
                deploy3()

                time.sleep(5)
                deploy4 = lambda: os.system('git remote add origin https://github.com/Anddows/Anddows.github.io.git')
                deploy4()

                time.sleep(5)
                deploy5 = lambda: os.system('git push -u origin master')
                deploy5()

                time.sleep(5)
                deploy6 = lambda: os.system('git pull --rebase origin master')
                deploy6()

                time.sleep(5)
                deploy7 = lambda: os.system('git commit "deploy"')
                deploy7()

                time.sleep(5)
                deploy8 = lambda: os.system('git push origin master')
                deploy8()

                time.sleep(5)
                deploy9 = lambda: os.system('git status')
                deploy9()

                time.sleep(5)
                deploy10 = lambda: os.system('git reflog')
                deploy10()


            elif inpt == "w = clear":

                try:
                    clear = lambda: os.system('cls')
                    clear()
                except:
                    clear = lambda: os.system('clear')
                    clear()

            elif inpt in c_web:
                commandid = input('*>_ your id > ')
                with open(f'{commandid}.html', 'a') as f:
                    f.write('<!DOCTYPE html>\n<html>\n<head>\n<meta charset="UTF-8">\n  <meta http-equiv="X-UA-Compatible" content="IE=edge">\n<meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">\n   <link rel="stylesheet" href="https://Anddows.github.io/style.css">\n')
                commandtitle = input('*>_ title > ')
                with open(f'{commandid}.html', 'a') as f:
                    f.write(f'<title>{commandtitle}</title>\n</head>\n<body>\n<center>\n    <div class="card">\n')

                commandposttitle = input('*>_ title > ')
                with open(f'{commandid}.html', 'a') as f:
                    f.write(f'<h1 class="text1"><b>{commandposttitle}</b></h1>\n')

                author = input('*>_ author > ')
                with open(f'{commandid}.html', 'a') as f:
                    f.write(f'    <h4 class="author">{author}</h3>\n</div>\n')

            elif inpt in s_image:
                commandimage = input('*>_ your image > ')
                with open(f'{commandid}.html', 'a') as f:
                    f.write(f'   <img src="{commandimage}" width="auto" height="auto">\n <div class="card">\n')

            elif inpt in 's == web.title':
                commandtitle2 = input('*>_ title > ')
                with open(f'{commandid}.html', 'a') as f:
                    f.write(f'    <h1 class="text1">{commandtitle2}</h1>\n')

            elif inpt in s_text:
                commandtext = input('*>_ your text > ')
                with open(f'{commandid}.html', 'a') as f:
                    f.write(f'    <h3 class="text-simply">{commandtext}</h3>\n</div>\n</center>\n</body>\n</html>')

            else: 
                print("error")
