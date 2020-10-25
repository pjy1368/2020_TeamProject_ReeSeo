import os
import shutil
import re
from Goal import Goal
from WorkOut import WorkOut
from datetime import datetime

class Account:
    def __init__(self):
        if self.isMember():
            filePath = "./user/profile.txt"
            f = open(filePath, "r")
            s = f.readlines()
        
            self.name = s[0].split('\n')[0]
            self.gender = s[1].split('\n')[0]
            self.birth = s[2].split('\n')[0]
            self.currentTime = s[3].split('\n')[0]
            self.height = s[4].split('\n')[0]
            self.weight = s[5].split('\n')[0]
            self.goal = Goal(self)
            self.workOut = WorkOut()

            f.close()
        else:
            self.name = None
            self.gender = None
            self.birth = None
            self.currentTime = None
            self.height = None
            self.weight = None

    # Does the account exist?
    def isMember(self):
        return os.path.isdir("./user")

    # Create account.
    def create(self):
        os.mkdir("./user")

        filePath = "./user/profile.txt"
        f = open(filePath, "w")

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
                        
            f.write(name + "\n")
            os.system('cls')
            break
        
        while True:
            gender = input("Enter gender (1. Female 2. Male) : ")

            if len(gender) != 1:
                print("Length of name must be 1.")
                input()
                os.system('cls')
                continue
            
            if gender < '1' or gender > '2':
                print("Only one Digit: 1 or 2 are legal.")
                input()
                os.system('cls')
                continue
            
            if gender == '1':
                f.write("Female\n")
            else:
                f.write("Male\n")

            os.system('cls')
            break
        
        while True:
            birth = input("Enter the date of birth (YYYY-MM-DD) : ")
            
            if len(birth) != 10:
                print("Length of string must be 10.")
                input()
                os.system('cls')
                continue
            
            if birth[4] != '-' or birth[7] != '-':
                print("Each year,month and date are must classified as '-' with followed form (YYYY-MM-DD)")
                input()
                os.system('cls')
                continue
            
            list = birth.split('-')

            if len(list[0]) != 4 or len(list[1]) != 2 or len(list[2]) != 2:
                print("Each year,month and date are must classified as '-' with followed form (YYYY-MM-DD)")
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
                    date = datetime(int(list[0]), int(list[1]), int(list[2]))
                    break
                except ValueError:
                    print("Inexistent form of date followed by Gregorian Calendar")
                    input()
                    os.system('cls')
                    check = False
            
            if not check:
                continue

            f.write(birth + "\n")
            os.system('cls')
            break

        while True:
            currentTime = input("Enter current time (YYYY-MM-DD) : ")
            
            if len(currentTime) != 10:
                print("Length of string must be 10.")
                input()
                os.system('cls')
                continue
            
            if currentTime[4] != '-' or currentTime[7] != '-':
                print("Each year,month and date are must classified as '-' with followed form (YYYY-MM-DD)")
                input()
                os.system('cls')
                continue
            
            list = currentTime.split('-')

            if len(list[0]) != 4 or len(list[1]) != 2 or len(list[2]) != 2:
                print("Each year,month and date are must classified as '-' with followed form (YYYY-MM-DD)")
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


            p = re.search(r'^((19[7-9][0-9]|20[0-2][0-9]|203[0-6])-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])|(2037-(0[1-9]|1[0-1])-(0[1-9]|[12][0-9]|3[01])))$', currentTime)

            if not p:
                print("Iligeal form of date. (1970-01-01 ~ 2037-11-30)")
                input()
                os.system('cls')
                continue
            
            check = True
            while check:
                try:
                    date = datetime(int(list[0]), int(list[1]), int(list[2]))
                    break
                except ValueError:
                    print("Inexistent form of date followed by Gregorian Calendar")
                    input()
                    os.system('cls')
                    check = False
            
            if not check:
                continue

            f.write(currentTime + "\n")
            os.system('cls')
            break

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

            f.write(height + "\n")
            os.system('cls')
            break
        
        while True:
            weight = input("Enter your weight (aa.bb) : ")

            if len(weight) != 5:
                print("Illegal form of weight. Length of weight is total 5 character.")
                input()
                os.system('cls')
                continue

            if weight.find('.') == -1 or len(weight.split('.')[0]) != 2 or len(weight.split('.')[1]) != 2:
                print("Illegal form of height. Height is consisted with 3 integer and 2 decimal classified with '.'.")
                input()
                os.system('cls')
                continue

            if int(weight.split('.')[0]) < 10:
                print("Integer part of weight must be 10 or more.")
                input()
                os.system('cls')
                continue

            f.write(weight + "\n")
            os.system('cls')
            break

        f.close()
        self.__init__()

    # Clear account.
    def clear(self):
        shutil.rmtree("./user")
        self.__init__()


    # Revise profile.
    def revise(self, list):
        filePath = "./user/profile.txt"
        f = open(filePath, 'r')
        s = f.readlines()
        
        idx = 1
        for i in list:
            i = int(i)

            if i == 1:
                print(str(idx) + ". Name : " + s[i - 1])
                self.name = input("Enter name : ")
            elif i == 2:
                print(str(idx) + ". Gender : " + s[i - 1])
                self.gender = input("Enter gender : ")
            elif i == 3:
                print(str(idx) + ". Birth : " + s[i - 1])
                self.birth = input("Enter birth : ")
            elif i == 4:
                print(str(idx) + ". Current time : " + s[i - 1])
                self.currentTime = input("Enter current time : ")
            elif i == 5:
                print(str(idx) + ". Height : " + s[i - 1] + " (cm)")
                self.height = input("Enter height : ")
            elif i == 6:
                print(str(idx) + ". Weight : " + s[i - 1] + " (kg)")
                self.weight = input("Enter weight : ")

            idx += 1
        
        # file clear
        f.close()
        os.remove(filePath)

        # file rewrite
        f = open(filePath, 'w')

        f.write(self.name + "\n")
        f.write(self.gender + "\n")
        f.write(self.birth + "\n")
        f.write(self.height + "\n")
        f.write(self.weight + "\n")
        f.write(self.currentTime + "\n")

        f.close()

    # Print profile.
    def view(self):
        filePath = "./user/profile.txt"
        f = open(filePath, 'r')

        print("1. Name : " + self.name + "\n")
        print("2. Gender : " + self.gender + "\n")
        print("3. Birth : " + self.birth + "\n")
        print("4. Current time : " + self.currentTime + "\n")
        print("5. Height : " + self.height + " (cm)\n")
        print("6. Weight : " + self.weight + " (kg)\n")

        f.close()