import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Snehal@45',
    database = 'course'
)

sql = 'select * from students'

cursor = conn.cursor()

cursor.execute(sql)
results = cursor.fetchall()

for result in results:
    print(result)

cursor.close()

conn.close()