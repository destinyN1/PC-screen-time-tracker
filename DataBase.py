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
            Durmain INTEGER,        
            first_active TEXT,
            last_active TEXT,
            times_opened INTEGER,
            PRIMARY KEY (current_app, main_app, sub_app, first_active)
        )
    ''')
    connection.commit()
    connection.close()
    print("Table 'screentime' created successfully.")

def update_database(current_app, main_app, sub_app, total_duration, Durmain, first_active, last_active, times_opened):
    """
    Updates the screentime table with the provided data, including the Durmain variable.
    - Preserves first_active for existing records.
    - Updates all other fields if a record with the same current_app, main_app, sub_app exists.
    """
    connection = sqlite3.connect('screentime.db')
    cursor = connection.cursor()

    # Insert new record if it doesn't exist
    cursor.execute('''
        INSERT OR IGNORE INTO screentime 
        (current_app, main_app, sub_app, first_active, total_duration_window, Durmain, last_active, times_opened)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (current_app, main_app, sub_app, first_active, total_duration, Durmain, last_active, times_opened))

    # Update existing record's fields, excluding first_active
    cursor.execute('''
        UPDATE screentime
        SET total_duration_window = ?,
            Durmain = ?,
            last_active = ?,
            times_opened = ?
        WHERE current_app = ? AND main_app = ? AND sub_app = ?
    ''', (total_duration, Durmain, last_active, times_opened, current_app, main_app, sub_app))

    connection.commit()
    connection.close()

    # Debug message
