from Account import Account
from StartScreen import startScreen
from Init import login
from Menu import menu

print(1 == True)
import os
print(os.getcwd())
account = Account()

while(True):
    startScreen()
    
    if not login(account):
        continue
    else:
        if menu(account):
            break
        else:
            continue 