import os
import re
class Goal:
    def __init__(self, account):
        if self.isGoal():
            filePath = "./user/goal.txt"
            f = open(filePath, "r")
            s = f.readlines()
        
            self.term = s[0].split('\n')[0]
            self.calories = s[1].split('\n')[0]

            f.close()
        else:
            self.term = None
            self.calrories = None

    # Does the goal exist?
    def isGoal(self):
        return os.path.isfile("./user/goal.txt")

    # Set goal.
    def setGoal(self, account):
        filePath = "./user/goal.txt"
        f = open(filePath, "w")
        while True:
            print("<Setting goal>")
            print("Enter the goal term")
            print("(Enter a natural number from 1 to 30 for the goal term) : ")
            term = input("-> ")

            if len(term) < 1 or len(term) > 2:
                print("Enter a natural number from 1 to 30 for the goal term.")
                input()
                os.system('cls')
                continue

            p = re.search(r'^[0-9]{1,2}$', term)

            if not p:
                print("Enter a natural number from 1 to 30 for the goal term.")
                input()
                os.system('cls')
                continue
            
            f.write(term + "\n")
            os.system('cls')
            break

        maxCalories = 0
        if account.gender == "Male":
            maxCalories = (float(account.weight) * 10) * 1.2
        else:
            maxCalories = (float(account.weight) * 10) * 0.8

        while True:
            print("<Setting goal>")
            print("The maximum daily calorie is " + str(maxCalories) + " kcal. Please enter the goal daily calorie.") 
            print("The integer part of the value must be at least 2 digits and the decimal part must be 2 digits. At this point, the integer part must be positive")
            calories = input("-> ")

            if len(calories) < 5:
                print("The integer part of the value must be at least 2 digits and the decimal part must be at 2 digits.")
                print("At this point, the integer part must be positive.")
                input()
                os.system('cls')
                continue

            if calories.find('.') == -1 or len(calories.split('.')[0]) < 2 or len(calories.split('.')[1]) != 2:
                print("Illegal form of calories. Calories is consisted with at least 2 integer and 2 decimal classified with '.'.")
                input()
                os.system('cls')
                continue

            if int(calories.split('.')[0]) < 10:
                print("Integer part of calories must be 10 or more.")
                input()
                os.system('cls')
                continue

            if float(calories) > maxCalories:
                print("The maximum daily calorie must not be exceeded.")
                input()
                os.system('cls')
                continue
            
            
            f.write(str(float(calories)) + "\n")
            os.system('cls')
            break

        f.close()
        self.__init__(account)
    
    # Delete goal.
    def delete(self):
        os.remove("./user/goal.txt")

    # Print goal.
    def view(self):
        filePath = "./user/goal.txt"
        f = open(filePath, 'r')

        print("<View goal>")
        print("Goal Term : " + self.term + " days\n")
        print("Goal daily calories : " + self.calories + " kcal\n")

        f.close()