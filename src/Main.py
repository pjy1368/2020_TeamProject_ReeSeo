from Account import Account
from StartScreen import startScreen
from Init import login
from Menu import menu
import os

account = Account()

while(True):
    startScreen()
    
    if not login(account):
        continue
    else:
        os.system('cls')
        if menu(account):
            break
        else:
            continue 