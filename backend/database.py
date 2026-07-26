import sqlite3

DATABASE_NAME = "jobpilot.db"

def create_connection():
    connection = sqlite3.connect(DATABASE_NAME)
    return connection

def create_tables():
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT UNIQUE,
        password TEXT
    )
    """)

    connection.commit()
    connection.close()

if __name__ == "__main__":
    create_tables()
    print("Database created successfully!")
