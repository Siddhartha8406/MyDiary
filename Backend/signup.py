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


def signUp(userName, password):
    query = "INSERT INTO Cred (userName, pwd) VALUES (%s, %s)"
    values = (userName, password)
    myCursor.execute(query,values)
    db.commit()

def ShowCreds():
    myCursor.execute("SELECT * FROM Cred")
    a = myCursor.fetchall()
    for x in a:
        print(x)

if __name__=="__main__":
    ShowCreds()