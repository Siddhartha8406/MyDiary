import mysql.connector
from mysql.connector import connect     #importing only connect as it is the only required and can also be a bit more efficient
import json
from configparser import ConfigParser

#MyCursor.execute("CREATE DATABASE MyDiary")
config=ConfigParser()
config.read("config.ini")
db = connect(
    host=config.get("database", "host"),
    user=config.get("database", "user"),
    password=config.get("database", "password"),
    database=config.get("database", "database")
)
"""Using .ini file to get database info"""

myCursor = db.cursor()

def new_event(userID, Date, Title, Event):
    userID = "VR74"
    myCursor.execute(f"CREATE TABLE IF NOT EXISTS {userID}(Date DATE, Title VARCHAR(225), Description VARCHAR(1024))")

    #myCursor.execute("INSERT INTO VR74 (Date, Title, Description) VALUES('2006-04-08','Birth1', 'I was Born on this date')")
    myCursor.execute("SELECT * FROM VR74")
    for x in myCursor:
        print(x)