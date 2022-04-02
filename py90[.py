import sqlite3 as sq

con = sq.connect('school.sqlite3')
cur = con.cursor()

que = '''
CREATE TABLE IF NOT EXISTS class (
    id INTEGER PRIMARY KEY,
    name TEXT,
    surname TEXT,
    mark INTEGER
)
'''

cur.execute(que)
con.commit()

con.close()