import mysql.connector

class Datastore:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host = 'localhost',
                user = 'root',
                password = 'Snehal@45',
                database = 'snehal'
            )
            self.cursor = self.conn.cursor()

        except Exception as e:
            print('Error:',e)

    def addData(emp,table_name):
        pass