from mysql.connector import connect

db = connect(
    host="localhost",
    user="root",
    password="root",
    database="MyDiary"
)
myCursor = db.cursor()

def Login(userName, password):
    myCursor.execute(f"SELECT pwd FROM Cred WHERE userName='{userName}'")
    pwd = myCursor.fetchone()
    for x in pwd:
        return(x==password)

#print(Login('Sid', "Sid7777"))