import sqlite3 as sq

con = sq.connect('school.sqlite3')
cur = con.cursor()

que_in = '''
INSERT INTO class (name, surname, mark) VALUES
    ('Василий', 'Пупкин', 3),
    ('Денис', 'Синицин', 4),
    ('Ангелина', 'Соколова', 5),
    ('Саша', 'Петров', 2),
    ('ЫЫЫЫ', 'ЫЫЫЫ', 4)
'''

cur.execute(que_in)
con.commit()

con.close()