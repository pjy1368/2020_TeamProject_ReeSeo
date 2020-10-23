import os
import shutil

class Account:
    def __init__(self):
        self.name = None
        self.gender = None
        self.birth = None
        self.height = None
        self.weight = None
        self.currentTime = None

    def init(self):
        filePath = os.path.join("./user", "profile.txt")
        f = open(filePath, "r")
        s = f.readlines()

        self.name = s[0].split('\n')[0]
        self.gender = s[1].split('\n')[0]
        self.birth = s[2].split('\n')[0]
        self.height = s[3].split('\n')[0]
        self.weight = s[4].split('\n')[0]
        self.currentTime = s[5].split('\n')[0]

        f.close()

    # Does the account exist?
    def isMember(self):
        if os.path.isdir("./user"):
            self.init()

        return os.path.isdir("./user")

    # Create account.
    def create(self):
        os.mkdir("./user")

        filePath = os.path.join("./user", "profile.txt")
        f = open(filePath, "w")

        name = input("Enter name : ")
        f.write(name + "\n")

        gender = input("Enter gender : ")
        f.write(gender + "\n")

        birth = input("Enter the date of birth (YYYY-MM-DD) : ")
        f.write(birth + "\n")

        height = input("Enter height : ")
        f.write(height + "\n")

        weight = input("Enter weight : ")
        f.write(weight + "\n")

        currentTime = input("Enter current time : ")
        f.write(currentTime + "\n")

        f.close()
        self.init()

    # Clear account.
    def clear(self):
        shutil.rmtree("./user")

    # Revise profile.
    def revise(self, list):
        filePath = os.path.join("./user", "profile.txt")
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
                print(str(idx) + ". Height : " + s[i - 1])
                self.height = input("Enter height : ")
            elif i == 5:
                print(str(idx) + ". Weight : " + s[i - 1])
                self.weight = input("Enter weight : ")
            elif i == 6:
                print(str(idx) + ". Current time : " + s[i - 1])
                self.currentTime = input("Enter current time : ")
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
        filePath = os.path.join("./user", "profile.txt")
        f = open(filePath, 'r')

        print("1. Name : " + self.name + "\n")
        print("2. Gender : " + self.gender + "\n")
        print("3. Birth : " + self.birth + "\n")
        print("4. Height : " + self.height + " (cm)\n")
        print("5. Weight : " + self.weight + " (kg)\n")
        print("6. Current time : " + self.currentTime + "\n")

        f.close()