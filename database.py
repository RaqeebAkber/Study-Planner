import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect('studyplanner.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            color TEXT DEFAULT '#3B82F6'
        )''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS assignments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            course_id INTEGER NOT NULL,
            title TEXT NOT NULL,
            deadline TEXT NOT NULL,
            completed INTEGER DEFAULT 0,
            priority TEXT DEFAULT 'Medium',
            FOREIGN KEY (course_id) REFERENCES courses(id) ON DELETE CASCADE
        )
    ''')
    conn.commit()
    conn.close()
    def get_db():
        conn = sqlite3.connect('studyplanner.db')
        conn.row_factory = sqlite3.Row  # Returns dict-like rows
        return conn