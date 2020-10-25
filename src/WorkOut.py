import os
import re

class WorkOut:
    def __init__(self):
        # check if file exists
        self.filePath =  os.path("./user/workout.txt")
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
            self.countWorkouts = 3
            self.countCalories = 5
            self.limit = 10  # maximal number of workouts that can be in workOutList            
            self.workOutList = [[words[0], {self.calorrieRanges[calorieIndex]: int(words[calorieIndex]) for calorieIndex in range(self.countCalories)}] for words in line.split('\t') for line in lines]
            return

        # temporary variables for workout names
        TAKING_A_WALK = "taking a walk"
        GOING_FOR_A_RUN = "going for a run"
        RIDING_A_BIKE = "riding a bike"
        self.DEFAULT_WORKOUTS = [TAKING_A_WALK, GOING_FOR_A_RUN, RIDING_A_BIKE]

        
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
        
    def view(self):
        print("<View and Modify list of exercise>")
        for index, workOut in enumerate(self.workOutList):
            index_on_display = index + 1
            workOutName = workOut[0]
            print(f"{index_on_display}. {workOutName}")

        OPTION1 = "1. View Exercise"
        OPTION2 = "2. Add Exercise"
        OPTION3 = "3. Back"
        options = [OPTION1, OPTION2, OPTION3]
        countOptions = len(options)

        for option in options:
            print(option)


        SELECT_MENU = "select menu: "
        sel = input(SELECT_MENU)
        
        while len(sel) >= 2 or sel[0] <= '1' or sel[0] >= str(countOptions):
            print("Invalid input. please try agian.")
            sel = input(SELECT_MENU)
        return sel


    #######
    # how to deal with this: 000003?
    #######
    def viewExercise(self):
        index = 0
        while (True):
            string = input("Input number of exercise to view:")
            length = str(len(string))
            p = re.search(rf"^[0-9]{1,{length}}$", string)
            if not p:
                print("Contains invalid characters!")
                continue
            index = int(string) - 1
            if 0 <= index < self.countWorkouts:
                print("The number does not exist in the list!")
                continue
            break

        selectedWorkOut = self.workOutList[index]
        workOutName = selectedWorkOut[0]
        print(f"Name of Exercise: {workOutName}")
        print()

        workOutCalories = selectedWorkOut[1]
        print("Calorie consumption by seciton: ")
        for calorieRange in self.calorieRanges:
            calorie = workOutCalories[calorieRange]
            if calorie == self.BELOW:
                print(f"~{calorie}: {workOutCalories[calorie]}kcal")
            elif calorie == self.ABOVE:
                print(f"{calorie}~: {workOutCalories[calorie]}kcal")
            else:
                print(f"{calorie}~{int(calorie) + self.RANGE}: {workOutCalories[calorie]}kcal")
        
        OPTION1 = "1. edit"
        OPTION2 = "2. delete"
        OPTION3 = "3. back"
        options = [OPTION1, OPTION2, OPTION3]
        countOptions = len(options)

        for option in options:
            print(option)

        SELECT_MENU = "select menu"
        sel = input("select menu: ")

        while len(sel) >= 2 or sel <= '1' or sel >= str(countOptions):
            print("Invalid input. please try agian.")
            sel = input(SELECT_MENU)
        return [sel, index]

    def addWorkOut(self):
        if self.countWorkouts >= 10:
            print("Max count of exercise limit is 10!\n You cannot over it!")
            input()

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
            else:
                break
        consumption = ""
        while True:
            consumption = input("(65~75kg standard) Input calorie consumption per minute: ")
            p = re.search(r'^[1-9]|[1-9][0-9]|[1-5][0-9][0-9]$', consumption)
            if not p:
                print("Please enter digit between 1~500!")
                input()
        
        self.workOutList.append([name, {self.calorieRanges[indexCalories]: self.coefficient[indexCalories] * int(consumption) for indexCalories in self.countCalories}])
        self.rewrite()
        # for test purpose only
        print(self.workOutList)
        print("Exercise added.")
        input()
        
        

    def editWorkOut(self, index):
        while True:
            OPTION1 = "1. workout name"
            OPTION2 = "2. calorie consumption"
            options = [OPTION1, OPTION2]
            for option in options:
                print(option)
            sel = input("please select an item to modify: ")
            p = re.search(r'^1|2$', sel)
            if not p:
                print("invalid input. please try again.")
                continue
            break

        if sel == '1':
            while True:
                name = input("Input name of exercise: ")
                p = re.search(r'^[\w ]{1,20}$', name)
                if len(name) > 20:
                    print("Length of name must be 1 to 20.")
                    input()
                elif not p:
                    print("Wrong input! Please Enter Again!")
                    input()
                else:
                    break
            self.workOutList[[index][0]] = name
        elif sel == '2':
            consumption = ""
            while True:
                consumption = input("(65~75kg standard) Input calorie consumption per minute: ")
                p = re.search(r'^[1-9]|[1-9][0-9]|[1-5][0-9][0-9]$', consumption)
                if not p:
                    print("Please enter digit between 1~500!")
                    input()
            for indexCalories in self.countCalories:
                self.workOutList[index][1][indexCalories] = self.coefficient[indexCalories] * int(consumption)
                
        self.rewrite()
        # for test purpose only
        print(self.workOutList)
        print("Successfully modified.")
        input()

    def deleteWorkOut(self, index):
        workOutName = self.workOutList[index][0]
        if workOutName in self.DEFAULT_WORKOUTS:
            print("this workout can't be deleted.")
            input()
            return
        self.workOutList.pop(index)
        self.rewrite()
        print("finished deleting.")
        input()
        
        


        
    def rewrite(self):
        os.remove(self.filePath)
        f = open(self.filePath, "w")
        for workOutName, calorieConsumption in self.workOutList:
            f.write('\t'.join(workOutName + list(calorieConsumption.values())) + '\n')
        
    


        

            



        


        



    


    # edit workout list
    # def edit():

    # delete workout list
    # def delete():


