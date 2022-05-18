from typing_extensions import Self
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="MyDiary"
)
myCursor = db.cursor()


class SignUp:
    def __init__(self, userName, Password):
        pass

myCursor.execute("SHOW DATABASES")
for x in myCursor:
    print(x)