import sqlite3

with sqlite3.connect('screentime') as connection:

 cursor = connection.cursor()

 print("Database created and connected succesfully")

 create_table_query = '''
 CREATE TABLE IF NOT EXISTS Screentime (
     id INTEGER PRIMARY KEY AUTOINCREMENT,
     app_name TEXT NOT NULL,
     total_duration FLOAT NOT NULL,
     current_duration
     FIRST_TIME_CLOSED INTEGER, 
     last_closed INTEGER,
     times_opened INTEGER
 );
'''
 cursor.execute(create_table_query)

 connection.commit()

 print("Table 'Screen time' createed succesfully")


