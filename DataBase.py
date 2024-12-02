import sqlite3

with sqlite3.connect('screentime') as connection:

 cursor = connection.cursor()

 print("Database created and connected succesfully")

 create_table_query = '''
 CREATE TABLE IF NOT EXISTS Screentime (
     app_name TEXT PRIMARY KEY,                    
     app_name_subset TEXT,
     total_duration REAL NOT NULL,
     last_session TEXT,
     first_time_opened TEXT,  
     times_opened INTEGER
 );
'''

 cursor.execute(create_table_query)

 connection.commit()

 print("Table 'Screen time' createed succesfully")


#App_name,app_name_subset,times_opened, total_duration, last_session - first_time_opened - DONE


def update_db(app_name, app_name_subset, total_duration,last_session,first_time_opened,times_opened):

 conn = sqlite3.connect(f'screentime')
 cursor = conn.cursor()
 cursor.execute(
  
 )