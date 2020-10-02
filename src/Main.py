from Account import Account

account = Account()

if account.isMember():
    print("1. Clear account")
    print("2. Use an existing account")

    sel = input("=> ")

    if sel == "1":
        account.clear()
    elif sel == "2":
        print("Move to main prompt")
    else:
        print("Invalid input")
else:
    print("1. Create account")
    print("2. Move to title menu")

    sel = input("=> ")

    if sel == "1":
        account.create()
    elif sel == "2":
        print("Move to title menu")
    else:
        print("Invalid input")

