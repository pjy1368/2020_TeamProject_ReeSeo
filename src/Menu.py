def menu(account):
    while(True):
        print("<Main menu>")
        print("1. View and Modify Profile")
        print("2. View and Modify list of exercise")
        print("3. Analyze my exercise record")
        print("4. Set and View my exercise goal")
        print("5. Submit today's exercise record")
        print("6. To the start screen")
        print("7. Exit Program\n")
        
        sel = input("select menu : ")
        
        if sel == '1':
            while(True):
                if viewAndModifyProfile(account):
                    break
        elif sel == '2':
            viewAndModifyListOfExercise(account)
        elif sel == '3':
            analyzeMyExerciseRecord(account)
        elif sel == '4':
            setAndViewMyExerciseGoal(account)
        elif sel == '5':
            subMitExerciseRecord(account)
        elif sel == '6':
            return False
        elif sel == '7':
            return True
        else:
            continue

    
def viewAndModifyProfile(account):
    account.view()
    print("Select the number of the item you want to modify.")
    print("(If multiple selections are made, please add a space between the number and the number).")
    print("(q : Back to Menu)")

    str = input("=> ")

    if str == 'q' or str == 'Q':
        return True

    list = str.split(" ")
    for i in list:
        if len(i) >= 2:
            return False
        if i < '1' or i > '6':
            return False
    account.revise(list)

def viewAndModifyListOfExercise(account):
    print("This is viewAndModifyListOfExercise")
    account.workOut.print()
    




def analyzeMyExerciseRecord(account):
    print("This is analyze my exercise record")

def setAndViewMyExerciseGoal(account):
    if account.goal.isGoal():
        account.goal.view()
    else:
        account.goal.setGoal(account)

def subMitExerciseRecord(account):
    print("This is sumit today's exercise record")

