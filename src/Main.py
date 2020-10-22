from Account import Account
from StartScreen import startScreen
from Init import login
from Menu import menu

account = Account()

while(True):
    startScreen()
    
    if not login(account):
        continue
    else:
        menu(account)
        
    break