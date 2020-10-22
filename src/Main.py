from Account import Account
from Init import login
from Menu import menu

account = Account()

while(True):
    #StartScreen.
    print("StartScreen")
    #InitMenu. -> return False : continue, return True : Menu
    if not login(account):
        continue
    else:
        menu(account)
    break