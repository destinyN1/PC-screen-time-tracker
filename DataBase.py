import sqlite3

conn = sqlite3.connect('screen_time.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS screen_time (
id I
               )
             ''')  