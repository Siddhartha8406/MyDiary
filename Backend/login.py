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

def login(userName, password):
    myCursor.execute(f"SELECT pwd FROM Cred WHERE userName='{userName}'")
    pwd = myCursor.fetchone()
    myCursor.execute(f"SELECT userID FROM Cred WHERE userName='{userName}'")
    id = myCursor.fetchone()
    
    #using for first take only the password, then check if passwords don't match 
    #if they don't return Flase and #0000 as id
    for pwd in pwd:
        if pwd!=password:
            return False, "#0000"
    
    #if the above condition fail it means passwords match so just return Ture and the ID
    for id in id:
        return True, id

if __name__ == "__main__":
    print(login('Sid', "Sid7777"))