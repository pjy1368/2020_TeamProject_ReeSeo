import os

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
        os.system('cls')
        
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
            print("You must enter a natural number from 1 to 7.")
            input()
            os.system('cls')
            continue

    
def viewAndModifyProfile(account):
    os.system('cls')
    account.view()
    print("Select the number of the item you want to modify.")
    print("(If multiple selections are made, please add a space between the number and the number).")
    print("(q : Back to Menu)")

    str = input("=> ")

    if str == 'q' or str == 'Q':
        os.system('cls')
        return True

    list = str.split(" ")
    for i in list:
        if len(i) != 1 or i < '1' or i > '6' or i == '4':
            print("Digit 1, 2, 3, 5, 6 allowed only")
            input()
            os.system('cls')
            return False

    list.sort()
    os.system('cls')
    account.revise(list)
    os.system('cls')

def viewAndModifyListOfExercise(account):
    ERR_MESSAGE = "An error occured. We'll load the previous page."
    workOut = account.workOut
    while True:
        sel = workOut.view()
        if sel == '1':
            workOutIndex = workOut.getWorkOutSelection()
            while True:
                sel2, index = workOut.viewWorkOut(workOutIndex)
                if sel2 == '1':
                    workOut.editWorkOut(index)
                elif sel2 == '2':
                    workOut.deleteWorkOut(index)
                    break
                elif sel2 == '3':
                    break
                else:
                    print(ERR_MESSAGE)
                    break
        elif sel == '2':
            workOut.addWorkOut()
        elif sel == '3':
            return
        else:
            input(ERR_MESSAGE)
            return

    




def analyzeMyExerciseRecord(account):
    print("This is analyze my exercise record")

def setAndViewMyExerciseGoal(account):
    if account.goal.isGoal():
        account.goal.view()
    else:
        account.goal.setGoal(account)

def subMitExerciseRecord(account):
    print("This is sumit today's exercise record")

