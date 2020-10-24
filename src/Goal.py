class Goal:
    def __init__(self):
        if self.isMember():
            filePath = os.path.join("./user", "goal.txt")
            f = open(filePath, "r")
            s = f.readlines()
        
            self.term = s[0].split('\n')[0]
            self.calories = s[1].split('\n')[0]

            f.close()
        else:
            self.term = None
            self.calrories = None

    def isMember(self):
        return os.path.isfile("./user/goal.txt")

    # Set goal.
    def setGoal(self):
        filePath = os.path.join("./user", "goal.txt")
        f = open(filePath, "w")

        print("<Setting goal>")
        print("Enter the goal term : ")
        term = input("(Enter a natural number from 1 to 30 for the goal term)")
        f.write(term + "\n")

        print("<Setting goal>")
        print("The maximum daily calorie is" + "AAA" + " kcal. Please enter the goal daily calorie.") # AAA = kg * 10 * x kcal
        calories = input("The integer part of the value must be at least 2 digits and the decimal part must be 2 digits. At this point, the integer part must be positive.")
        
        f.write(calories + "\n")

        f.close()
        self.__init__()
    
    # Delete goal.
    def delete(self):
        os.rmdir("./user/goal.txt")

    # Print goal.
    def view(self):
        filePath = os.path.join("./user", "goal.txt")
        f = open(filePath, 'r')

        print("<View goal>")
        print("Goal Term : " + self.term + " days\n")
        print("Goal daily calories : " + self.calories + " kcal\n")

        f.close()