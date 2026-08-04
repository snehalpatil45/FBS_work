import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Snehal@45',
    database = 'course'
)

sql = 'create table students(id int,name varchar(20),course varchar(20))'

cursor = conn.cursor()

cursor.execute(sql)

cursor.close()

conn.close()