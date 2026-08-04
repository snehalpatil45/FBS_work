import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Snehal@45'
)

sql = 'create database course'

cursor = conn.cursor()

cursor.execute(sql)

cursor.close()

conn.close()