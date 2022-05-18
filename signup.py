import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="MyDiary"
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