import os
import re
import datetime
from math import floor

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
        self.goalHistory = []
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
            sel = input("select menu: ")
            # only match either 1,2 or 3
            p = re.search(r"^(1|2|3)$", sel)
            if not p:
                os.system('cls')        
                input("Please re-enter!")
                os.system('cls')        
                continue
            break
        os.system('cls')
        return sel
    
    def analyze(self, account):
        print("Enter time period")
        print("(The entry period should not include the current date or the date after the current date, or the period of the date entry should not exceed 14 days.")
        print("ex)2020-10-01")
        print("ex)2020-10-01 ~ 2020-10-05")
        print("press q to exit")
        dateStr = input()
        if dateStr == 'q':
            return False

        # check date validation:
        # 1. if any record is included in the date range
        # if not self.isInDailyHitory(dateStr):
        # 2. YYYY-MM-DD ~ YYYY-MM-DD OR YYYY-MM-DD
        # 3. if YYYY-MM-DD => cannont exceed 14 days
        # 4. if it is before currentTime
        # if input is a date

        
        currentDateList = account.currentDate.split("-")
        currentDateTime = datetime.datetime(int(currentDateList[0]), int(currentDateList[1]), int(currentDateList[2]))

        if re.search('^([0-9]{4}-([0-9]){2}-([0-9]){2})$', dateStr):
            if not self.dailyNotTimeValid(dateStr):
                return True

            dateStrList = dateStr.split("-")
            dateStrDateTime = datetime.datetime(int(dateStrList[0]), int(dateStrList[1]), int(dateStrList[2]))

            if dateStrDateTime >= currentDateTime:
                print("You must enter a date prior to the current date.")
                input()
                os.system('cls')
                return True

            date = self.createDatetime(dateStr)
            for index, [date, timeInfos] in enumerate(self.dailyHistory):
                if dateStr == date:
                    consumption = self.consumptionHistory[index]
                    goal = self.goalHistory[index]
                    if goal == 0:
                        achievementRate = 100
                    else:
                        achievementRate = (consumption / goal) * 100
                    achievementRateOutput = "%0.2f" % achievementRate
                    print(f"{date}: {consumption}kcal({achievementRateOutput})%")
            input()
            return True

        elif re.search('^([0-9]{4}-([0-9]){2}-([0-9]){2}) ~ ([0-9]{4}-([0-9]){2}-([0-9]){2})$', dateStr):
            startDateStr, finishDateStr = [dateStr.strip() for dateStr in dateStr.split('~')]

            if not self.dailyNotTimeValid(startDateStr) or not self.dailyNotTimeValid(finishDateStr):
                return True
            
            dateStrStartDateList = startDateStr.split("-")
            dateStrStartDateTime = datetime.datetime(int(dateStrStartDateList[0]), int(dateStrStartDateList[1]), int(dateStrStartDateList[2]))

            if dateStrStartDateTime >= currentDateTime:
                print("You must enter a date prior to the current date.")
                input()
                os.system('cls')
                return True

            dateStrFinishDateList = finishDateStr.split("-")
            dateStrFinishDateTime = datetime.datetime(int(dateStrFinishDateList[0]), int(dateStrFinishDateList[1]), int(dateStrFinishDateList[2]))

            if dateStrFinishDateTime >= currentDateTime:
                print("You must enter a date prior to the current date.")
                input()
                os.system('cls')
                return True

            if dateStrStartDateTime >= dateStrFinishDateTime:
                print("Finish date must not exceed one day from the start date.")
                input()
                os.system('cls')
                return True

            if dateStrFinishDateTime - datetime.timedelta(days=14) > dateStrStartDateTime:
                print("The period must not exceed 14 days.")
                input()
                os.system('cls')
                return True

            startDate, finishDate = [self.createDatetime(startDateStr), self.createDatetime(finishDateStr)]            
            for index, [date, timeInfos] in enumerate(self.dailyHistory):
                if startDate <= self.createDatetime(date) <= finishDate:
                    
                    consumption = self.consumptionHistory[index]
                    goal = self.goalHistory[index]
                    if goal == 0:
                        achievementRate = 100
                    else:
                        achievementRate = (consumption / goal) * 100
                    achievementRateOutput = "%0.2f" % achievementRate
                    print(f"{date}: {consumption}kcal({achievementRateOutput})%")
            input()
            return True
        else:
            print("an error occured.")
            print("Make sure you enter spaces before and after '~'.")
            input()
            os.system('cls')
            return True

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

        list = None
        pre = None

        while True:
            while True:
                startTime = input("Enter exercise started time (YYYY-mm-dd-HH-MM): ")

                if not self.dailyValid(startTime):
                    continue

                list = startTime.split("-")
                pre = datetime.datetime(int(list[0]), int(list[1]), int(list[2]), int(list[3]), int(list[4]))

                if account.currentDate != (list[0] + "-" + list[1] + "-" + list[2]):
                    print("Start date and current date must be the same.")
                    input()
                    os.system('cls')
                    continue
                break
            
            while True:
                finishTime = input("Enter exercise finished time (YYYY-mm-dd-HH-MM): ")

                if not self.dailyValid(finishTime, pre):
                    continue
                
                list = finishTime.split("-")
                now = datetime.datetime(int(list[0]), int(list[1]), int(list[2]), int(list[3]), int(list[4]))
                if now > pre + datetime.timedelta(days=1):
                    print("Finish date must not exceed one day from the start date.")
                    input()
                    os.system('cls')
                    continue
                break
            
            if not self.isTimeRangeValid(startTime, finishTime):
                print("Existing exercise time overlaps!")
                input()
                return
            break
                      

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
        os.system('cls')

    def dailyValid(self, date, pre = None): 
        if len(date) != 16:
            print("Length of string must be 16.")
            input()
            os.system('cls')
            return False
        
        if date[4] != '-' or date[7] != '-' or date[10] != '-' or date[13] != '-':
            print("Each year, month and date are must classified as '-' with followed form (YYYY-MM-DD-HH-mm)")
            input()
            os.system('cls')
            return False
        
        list = date.split('-')

        if len(list[0]) != 4 or len(list[1]) != 2 or len(list[2]) != 2 or len(list[3]) != 2 or len(list[4]) != 2:
            print("Each year, month and date are must classified as '-' with followed form (YYYY-MM-DD-HH-mm)")
            input()
            os.system('cls')
            return False
        
        check = True
        for i in list:
            p = re.search(r'^[0-9]{1,4}$', i)

            if not p:
                check = False
                print("Character that is not a digit or '-' are illegal.")
                input()
                os.system('cls')
                break

        if not check:
            return False

        dailyNotTime = list[0] + "-" + list[1] + "-" + list[2]
        p = re.search(r'^((19[7-9][0-9]|20[0-2][0-9]|203[0-6])-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])|(2037-(0[1-9]|1[0-1])-(0[1-9]|[12][0-9]|3[01])))$', dailyNotTime)

        if not p:
            print("Iligeal form of date. (1970-01-01 ~ 2037-11-30)")
            input()
            os.system('cls')
            return False
        
        check = True
        while check:
            try:
                now = datetime.datetime(int(list[0]), int(list[1]), int(list[2]))
                break
            except ValueError:
                print("Inexistent form of date followed by Gregorian Calendar")
                input()
                os.system('cls')
                check = False
        
        if not check:
            return False

        time = list[3] + "-" + list[4]

        p = re.search("^(([0-1][0-9])|2[0-3])-([0-5][0-9])$", time)

        if not p:
            print("Iligeal form of time. (00-00 ~ 23-59)")
            input()
            os.system('cls')
            return False

        now = datetime.datetime(int(list[0]), int(list[1]), int(list[2]), int(list[3]), int(list[4]))
        if pre != None and pre > now:
            print("Finish date is earlier than start date.")
            input()
            os.system('cls')
            return False

        os.system('cls')
        return True
    
    def dailyNotTimeValid(self, date):
        if len(date) != 10:
            print("Length of string must be 10.")
            input()
            os.system('cls')
            return False
        
        if date[4] != '-' or date[7] != '-':
            print("Each year, month and date are must classified as '-' with followed form (YYYY-MM-DD)")
            input()
            os.system('cls')
            return False
        
        list = date.split('-')

        if len(list[0]) != 4 or len(list[1]) != 2 or len(list[2]) != 2:
            print("Each year, month and date are must classified as '-' with followed form (YYYY-MM-DD)")
            input()
            os.system('cls')
            return False
        
        check = True
        for i in list:
            p = re.search(r'^[0-9]{1,4}$', i)

            if not p:
                check = False
                print("Character that is not a digit or '-' are illegal.")
                input()
                os.system('cls')
                break

        if(not check):
            return False

        p = re.search(r'^((19[7-9][0-9]|20[0-2][0-9]|203[0-6])-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])|(2037-(0[1-9]|1[0-1])-(0[1-9]|[12][0-9]|3[01])))$', date)

        if not p:
            print("Iligeal form of date. (1970-01-01 ~ 2037-11-30)")
            input()
            os.system('cls')
            return False
        
        check = True
        while check:
            try:
                now = datetime.datetime(int(list[0]), int(list[1]), int(list[2]))
                break
            except ValueError:
                print("Inexistent form of date followed by Gregorian Calendar")
                input()
                os.system('cls')
                check = False
        
        if not check:
            return False
        return True


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
        self.goalHistory.append(self.goalCalories)
        self.rewriteFile()
        self.goalCalories = 0
        self.consumptionCalories = 0

        currentDateList = account.currentDate.split("-")
        pre = datetime.datetime(int(currentDateList[0]), int(currentDateList[1]), int(currentDateList[2]))
        now = pre + datetime.timedelta(days=1)
        account.currentDate = now.strftime('%Y-%m-%d')
        account.revise([account.name, account.gender, account.birth, account.currentDate, account.height, account.weight], False)
        account.goal.isEnd(account)


	
    def rewriteFile(self):
        if os.path.isfile(self.FILE_PATH):
            os.remove(self.FILE_PATH)
        f = open(self.FILE_PATH, "w")
        # [[date , goal , consumption, [{startDate: finishDate:, name:}, {startDate: finishDate:, name: }]]
        string = ""
        for index, [date, timeInfos] in enumerate(self.dailyHistory):
            string += f"{date}\t{self.goalCalories}\t{self.consumptionHistory[index]}\t"
            timeInfos.sort(key= lambda item: self.createDatetime(item[self.START_TIME]))
            for index2, timeInfo in enumerate(timeInfos):
                if index2 == len(timeInfos) - 1:
                    string += f"{timeInfo[self.START_TIME]}~{timeInfo[self.FINISH_TIME]}:{timeInfo[self.NAME]}"
                    continue
                string += f"{timeInfo[self.START_TIME]}~{timeInfo[self.FINISH_TIME]}:{timeInfo[self.NAME]}\t"
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
                self.goalHistory.append(float(calorieGoal))

    def createDatetime(self, string):
        strList = string.split('-')
        if len(strList) == 3:
            year, month, day = [int(strSplitted) for strSplitted in strList]
            return datetime.datetime(year, month , day)
        elif len(strList) == 5:
            year, month, day, hour, minute = [int(strSplitted) for strSplitted in strList]
            return datetime.datetime(year, month, day, hour, minute)
        else:
            print("An Error occured in createDatetime")
    
    def isInDailyHitory(self, dateStr):
        for date in self.dailyHistory:
            if date == dateStr:
                return True
        return False
        
    def isIntervalLappedOver(self, interval1, interval2):
        a, b = interval1
        c, d = interval2
        if  c <= a <= d:
            return True
        elif c <= b <= d:
            return True
        elif a <= c <= d <= b:
            return True
        return False
    
    # check if given time is overlapped when given date are the same
    def isTimeInfoLappedOver(self, dateWritten, dateToBeChecked, timeInfos, timeToBeChecked):
        if dateWritten == dateToBeChecked or (dateWritten + datetime.timedelta(days=1) == dateToBeChecked):
            for timeInfo in timeInfos:
                timeWritten = [self.createDatetime(timeInfo[self.START_TIME]), self.createDatetime(timeInfo[self.FINISH_TIME])]
                if self.isIntervalLappedOver(timeToBeChecked, timeWritten):
                    return True
        return False
    
    # check if given time range is valid
    def isTimeRangeValid(self, startTime, finishTime):
        for dateStr, timeInfos in self.dailyHistory:
            dateWritten = self.createDatetime(dateStr)
            dateSlicedFromStart = '-'.join(startTime.split('-')[0:3])
            dateToBeChecked = self.createDatetime(dateSlicedFromStart)
            dateInputs = [self.createDatetime(startTime), self.createDatetime(finishTime)]
            if self.isTimeInfoLappedOver(dateWritten, dateToBeChecked, timeInfos, dateInputs):
                return False
        return True

        
    