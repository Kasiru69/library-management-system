import sqlite3

conn = sqlite3.connect('library.db')
conn.commit()
conn.close()