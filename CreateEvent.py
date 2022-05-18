import mysql.connector
from mysql.connector import connect     #importing only connect as it is the only required and can also be a bit more efficient
import json

#MyCursor.execute("CREATE DATABASE MyDiary")
db = connect(
    host="localhost",
    user="root",
    password="root",
    database="MyDiary"
)
myCursor = db.cursor()

userID = "VR74"

myCursor.execute(f"CREATE TABLE IF NOT EXISTS {userID}(Date DATE, Title VARCHAR(225), Description VARCHAR(1024))")

#myCursor.execute("INSERT INTO VR74 (Date, Title, Description) VALUES('2006-04-08','Birth1', 'I was Born on this date')")

myCursor.execute("SELECT * FROM VR74")
for x in myCursor:
    print(x)