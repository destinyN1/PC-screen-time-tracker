import sqlite3

def init_db():
    """
    Initialize the database and create the screentime table if it doesn't exist.
    """
    connection = sqlite3.connect('screentime.db')
    cursor = connection.cursor()

    print("Database created and connected successfully.")

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS screentime (
            current_app TEXT,
            main_app TEXT NOT NULL,
            sub_app TEXT, -- Changed to TEXT to match app naming convention
            total_duration_window INTEGER,
            first_active TEXT,
            last_active TEXT,
            times_opened INTEGER,
            PRIMARY KEY (current_app, main_app, sub_app)
        )
    ''')
    connection.commit()
    connection.close()
    print("Table 'screentime' created successfully.")

def update_database(current_app, main_app, sub_app, total_duration, first_active, last_active, times_opened):
    """
    Updates the screentime table with the provided data.
    If a record with the same primary keys (current_app, main_app, sub_app) exists, it will be replaced.
    """
    connection = sqlite3.connect('screentime.db')
    cursor = connection.cursor()

    cursor.execute('''
        INSERT OR REPLACE INTO screentime 
        (current_app, main_app, sub_app, total_duration_window, first_active, last_active, times_opened)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (current_app, main_app, sub_app, total_duration, first_active, last_active, times_opened))

    connection.commit()
    connection.close()
    print(f"Updated database for window '{current_app}', main app '{main_app}', sub app '{sub_app}'.")