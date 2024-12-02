import sqlite3

with sqlite3.connect('screentime') as connection:

 cursor = connection.cursor()

 print("Database created and connected succesfully")

 create_table_query = '''
 CREATE TABLE IF NOT EXISTS Screentime (
     app_name TEXT NOT NULL,                  
     app_name_subset TEXT NOT NULL,
     total_duration REAL,
     last_active TEXT,
     first_active TEXT,  
     times_opened INTEGER,
     
     PRIMARY KEY (app_name, app_name_subset) 
 );
'''

 cursor.execute(create_table_query)

 connection.commit()

 print("Table 'Screen time' createed succesfully")


#App_name,app_name_subset,times_opened, total_duration, last_session - first_time_opened - DONE


def update_db(app_name, app_name_subset, total_duration,last_active,first_active,times_opened):

 conn = sqlite3.connect(f'screentime')
 cursor = conn.cursor()
 cursor.execute('''
 INSERT INTO screetime(app_name, app_name_subset, total_duration,last_session,first_time_opened,times_opened)
 VALUES(?,?,?,?,?,?)
 ON CONFLICT(app_name, app_name_subset)
 DO UPDATE SET
     total_duration = excluded.total_duration
     last_active = excluded.last_active
    times_opened = excluded.times_opened  
''',(app_name,app_name_subset,total_duration,last_active,first_active,times_opened))    
 
 connection.commit()
 connection.close()