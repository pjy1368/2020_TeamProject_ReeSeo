import os
import shutil
import re
from Goal import Goal
from WorkOut import WorkOut
from datetime import datetime

class Account:
    # If you have an account, define the member variables based on the contents of the text file.
    # If no account exists, define the member variable as 'None'.
    def __init__(self):
        if self.isMember():
            filePath = "./user/profile.txt"
            f = open(filePath, "r")
            s = f.readlines()
        
            self.name = s[0].split('\n')[0]
            self.gender = s[1].split('\n')[0]
            self.birth = s[2].split('\n')[0]
            self.startingDate = s[3].split('\n')[0]
            self.height = s[4].split('\n')[0]
            self.weight = s[5].split('\n')[0]
            self.goal = Goal(self)
            self.workOut = WorkOut()

            f.close()
        else:
            self.name = None
            self.gender = None
            self.birth = None
            self.startingDate = None
            self.height = None
            self.weight = None

    # Does the account exist?
    def isMember(self):
        return os.path.isdir("./user")

    # Create account.
    def create(self, arr):
        isNew = not self.isMember() # Is it a new account?

        # pre : The user's birth date is expressed as a "datetime" object.
        # now : The user's starting date is expressed as a "datetime" object.

        # If no account exists, Create a folder and a "profile.txt" file.
        # Also, 'pre', 'now' are defined as 'None'
        if isNew:
            os.mkdir("./user")

            filePath = "./user/profile.txt"
            f = open(filePath, "w")

            pre = None
            now = None
        else:
            list = self.birth.split("-")
            pre = datetime(int(list[0]), int(list[1]), int(list[2]))

            list = self.startingDate.split("-")
            now = datetime(int(list[0]), int(list[1]), int(list[2])) 

        # If you have a new account, arr must be [1, 2, 3, 4, 5, 6].
        # In other words, all personal information of the user are entered.

        # If If you have an account, arr is [1], or [1, 2] , ... , [1, 2, 3, 4, 5, 6].
        # In other words, the user's personal information is partially or all entered.
        for i in arr:
            i = int(i)

            if i == 1:
                while True:
                    print("Enter name (20 Digits with Upper- and Lower-case alphabet and blank spaces)")
                    name = input("-> ")

                    if len(name) < 1 or len(name) > 20:
                        print("Length of name must be 1 to 20.")
                        input()
                        os.system('cls')
                        continue
                    
                    p = re.search(r'^[a-zA-Z ]{1,20}$', name)

                    if not p:
                        print("Only Upper- and Lower-case alphabet and blank spaces are allowed.")
                        input()
                        os.system('cls')
                        continue
                    
                    if not isNew and self.name == name:
                        print("You have entered the same value as before.")
                        input()
                        os.system('cls')
                        continue

                    os.system('cls')

                    if not isNew:
                        print("Your name has been modified.")
                        input()

                    self.name = name
                    os.system('cls')
                    break
            elif i == 2:
                while True:
                    gender = input("Enter gender (1. Female 2. Male) : ")

                    if len(gender) != 1:
                        print("Length of gender must be 1.")
                        input()
                        os.system('cls')
                        continue
                    
                    if gender < '1' or gender > '2':
                        print("Only one Digit: 1 or 2 are legal.")
                        input()
                        os.system('cls')
                        continue
                    
                    if gender == '1':
                        self.gender = "Female"
                    else:
                        self.gender = "Male"

                    os.system('cls')
                    if not isNew and self.gender == gender:
                        print("You have entered the same value as before.")
                        input()
                        os.system('cls')
                        continue

                    if not isNew:
                        print("Your gender has been modified.")
                        input()

                    os.system('cls')
                    break
            elif i == 3:
                 while True:
                    birth = input("Enter the date of birth (YYYY-MM-DD) : ")
                    
                    if len(birth) != 10:
                        print("Length of string must be 10.")
                        input()
                        os.system('cls')
                        continue
                    
                    if birth[4] != '-' or birth[7] != '-':
                        print("Each year, month and date are must classified as '-' with followed form (YYYY-MM-DD)")
                        input()
                        os.system('cls')
                        continue
                    
                    list = birth.split('-')

                    if len(list[0]) != 4 or len(list[1]) != 2 or len(list[2]) != 2:
                        print("Each year, month and date are must classified as '-' with followed form (YYYY-MM-DD)")
                        input()
                        os.system('cls')
                        continue
                    
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
                        continue

                    p = re.search(r'^(19[7-9][0-9]|20[0-1][0-9])-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$', birth)

                    if not p:
                        print("Iligeal form of date (1970-01-01 ~ 2019-12-31)")
                        input()
                        os.system('cls')
                        continue
                    
                    check = True
                    while check:
                        try:
                            pre = datetime(int(list[0]), int(list[1]), int(list[2]))
                            break
                        except ValueError:
                            print("Inexistent form of date followed by Gregorian Calendar")
                            input()
                            os.system('cls')
                            check = False
                    
                    if not check:
                        continue

                    if not isNew and pre > now:
                        print("Birth is later than date of starting date.")
                        input()
                        os.system('cls')
                        continue

                    os.system('cls')
                    if not isNew and self.birth == birth:
                        print("You have entered the same value as before.")
                        input()
                        os.system('cls')
                        continue

                    if not isNew:
                        print("Your birth has been modified.")
                        input()

                    self.birth = birth
                    os.system('cls')
                    break
            elif i == 4:
                 while True:
                    startingDate = input("Enter starting date (YYYY-MM-DD) : ")
                    
                    if len(startingDate) != 10:
                        print("Length of string must be 10.")
                        input()
                        os.system('cls')
                        continue
                    
                    if startingDate[4] != '-' or startingDate[7] != '-':
                        print("Each year, month and date are must classified as '-' with followed form (YYYY-MM-DD)")
                        input()
                        os.system('cls')
                        continue
                    
                    list = startingDate.split('-')

                    if len(list[0]) != 4 or len(list[1]) != 2 or len(list[2]) != 2:
                        print("Each year, month and date are must classified as '-' with followed form (YYYY-MM-DD)")
                        input()
                        os.system('cls')
                        continue
                    
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
                        continue


                    p = re.search(r'^((19[7-9][0-9]|20[0-2][0-9]|203[0-6])-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])|(2037-(0[1-9]|1[0-1])-(0[1-9]|[12][0-9]|3[01])))$', startingDate)

                    if not p:
                        print("Iligeal form of date. (1970-01-01 ~ 2037-11-30)")
                        input()
                        os.system('cls')
                        continue
                    
                    check = True
                    while check:
                        try:
                            now = datetime(int(list[0]), int(list[1]), int(list[2]))
                            break
                        except ValueError:
                            print("Inexistent form of date followed by Gregorian Calendar")
                            input()
                            os.system('cls')
                            check = False
                    
                    if not check:
                        continue

                    if pre > now:
                        print("Starting date is earlier than date of birth.")
                        input()
                        os.system('cls')
                        continue
                    
                    if not isNew and self.startingDate == startingDate:
                        print("You have entered the same value as before.")
                        input()
                        os.system('cls')
                        continue

                    if not isNew:
                        print("Your starting date has been modified.")
                        input()

                    self.startingDate = startingDate
                    os.system('cls')
                    break
            elif i == 5:
                while True:
                    height = input("Enter your height (aaa.bb) : ")
                    
                    if len(height) != 6:
                        print("Illegal form of height. Length of height is total 6 character.")
                        input()
                        os.system('cls')
                        continue
                    
                    if height.find('.') == -1 or len(height.split('.')[0]) != 3 or len(height.split('.')[1]) != 2:
                        print("Illegal form of height. Height is consisted with 3 integer and 2 decimal classified with '.'.")
                        input()
                        os.system('cls')
                        continue

                    if int(height.split('.')[0]) < 100:
                        print("Integer part of weight must be 100 or more.")
                        input()
                        os.system('cls')
                        continue

                    if not isNew and self.height == height:
                        print("You have entered the same value as before.")
                        input()
                        os.system('cls')
                        continue

                    if not isNew:
                        print("Your height has been modified.")
                        input()
                    
                    self.height = height
                    os.system('cls')
                    break
            elif i == 6:
                while True:
                    weight = input("Enter your weight (aa.bb) or (aaa.bb) : ")

                    if len(weight) < 5 or len(weight) > 6:
                        print("Illegal form of weight. Length of weight is total 5 or 6 character.")
                        input()
                        os.system('cls')
                        continue

                    if weight.find('.') == -1 or len(weight.split('.')[0]) < 2 or len(weight.split('.')[0]) > 3 or len(weight.split('.')[1]) != 2:
                        print("Illegal form of weight. Weight is consisted with 2 or 3 integer and 2 decimal classified with '.'.")
                        input()
                        os.system('cls')
                        continue

                    if int(weight.split('.')[0]) < 10:
                        print("Integer part of weight must be 10 or more.")
                        input()
                        os.system('cls')
                        continue

                    if not isNew and self.weight == weight:
                        print("You have entered the same value as before.")
                        input()
                        os.system('cls')
                        continue

                    if not isNew:
                        print("Your weight has been modified.")
                        input()
                    
                    self.weight = weight
                    os.system('cls')
                    break
        
        # If you have a new account, the personal information of the user entered above is recorded in "profile.txt".
        if isNew:
            f.write(self.name + "\n")
            f.write(self.gender + "\n")
            f.write(self.birth + "\n")
            f.write(self.startingDate + "\n")
            f.write(self.height + " (cm)\n")
            f.write(self.weight + " (kg)\n")
            f.close()

    # Clear account.
    def clear(self):
        shutil.rmtree("./user")
        self.__init__()


    # Revise profile.
    def revise(self, list):
        filePath = "./user/profile.txt"
        self.create(list)
        
        # file clear
        os.remove(filePath)

        # file rewrite
        f = open(filePath, 'w')

        f.write(self.name + "\n")
        f.write(self.gender + "\n")
        f.write(self.birth + "\n")
        f.write(self.startingDate + "\n")
        f.write(self.height + "\n")
        f.write(self.weight + "\n")

        f.close()
        self.__init__()

    # Print profile.
    def view(self):
        print("1. Name : " + self.name + "\n")
        print("2. Gender : " + self.gender + "\n")
        print("3. Birth : " + self.birth + "\n")
        print("4. Starting time : " + self.startingDate + "\n")
        print("5. Height : " + self.height + " (cm)\n")
        print("6. Weight : " + self.weight + " (kg)\n")