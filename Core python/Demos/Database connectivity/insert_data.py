import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Snehal@45',
    database = 'course'
)

sql = 'insert into students values(%s, %s, %s)'
values =(4,'Snehal','Python DS with AI')
cursor = conn.cursor()

cursor.execute(sql,values)

conn.commit()
print('Student added successfully.')

cursor.close()

conn.close()