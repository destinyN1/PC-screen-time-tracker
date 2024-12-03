import sqlite3


def init_db():
    """
    Initialize the database and create the screentime table if it doesn't exist.
    """
    connection = sqlite3.connect('screentime.db')
    cursor = connection.cursor()

    print("Database created and connected successfully")

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS screentime (
            app_name TEXT NOT NULL,
            app_name_subset TEXT NOT NULL,
            total_duration REAL,
            last_active TEXT,
            first_active TEXT,
            times_opened INTEGER,
            PRIMARY KEY (app_name, app_name_subset)
        )
    ''')

    connection.commit()
    connection.close()

    print("Table 'Screentime' created successfully")


def update_db(app_name, app_name_subset, total_duration, last_active, first_active, times_opened):
    """
    Update the database with app usage information, or insert if it doesn't exist.
    """
    connection = sqlite3.connect('screentime.db')
    cursor = connection.cursor()

    cursor.execute('''
            INSERT INTO screentime (app_name, app_name_subset, total_duration, last_active, first_active, times_opened)
            VALUES (?, ?, ?, ?, ?, ?)
            ON CONFLICT(app_name, app_name_subset)
            DO UPDATE SET
                total_duration = excluded.total_duration,
                last_active = excluded.last_active,
                times_opened = excluded.times_opened;
        ''', (app_name, app_name_subset, total_duration, last_active, first_active, times_opened))

        

