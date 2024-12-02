import sqlite3

with sqlite3.connect('screentime') as connection:

 cursor = connection.cursor()

 print("Database created and connected succesfully")

 create_table_query = '''
 CREATE TABLE IF NOT EXISTS Screentime (
     id INTEGER PRIMARY KEY AUTOINCREMENT,
     app_name TEXT NOT NULL,                    
     app_name_subset TEXT,
     total_duration FLOAT NOT NULL,
     last_session FLOAT NOT NULL,
     first_time_opened INTEGER NOT NULL,  
     times_opened INTEGER NOT NULL
 );
'''

 cursor.execute(create_table_query)

 connection.commit()

 print("Table 'Screen time' createed succesfully")


#App_name,app_name_subset,times_opened, total_duration, last_session - first_time_opened - DONE



