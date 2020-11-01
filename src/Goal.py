import os
import re
import math
from datetime import datetime
class Goal:
    def __init__(self, account):
        if self.isGoal():
            filePath = "./user/goal.txt"
            f = open(filePath, "r")
            s = f.readlines()

            self.startingDate = s[0].split('\n')[0]
            self.term = s[1].split('\n')[0]
            self.calories = s[2].split('\n')[0]

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
        

        while True:
            print("<Setting goal>")
            print("Enter the goal term")
            print("(Enter a natural number from 1 to 30 for the goal term)")
            term = input("-> ")

            if len(term) < 1 or len(term) > 2:
                print("Term must be entered as a natural number.")
                input()
                os.system('cls')
                continue

            p = re.search(r'^[0-9]{1,2}$', term)

            if not p:
                print("Term must be entered as a natural number.")
                input()
                os.system('cls')
                continue

            if int(term) < 1 or int(term) > 30:
                print("Enter a natural number from 1 to 30 for the goal term.")
                input()
                os.system('cls')
                continue
            
            os.system('cls')
            break

        maxCalories = 0
        if account.gender == "Male":
            maxCalories = (float(account.weight) * 10) * 1.2
        else:
            maxCalories = (float(account.weight) * 10) * 0.8

        output = "%0.2f" % maxCalories
        while True:
            print("<Setting goal>")
            print("The maximum daily calorie is " + str(output) + " kcal. Please enter the goal daily calorie.") 
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
            
            
            os.system('cls')
            break
        f = open(filePath, "w")
        f.write(account.currentDate + "\n")
        f.write(term + "\n")
        f.write(str(float(calories)) + "\n")
        f.close()
        self.__init__(account)

    
    # Print goal.
    def view(self):
        print("<View goal>")
        print("Starting Date : " + self.startingDate + "\n")
        print("Goal Term : " + self.term + " days\n")
        print("Goal daily calories : " + self.calories + " kcal")
        input()
        os.system('cls')

    # Verify that the goal is complete.            
    def isEnd(self, account):
        if self.isGoal():
            selfList = self.startingDate.split("-")
            pre = datetime(int(selfList[0]), int(selfList[1]), int(selfList[2]))

            accountList = account.currentDate.split("-")
            now = datetime(int(accountList[0]), int(accountList[1]), int(accountList[2]))

            
            if (now - pre).days == int(self.term):
                print("Goal is complete.\n")
                achievedDate = 0
                activity = account.activity
                dailyHistory = account.activity.dailyHistory
                for index, [date, timeInfos] in enumerate(dailyHistory):
                    dateWritten = activity.createDatetime(date)
                    if pre <= dateWritten < now:
                        consumption = activity.consumptionHistory[index]
                        goal = activity.goalHistory[index]
                        if consumption > goal:
                            achievedDate += 1
                achievementRate = (achievedDate / int(self.term)) * 100
                achievedRateOutput = "%0.2f" % achievementRate
                print(f"Your achievement rate is {achievedRateOutput}%")
                os.remove("./user/goal.txt")
                self.__init__(account)
        
