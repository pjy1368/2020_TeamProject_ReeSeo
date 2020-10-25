from os import path
class WorkOut:
    def __init__(self):
        # check if file exists
        # filePath = path.join("./user", "goal.txt")
        # f = open(filePath, "r")
        # s = f.readlines()
        # self.term = s[0].split('\n')[0]
        # self.calories = s[1].split('\n')[0]
        # f.close()


        # temporary variables for workout names
        TAKING_A_WALK = "taking a walk"
        GOING_FOR_A_RUN = "going for a run"
        RIDING_A_BIKE = "riding a bike"
        defaultWorkOuts = [TAKING_A_WALK, GOING_FOR_A_RUN, RIDING_A_BIKE]

        
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
        self.countWorkouts = 3
        self.countCalories = 5
        self.workOutList = [[defaultWorkOuts[workOutIndex], {self.calorieRanges[calorieIndex]: defaultCalories[workOutIndex][calorieIndex] for calorieIndex in range(self.countCalories)}] for workOutIndex in range(self.countWorkouts)]
        self.limit = 10 # maximal number of workouts that can be in workOutList
        
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

    def viewExercise(self, index):
        
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

    def editWorkOut(self):
        OPTION1 = "1. workout name"
        OPTION2 = "2. calorie consumption"
        options = [OPTION1, OPTION2]
        for option in options:
            print(option)
        
        sel = input("please select an item to modify")


        # while len(sel) >= 2 or 
        # "invalid input. pla"

        


        

            



        


        



    


    # edit workout list
    # def edit():

    # delete workout list
    # def delete():


