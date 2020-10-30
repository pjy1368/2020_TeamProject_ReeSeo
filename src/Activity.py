import os
import re
from datetime import datetime

# DEAL WITH MARK 'ADD'
# 'FOR TEST PURPOSE': Print out results for test purpose
# WHAT HASN'T BEEN TESTED(DATE NEEDED)
# 1. WHEN YOU GO TO TOMORROW AND WRITE DOWN DAILY ACTIVITIES
# 2. THE STRUCTURE OF dailyHistory changes with multiple dates
# 3. analyze: couldn't proceed because there're issues dealing with date class

class Activity:
    # Each Daily Activity saved like this example:
    # YYYY-MM-DD\t(CALORIE_GOAL)\t(CALORIE_CONSUMPTION)\t(START TIME) ~ (FINISH TIME):WORKOUT\n

    def __init__(self):
        self.FILE_PATH = "./user/history.txt"
        self.dailyHistory = []
        self.TIME_INDEX = 3
        self.START_TIME = "startDate"
        self.FINISH_TIME = "finishDate"
        self.NAME = "name"
        self.goalCalories = 0
        self.consumptionCalories = 0
        self.consumptionHistory = []
        # dailyHistory has data structured like this for exmaple:
        # [[date, [{startDate: finishDate:, name:}, {startDate: finishDate:, name: }]]
        # value parts of date,  startDate, finishDate would be built-in date class
        # value parts of goal, consumption would be a floating number upto 2 decimal point.


    def submit(self):
        sel = ""
        while True:
            print("<Submit Today's Exercise Records>")
            print("1. submit exercise record")
            print("2. change to the next day")
            print("3. back")
            sel = input("select menu: ")
            # only match either 1,2 or 3
            p = re.search(r"^(1|2|3)$", sel)
            if not p:
                input("Please re-enter!")
                continue
            break
        return sel
        

    def submitWorkOutRecord(self, account):
        # obtain variables from account object
        weight = account.weight
        workOut = account.workOut
        goal = account.goal

        self.goalCalories = goal.calories

        # ADD need to change account.currentDate to string
        date = account.currentDate

        # select a workout
        SEL_STR = "Please select an exercise"
        workOut.viewWorkOutList()
        index = workOut.getWorkOutSelection(SEL_STR)

        # enter date info
        FORMAT_ERR_MSG = "Please enter the correct format of the time!"
        LOGICAL_ERR_MSG = "Finished time is earlier than start time!"

        start_time = input("Enter exercise started time: ")
        # ADD: check if date input is valid!
        if False:
            print(FORMAT_ERR_MSG)

        finish_time = input("Enter exercise finished time: ")
        # ADD: check if date input is valid!
        if False:
            print(FORMAT_ERR_MSG)
            print(LOGICAL_ERR_MSG)

        workOutList = workOut.workOutList
        workOutInfo = workOutList[int(index)]


        workOutName = workOutInfo[0]

        # [{date, [{startDate: finishDate:, name:}, {startDate: finishDate:, name:}, ]
        if not self.dailyHistory:
            self.dailyHistory = [[date, 
            [{self.START_TIME: start_time, self.FINISH_TIME: finish_time, self.NAME: workOutName}]]]
        else:
            # ADD: we should decide the goal should be appended to the end of dailyHistory or not by chekcking dates
            if self.dailyHistory[len(self.dailyHistory) - 1][0] == date:
                # when the date exists
                self.dailyHistory[len(self.dailyHistory) - 1][1].append({self.START_TIME: start_time, self.FINISH_TIME: finish_time, self.NAME: workOutName})

            # when the date is new and we should append it
            # self.dailyHistory.append(date, [{self.START_TIME: start_time, self.FINISH_TIME: finish_time, self.NAME: workOutName}])
            else:
                self.dailyHistory.append(date, [{self.START_TIME: start_time, self.FINISH_TIME: finish_time, self.NAME: workOutName}])
        # find consumption 
        caloriesPerMin = self.findCaloriesPerMin(workOut, index, weight)

        # ADD: find out the gap between finish time and start time - fix 30
        startTimeList = self.START_TIME.split("-")
        finishTimeList = self.FINISH_TIME.split("-")

        start = datetime(int(startTimeList[0]), int(startTimeList[1]), int(startTimeList[2]), int(startTimeList[3]), int(startTimeList[4]))
        finish = datetime(int(finishTimeList[0]), int(finishTimeList[1]), int(finishTimeList[2]), int(finishTimeList[3]), int(finishTimeList[4]))
        gap = int((finish - start).minute)
        
        self.consumptionCalories += caloriesPerMin * gap
        
        print("Exercise record submitted successfully.")


    def findCaloriesPerMin(self, workOut, index, weight):
        caloriesPerMin = 0
        for calorieIndex, calorieRange in enumerate(workOut.calorieRanges):
            if calorieIndex == 0:
                if float(weight) < float(workOut.calorieRanges[1]):
                    print("test case 1")
                    caloriesPerMin = float(workOut.workOutList[index][1]["below"])
                    print(workOut.workOutList)
                    break
            elif calorieIndex == len(workOut.calorieRanges) - 1:
                print("test case 2")
                caloriesPerMin = float(workOut.workOutList[index][1]["above"])
                print(workOut.workOutList)
                break
            elif float(weight) >= int(calorieRange):
                print("test case 3")
                caloriesPerMin = float(workOut.workOutList[index][1][calorieRange])
                print(workOut.workOutList[index][1][calorieRange])
                print(workOut.workOutList)
                break
        # test purpose
        print(caloriesPerMin)
        return caloriesPerMin


    def tomorrow(self, account):
        # Add:account.currentDay should point to next day
        self.consumptionHistory.append(self.consumptionCalories)
        self.rewriteFile()
        self.goalCalories = 0
        self.consumptionCalories = 0

        currentDateList = account.currentDate.split("-")
        pre = datetime(int(currentDateList[0]), int(currentDateList[1]), int(currentDateList[2]))
        now = pre + pre.datetime.timedelta(days=1)

        account.currentDate = now.strftime('%Y-%m-%s')

    def analyze(self):
        print("Enter time period")
        print("(The entry period should not include the current date or the date after the current date, or the period of the date entry should not exceed 14 days.")
        print("ex)2020-10-01")
        print("ex)2020-10-01 ~ 2020-10-05")




	
    def rewriteFile(self):
        if os.path.isfile(self.FILE_PATH):
            os.remove(self.FILE_PATH)
        f = open(self.FILE_PATH, "w")
        # [[date , goal , consumption, [{startDate: finishDate:, name:}, {startDate: finishDate:, name: }]]
        # ADD: sort workout dateInfo
        for index, [date, timeInfos] in enumerate(self.dailyHistory):
            string = f"{date}\t{self.goalCalories}\t{self.consumptionHistory[index]}\t"
            for index2, timeInfo in enumerate(timeInfos):
                if index2 == len(timeInfos) - 1:
                    string += f"{timeInfo[self.START_TIME]}~{timeInfo[self.FINISH_TIME]}:{timeInfo[self.NAME]}"
                    continue
                string += f"{timeInfo[self.START_TIME]}~{timeInfo[self.FINISH_TIME]}:{timeInfo[self.NAME]}\t"
            string += "\n"
        f.write(string)

    #ADD: when you reach the last day of goal, you should indicate to user that it's finished.
    # goalCalories <= 0
    # dailyHistory <= []

    

