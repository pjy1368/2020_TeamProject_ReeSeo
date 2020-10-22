def login(account):
    if account.isMember():
        print("1. Clear account")
        print("2. Use an existing account")

        sel = input("=> ")

        if sel == "1":
            account.clear()
            return False
        elif sel == "2":
            return True
        else:
            print("Invalid input")
    else:
        print("1. Create account")
        print("2. Move to start screen")

        sel = input("=> ")

        if sel == "1":
            account.create()
            return True
        elif sel == "2":
            return False
        else:
            print("Invalid input")

