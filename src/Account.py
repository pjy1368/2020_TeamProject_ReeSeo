import os
import shutil

class Account:
    def __init__(self):
        self.name = None
        self.sex = None
        self.age = None
        self.height = None
        self.weight = None

    # Does the account exist?
    def isMember(self):
        return os.path.isdir("./user")

    # Create account.
    def create(self):
        os.mkdir("./user")

        filePath = os.path.join("./user", "profile.txt")
        f = open(filePath, "w")

        name = input("Name : ")
        f.write(name + "\n")

        sex = input("Sex : ")
        f.write(sex + "\n")

        age = input("Age : ")
        f.write(age + "\n")

        height = input("Height : ")
        f.write(height + "\n")

        weight = input("Weight : ")
        f.write(weight + "\n")

        f.close()

    # Clear account.
    def clear(self):
        shutil.rmtree("./user")

    def revise(self):
        print()

    def view(self):
        filePath = os.path.join("./user", "profile.txt")
        f = open(filePath, 'r')
        for s in f:
            print(s, end='')
        f.close()