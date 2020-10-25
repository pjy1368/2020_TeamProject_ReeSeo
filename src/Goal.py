import os
class Goal:
    def __init__(self, account):
        if self.isGoal():
            filePath = "./user/profile.txt"
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
        filePath = "./user/profile.txt"
        f = open(filePath, "w")
        while True:
            print("<Setting goal term>")
            print("Enter the goal term")
            print("(Enter a natural number from 1 to 30 for the goal term) : ")
            term = int(input("-> "))
            if (type(term) is int and term > 0):
                if (term >= 1 and term <= 30):
                    f.write(str(term) + "\n")
                    break
                else:
                    print("Enter a natural number from 1 to 30 for the goal term.")
            else:
                print("Term must be entered as a natural number.")

        maxCalories = 0
        if account.gender == "Male":
            maxCalories = (float(account.weight) * 10) * 1.2
        else:
            maxCalories = (float(account.weight) * 10) * 0.8

        print("<Setting goal calories>")
        print("The maximum daily calorie is " + str(maxCalories) + " kcal. Please enter the goal daily calorie.") 
        print("The integer part of the value must be at least 2 digits and the decimal part must be 2 digits. At this point, the integer part must be positive")
        calories = input("-> ")
        f.write(calories + "\n")

        f.close()
        self.__init__(account)
    
    # Delete goal.
    def delete(self):
        os.remove("./user/goal.txt")

    # Print goal.
    def view(self):
        filePath = "./user/profile.txt"
        f = open(filePath, 'r')

        print("<View goal>")
        print("Goal Term : " + self.term + " days\n")
        print("Goal daily calories : " + self.calories + " kcal\n")

        f.close()