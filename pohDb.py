import sqlite3

sqlite_file = 'labAccess_db.sqlite'    # name of the sqlite database file

# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()
print('Connected to db')

c.execute('''CREATE TABLE members(
    id INTEGER PRIMARY KEY NOT NULL, NAME TEXT NOT NULL,STATUS TEXT, VALUE REAL)''')