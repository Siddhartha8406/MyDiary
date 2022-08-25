from pickle import FALSE, TRUE
from mysql.connector import connect
from configparser import ConfigParser
from random import randint

config=ConfigParser()
config.read("config.ini")
db = connect(
    host=config.get("database", "host"),
    user=config.get("database", "user"),
    password=config.get("database", "password"),
    database=config.get("database", "database")
)
myCursor = db.cursor()


"""
1. Use check_creds() to verify the given credentials

2. check_creds() first uses fgt_pass_check_username() to verufy username 
    If true, it checks if ID matches
    IF false returns False and if condition breaks

3. If everything is correct it returns a tupple of ("True", "Verificarion Code")

4. Use the verification code(@[1]) along with password to change the pass
            pass change("New password", "verification Code")
    Only if the code is same as returned (in 3) then the password will be changed


USE
    cls = forgot_pass('usename', 'password')
    verify = cls.check_creds()
    cls.pass_change("NewPass", VerificationCode)
"""
class forgot_pass:
    def __init__(self, username, userID):
        self.userName = username
        self.userID = int(userID)       #used int to remove the data type errors.

    def check_creds(self):
        exists = False
        verification_code = 0000000
        if self.fgt_pass_check_username():       #checks if the username exists and if it exits thn checks for UserID existance
            if self.fgt_pass_check_userID():
                exists=True
                verification_code = self.create_verification_code()
        return (exists, verification_code)

    def fgt_pass_check_username(self):                 #Checks if the given username exists
        exists = False
        myCursor.execute("SELECT userName FROM Cred")
        usernames = myCursor.fetchall()
        for x in usernames:
            if x[0]==self.userName:             #x[0] is given becauses usernames is a 3d array, [(value1), (value2)]
                exists = True
                break
        del usernames
        return exists
    
    def fgt_pass_check_userID(self):
        myCursor.execute(f"SELECT userID FROM Cred WHERE userName='{self.userName}'")
        ID = myCursor.fetchone()[0]
        exists = False
        if self.userID==ID:
            exists=True
        return exists

    def create_verification_code(self):
        i=0
        self.security_code = str()
        while i<7:
            self.security_code += str(randint(0,9))
            i+=1
        return self.security_code

    def pass_change(self, newPass, verification_code):
        if verification_code == self.security_code:
            print("AUTHORISED")
        else:
            print("UNAUTHORISED")

if __name__ == "__main__":
    cls = forgot_pass('Sid', '7474')
    av = cls.check_creds()
    if av[0]:
        cls.pass_change("sssss", av[1])
    else:
        print("UNAUTHORISED")