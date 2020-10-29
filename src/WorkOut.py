import os
import re
import math

class WorkOut:
    def __init__(self):
        
        # temporary variables for workout names
        TAKING_A_WALK = "taking a walk"
        GOING_FOR_A_RUN = "going for a run"
        RIDING_A_BIKE = "riding a bike"
        self.DEFAULT_WORKOUTS = [TAKING_A_WALK, GOING_FOR_A_RUN, RIDING_A_BIKE]

        # check if file exists
        self.filePath =  "./user/workout.txt"
        if os.path.isfile(self.filePath):
            f = open(self.filePath, "r")
            s = f.readlines()
            lines = [line[:-1] for line in s]
            
            # member constants for calorie ranges
            self.BELOW = "below"
            self.ABOVE = "above"

            # member variables
            self.RANGE = 10 # calorie range
            self.calorieRanges = [self.BELOW, "55", "65", "75", self.ABOVE]
            self.coefficient = [0.7, 0.8, 0.9, 1, 1.1]
            self.countCalories = 5
            self.limit = 10  # maximal number of workouts that can be in workOutList
            self.workOutList = []
            for line in lines:
                words = line.split('\t')
                name = words.pop(0)
                self.workOutList.append([name, {self.calorieRanges[calorieIndex]: float(words[calorieIndex]) for calorieIndex in range(self.countCalories)}])

            self.countWorkouts = len(self.workOutList)
                                    
            # self.workOutList.append([words[0], {self.calorieRanges[calorieIndex]: int(words[calorieIndex]) for calorieIndex in range(self.countCalories)}])
            # self.workOutList = [[words[0], {self.calorrieRanges[calorieIndex]: int(words[calorieIndex])
            #  for calorieIndex in range(self.countCalories)}] for words in line.split('\t') for line in lines]
            return

        
        
        # temporary variables for calorie consumption
        caloriesWalk = [3.4, 4.4, 5.4, 6.3, 7.2]
        caloriesRun = [11.4, 12.4, 14.4, 16.5, 19.6]
        caloriesBike = [4.4, 5.4, 6.1, 6.9, 7.6]
        defaultCalories = [caloriesWalk, caloriesRun, caloriesBike]
        
        # member constants for calorie ranges
        self.BELOW = "below"
        self.ABOVE = "above"

        # member variables
        self.RANGE = 10 # calorie range
        self.calorieRanges = [self.BELOW, "55", "65", "75", self.ABOVE]
        self.coefficient = [0.7, 0.8, 0.9, 1, 1.1]
        self.countWorkouts = 3
        self.countCalories = 5
        self.limit = 10 # maximal number of workouts that can be in workOutList
        self.workOutList = [[self.DEFAULT_WORKOUTS[workOutIndex], {self.calorieRanges[calorieIndex]: defaultCalories[workOutIndex][calorieIndex] for calorieIndex in range(self.countCalories)}] for workOutIndex in range(self.countWorkouts)]        
        # example of workOutList
        # [[name1, {below: consumption1, 55: consumption2, 65: consumption3, 75: consumption3, above: consumption3}],
        # [name2, {below: consumption1, 55: consumption2, 65: consumption3, 75: consumption3, above: consumption3}], ...]
        
        self.rewrite()

    def view(self):
        print("<View and Modify list of exercise>")
        self.viewWorkOutList()
        print()
        
        OPTION1 = "1. View Exercise"
        OPTION2 = "2. Add Exercise"
        OPTION3 = "3. Back"
        options = [OPTION1, OPTION2, OPTION3]
        countOptions = len(options)

        for option in options:
            print(option)
        
        SELECT_MENU = "select menu: "
        while True:
            sel = input(SELECT_MENU)
            p = re.search(r"^(1|2|3)$", sel)
            if not p:
                print("Invalid input. please try agian.")
                continue
            break
        return sel

    def viewWorkOutList(self):
        for index, workOut in enumerate(self.workOutList):
            index_on_display = index + 1
            workOutName = workOut[0]
            print(f"{index_on_display}. {workOutName}")


    #######
    # how to deal with this: 000003?
    #######

    def getWorkOutSelection(self, selStr = "Input number of exercise to view"):
        index = 0
        while (True):
            string = input(selStr)
            length = str(len(string))
            p = re.search(r"^[0-9]{1," + str(length) + r"}$", string)
            if not p:
                print("Contains invalid characters!")
                continue
            index = int(string) - 1
            if not (0 <= index < self.countWorkouts):
                print("The number does not exist in the list!")
                continue
            break
        return index


    def viewWorkOut(self, index):
        
        selectedWorkOut = self.workOutList[index]
        workOutName = selectedWorkOut[0]
        print(f"Name of Exercise: {workOutName}")
        print()

        workOutCalories = selectedWorkOut[1]
        print("Calorie consumption by section: ")
        for calorieRange in self.calorieRanges:
            calorie = workOutCalories[calorieRange]
            if calorieRange == self.BELOW:
                print(f"~{calorieRange}: {calorie}kcal")
            elif calorieRange == self.ABOVE:
                print(f"{calorieRange}~: {calorie}kcal")
            else:
                print(f"{calorieRange}~{int(calorieRange) + self.RANGE}: {calorie}kcal")

        workOutName = self.workOutList[index][0]

        # DEFAULT_WORKOUTS can't be edited
        if workOutName in self.DEFAULT_WORKOUTS:
            OPTION = "1. back"
            print(OPTION)
            SELECT_MENU = "select menu: "
            sel = input(SELECT_MENU)

            while sel != '1':
                print("Invalid input. please try again.")
                sel = input(SELECT_MENU)
            return ['3', '']
    
        OPTION1 = "1. edit"
        OPTION2 = "2. delete"
        OPTION3 = "3. back"
        options = [OPTION1, OPTION2, OPTION3]
        countOptions = len(options)

        for option in options:
            print(option)

        SELECT_MENU = "select menu"
        sel = input("select menu: ")

        while len(sel) >= 2 or not ('1' <= sel <= str(countOptions)):
            print("Invalid input. please try again.")
            sel = input(SELECT_MENU)
        return [sel, index]

    def addWorkOut(self):
        if self.countWorkouts >= 10:
            print("Max count of exercise limit is 10!\n You cannot over it!")
            input()
            return

        name = ""
        names = [workOut[0] for workOut in self.workOutList]
        while True:
            name = input("Input name of exercise: ")
            p = re.search(r'^[\w ]{1,20}$', name)
            if len(name) > 20:
                print("Length of name must be 1 to 20.")
                input()
            elif not p:
                print("Wrong input! Please Enter Again!")
                input()
            elif name in names:
                print("try with a different name. You already have a workout that has the same name.")
                input()
            else:
                break
        consumption = ""
        while True:
            consumption = input("(65~75kg standard) Input calorie consumption per minute: ")
            p = re.search(r'^([1-9]|[1-9][0-9]|[1-4][0-9][0-9]|500)$', consumption)
            if not p:
                print("Please enter digit between 1~500!")
                input()
                continue
            break
        
        self.workOutList.append([name, {self.calorieRanges[indexCalories]: math.floor(self.coefficient[indexCalories] * int(consumption) * 100) / 100.0 for indexCalories in range(self.countCalories)}])
        self.countWorkouts += 1
        self.rewrite()
        print("Exercise added.")
        input()
        
        

    def editWorkOut(self, index):
        workOutName = self.workOutList[index][0]
        if workOutName in self.DEFAULT_WORKOUTS:
            print("this workout can't be deleted.")
            input()
            return
        
        while True:
            OPTION1 = "1. workout name"
            OPTION2 = "2. calorie consumption"
            options = [OPTION1, OPTION2]
            for option in options:
                print(option)
            sel = input("please select an item to modify: ")
            p = re.search(r'^[1|2]$', sel)
            if not p:
                print("invalid input. please try again.")
                continue
            break


        
        if sel == '1':
            names = [workOut[0] for workOut in self.workOutList]
            name = ""
            while True:
                name = input("Input name of exercise: ")
                p = re.search(r'^[\w ]{1,20}$', name)
                if len(name) > 20:
                    print("Length of name must be 1 to 20.")
                    input()
                elif not p:
                    print("Wrong input! Please Enter Again!")
                    input()
                elif name == workOutName:
                    print("try with a different name. the previous name is the same as you typed.")
                    input()
                elif name in names:
                    print("try with a different name. You already have a workout that has the same name.")
                    input()
                else:
                    break
            self.workOutList[index][0] = name
        elif sel == '2':
            consumption = ""
            while True:
                consumption = input("(65~75kg standard) Input calorie consumption per minute: ")
                p = re.search(r'^([1-9]|[1-9][0-9]|[1-4][0-9][0-9]|500)$', consumption)
                if not p:
                    print("Please enter digit between 1~500!")
                    input()
            for indexCalories in range (self.countCalories):
                self.workOutList[index][1][indexCalories] = math.floor(self.coefficient[indexCalories] * int(consumption) * 100) / 100.0
                
        self.rewrite()
        print("Successfully modified.")
        input()

    def deleteWorkOut(self, index):
        workOutName = self.workOutList[index][0]
        self.workOutList.pop(index)
        self.countWorkouts -= 1
        self.rewrite()
        print("finished deleting.")
        input()
        
    def rewrite(self):
        if os.path.isfile(self.filePath):
            os.remove(self.filePath)
        f = open(self.filePath, "w")
        for workOutName, calorieConsumption in self.workOutList:
            consumptions = [str(value) for value in calorieConsumption.values()]
            f.write('\t'.join([workOutName] + consumptions) + '\n')


    
            



        


        




