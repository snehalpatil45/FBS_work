import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Snehal@45',
    database = 'course'
)

sql = 'insert into students values(%s, %s, %s)'
values =[(1,'Snehal','Python DS with AI'),(2,'divya','Java'),(3,'Roshni','testing')]
cursor = conn.cursor()

cursor.executemany(sql,values)

conn.commit()
print('Student added successfully.')

cursor.close()

conn.close()