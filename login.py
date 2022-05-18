from mysql.connector import connect

db = connect(
    host="localhost",
    user="root",
    password="root",
    database="MyDiary"
)

