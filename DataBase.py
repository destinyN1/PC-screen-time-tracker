import sqlite3

with sqlite3.connect('screentime') as connection:

 cursor = connection.cursor()

 print("Database created and connected succesfully")

 create_table_query = '''
 CREATE TABLE IF NOT EXISTS Screentime (
     id INTEGER PRIMARY KEY AUTOINCREMENT,
     appname TEXT NOT NULL,
     duration FLOAT NOT NULL,
     FIRST_TIME_CLOSED INTEGER, 
     LAST_CLOSED INTEGER,
     TIMES_OPENED INTEGER
 );
'''
 cursor.execute(create_table_query)

 connection.commit()

 print("Table 'Screen time' createed succesfully")


