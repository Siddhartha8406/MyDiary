from mysql.connector import connect
from configparser import ConfigParser

config=ConfigParser()
config.read("config.ini")
db = connect(
    host=config.get("database", "host"),
    user=config.get("database", "user"),
    password=config.get("database", "password"),
    database=config.get("database", "database")
)
myCursor = db.cursor()

def Login(userName, password):
    myCursor.execute(f"SELECT pwd FROM Cred WHERE userName='{userName}'")
    pwd = myCursor.fetchone()
    myCursor.execute(f"SELECT userID FROM Cred WHERE userName='{userName}'")
    id = myCursor.fetchone()
    for x in pwd:
        for y in id:
            return(x==password), y

print(Login('Sid', "Sid7777"))