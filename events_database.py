import sqlite3

def init_db():
    conn = sqlite3.connect('events.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            date TEXT NOT NULL,
            time TEXT NOT NULL,
            link TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_event(name, date, time, link):
    conn = sqlite3.connect('events.db')
    c = conn.cursor()
    c.execute('INSERT INTO events (name, date, time, link) VALUES (?, ?, ?, ?)', (name, date, time, link))
    conn.commit()
    conn.close()

def get_events():
    conn = sqlite3.connect('events.db')
    c = conn.cursor()
    c.execute('SELECT * FROM events')
    events = c.fetchall()
    conn.close()
    return events

def delete_event(event_id):
    conn = sqlite3.connect('events.db')
    c = conn.cursor()
    c.execute('DELETE FROM events WHERE id = ?', (event_id,))
    conn.commit()
    conn.close()