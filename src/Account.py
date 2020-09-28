import os
import shutil

class Account:
    name = None
    sex = None
    age = None
    height = None
    weight = None

    # Does the account exist?
    def isMember(self):
        return os.path.isdir("./user")

    # Create account.
    def create(self):
        os.mkdir("./user")

        filepath = os.path.join("./user", "profile.txt")
        f = open(filepath, "w")
        f.close

    # clear account.
    def clear(self):
        shutil.rmtree("./user")

