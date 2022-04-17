import sqlite3 as sq
from random import choice

class DataBase:
    def __init__(self, file):
        self.con = sq.connect(file)
        self.cur = self.con.cursor()
        self.create_table('score')
    def create_table(self, table_name):
        que = '''
        CREATE TABLE IF NOT EXISTS {} (
            id INTEGER PRIMARY KEY,
            name TEXT,
            score_points INTEGER,
            frags INTEGER
        )
        '''.format(table_name)
        self.cur.execute(que)
        self.con.commit()
    def get(self, que = 'select name, score_points from score ORDER BY score_points DESC'):
        return self.cur.execute(que).fetchall()
    def insert(self, name, score, frags):
        que_insert = f'''
        INSERT INTO score (name, score_points, frags)
        VALUES ('{name}', {score}, {frags})
        '''
        self.cur.execute(que_insert)
        self.con.commit
    def __del__(self):
        self.con.close()

pool_1 = ('best_player1337','qwerty', 'test12345', 'xXxlox228xXx', '___xXxlox228xXx___')
pool_2 = tuple(range(0, 100))
pool_3 = tuple(range(0, 15))

db = DataBase('game.sqlite')

for i in range(12):
    name_ins = choice(pool_1)
    score_ins = choice(pool_2)
    frags_ins = choice(pool_3)
    db.insert(name_ins, score_ins, frags_ins)
data = db.get()
for line in data:
    print(line)