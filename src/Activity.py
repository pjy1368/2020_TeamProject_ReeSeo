import os
import re
import datetime

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
        self.TIME_INDEX = 3
        self.START_TIME = "startDate"
        self.FINISH_TIME = "finishDate"
        self.NAME = "name"
        self.goalCalories = 0
        self.consumptionCalories = 0

        self.dailyHistory = []
        self.consumptionHistory = []
        self.loadHistory()
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
            print(self.dailyHistory)
            print(self.consumptionHistory)
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

        date = account.currentDate

        # select a workout
        SEL_STR = "Please select an exercise"
        workOut.viewWorkOutList()
        index = workOut.getWorkOutSelection(SEL_STR)

        # enter date info
        FORMAT_ERR_MSG = "Please enter the correct format of the time!"
        LOGICAL_ERR_MSG = "Finished time is earlier than start time!"

        startTime = input("Enter exercise started time: ")
        # ADD: check if date input is valid!
        if False:
            print(FORMAT_ERR_MSG)

        finishTime = input("Enter exercise finished time: ")
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
            [{self.START_TIME: startTime, self.FINISH_TIME: finishTime, self.NAME: workOutName}]]]
        else:
            # chekcking dates to decide where new data should be appended:
            if self.dailyHistory[len(self.dailyHistory) - 1][0] == date:
                # when the date exists in dailyHistory
                self.dailyHistory[len(self.dailyHistory) - 1][1].append({self.START_TIME: startTime, self.FINISH_TIME: finishTime, self.NAME: workOutName})

            # when the date can't be found in dailyHistory
            else:
                self.dailyHistory.append([date, [{self.START_TIME: startTime, self.FINISH_TIME: finishTime, self.NAME: workOutName}]])

        # compute consumption 
        caloriesPerMin = self.findCaloriesPerMin(workOut, index, weight)

        # find out the gap between finish time and start time
        startTimeList = startTime.split("-")
        finishTimeList = finishTime.split("-")

        start = datetime.datetime(int(startTimeList[0]), int(startTimeList[1]), int(startTimeList[2]), int(startTimeList[3]), int(startTimeList[4]))
        finish = datetime.datetime(int(finishTimeList[0]), int(finishTimeList[1]), int(finishTimeList[2]), int(finishTimeList[3]), int(finishTimeList[4]))
        gapList = str((finish - start)).split(":")
        gap = int(gapList[0]) * 60 + int(gapList[1])
        
        self.consumptionCalories += caloriesPerMin * gap
        
        print("Exercise record submitted successfully.")


    def findCaloriesPerMin(self, workOut, index, weight):
        caloriesPerMin = 0
        for calorieIndex, calorieRange in enumerate(workOut.calorieRanges):
            if calorieIndex == 0:
                if float(weight) < float(workOut.calorieRanges[1]):
                    caloriesPerMin = float(workOut.workOutList[index][1]["below"])
                    break
            elif calorieIndex == len(workOut.calorieRanges) - 1:
                caloriesPerMin = float(workOut.workOutList[index][1]["above"])
                break
            elif float(weight) >= int(calorieRange):
                caloriesPerMin = float(workOut.workOutList[index][1][calorieRange])
                break
        return caloriesPerMin


    def tomorrow(self, account):
        self.consumptionHistory.append(self.consumptionCalories)
        self.rewriteFile()
        self.goalCalories = 0
        self.consumptionCalories = 0

        currentDateList = account.currentDate.split("-")
        pre = datetime.datetime(int(currentDateList[0]), int(currentDateList[1]), int(currentDateList[2]))
        now = pre + datetime.timedelta(days=1)
        account.currentDate = now.strftime('%Y-%m-%d')
        account.revise([account.name, account.gender, account.birth, account.currentDate, account.height, account.weight], False)

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
        string = ""
        for index, [date, timeInfos] in enumerate(self.dailyHistory):
            string = f"{date}\t{self.goalCalories}\t{self.consumptionHistory[index]}\t"
            list = []
            for timeInfo in timeInfos:
                timeInfoList = []
                timeInfoList.append(timeInfo[self.START_TIME])
                timeInfoList.append("~")
                timeInfoList.append(timeInfo[self.FINISH_TIME])
                timeInfoList.append(":")
                timeInfoList.append(timeInfo[self.NAME])
                list.append(timeInfoList)

            sorted_list = sorted(list, key=lambda t: datetime.datetime.strptime(t[0], '%Y-%m-%d-%H-%M'))

            for index2, temp in enumerate(sorted_list):
                if index2 == len(sorted_list) - 1:
                    for i in temp:
                        string += i
                else:
                    for i in temp:
                        string += i
                    string += "\t"
            string += "\n"
            
        f.write(string)
        f.close()


    def loadHistory(self):
        if os.path.isfile(self.FILE_PATH):
            f = open(self.FILE_PATH, "r")
            lines = f.readlines()
            for line in lines:
                totalStr = line.strip().split("\t")
                date, calorieGoal, calorieConsumption, timeStrList = totalStr[0], totalStr[1], totalStr[2], totalStr[3:]
                timeInfo = []
                for timeStr in timeStrList:
                    timeRange, name = timeStr.split(":")
                    startTime, finishTime = timeRange.split("~")
                    timeInfo.append({self.START_TIME: startTime, self.FINISH_TIME: finishTime, self.NAME: name})
                self.dailyHistory.append([date, timeInfo])
                self.consumptionHistory.append(float(calorieConsumption))

        