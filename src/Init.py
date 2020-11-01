import os

# returns True in the following cases:
# 1. use an existing account
# 2. create a new account

# returns False in the follwing cases:
# 1. clear account
# 2. move to start screen

def login(account):
    if account.isMember():
        while True:
            print("1. Clear account")
            print("2. Use an existing account")

            sel = input("=> ")

            if sel == "1":
                account.clear()
                return False
            elif sel == "2":
                os.system('cls')
                
                # Is the goal complete? 
                account.goal.isEnd(account)
                return True
            else:
                print("Digit 1, 2 allowed only.")
                input()
                os.system('cls')
        
    else:
        while True:
            print("Creating a new account? (1. yes 2. no)")
            sel = input("=> ")

            if sel == "1":
                os.system('cls')
                account.create([1, 2, 3, 4, 5, 6])
                print("Sign up completed." )
                input()
                os.system('cls')
                return True
            elif sel == "2":
                return False
            else:
                print("Digit 1 or 2 are allowed only.")
                input()
                os.system('cls')

