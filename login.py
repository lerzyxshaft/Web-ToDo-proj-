import os 
import json

class Pass:
        
    def registration(self):

        with open("users.json", "r") as f:
            users = json.load(f)

        us = input("Fill this gap with your username:\nIt need to be beetween 10-15 char: ")
        if len(us) < 5 or len(us) > 12:
            print("Username has wrong lenth, it need to be from 5 to 12 char!")
        elif self.us_check(us):
            print("Username already exists")
        else:
            pass

        passw = input("Fill this gap with your password:\nIt need to be between 10-15 char: ")
        if len(passw) <10 or len(passw) > 15:
            print("Password has wrong lenth, it need to be from 10 to 20 char!")

        new_user = {
            "id": len(users)+1,
            "username": us,
            "password": passw
        }
        users.append(new_user)

        with open("users.json", "w", encoding = "utf8") as f:
            json.dump(users, f, indent = 4)

        print("You was successfully registrated!")


    def us_check(self, x):
        users = open("users.json", "r")
        data = json.load(users)  
        for us in data:
            if x == us['username']:
                return True
        return False

    def is_reg_check(self, x):
        with open("users.json", "r") as users:
            data = json.load(users)
        for usernm in data:
            if x == usernm['username']:
                return False 
        return True 

    def pass_check(self, x):
        with open("users.json", "r") as users:
            data = json.load(users)
        for password in data:
            if x == password['password']:
                return True
        return False

    def log_in(self):
        usernm = input("Fill this gap with your username:")
        if self.is_reg_check(usernm):
            ad_reg = int(input("You are not registered yet;/\nInput 1 if you want to"))
            if ad_reg == 1:
                self.registration()
            else:
                pass
        else:
            with open("users.json", "r") as f:
                users = json.load(f)

            if self.is_reg_check(usernm):
                pass
            else:
                print("")
            login_pass = input("Fill this gap with your password")
            if self.pass_check(login_pass):
                print("Succssessfull login")
            else:
                print("Wrong password, try again")

        
def init_file():
    if not os.path.exists("users.json"):
        with open("users.json", "w") as f:
            json.dump([], f)


def main():
    app = Pass()
    while True:
        with open("users.json") as f:
            data = json.load(f)

        log = int(input("Print 1 if you already have account.\nPrint  2 if you want to registrate an account:"))
        if log == 1:
            app.log_in()
        elif log == 2:
            app.registration()
        elif log !=1 or log != 2:
            print("Wrong input")


init_file()
main()