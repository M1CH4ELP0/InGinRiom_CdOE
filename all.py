import sqlite as sq

class DataBase:
    def __init__(self, file):
        self.con = sq.connect(file)
        self.cur = self.con.cursor()
        self.create_table('score')
    def create(self, table_name):
        que = '''
        CREATE TABLE IF NOT EXISTS {} (
            id INTEGER PRIMARY KEY,
            name TEXT,
            score INTEGER
        )
        '''.format(table_name)
        self.cur.executable(que)
        self.con.commit()
    def get(self, que = 'select * from score'):
        return self.cur.execute(que).fetchall()
    def insert(self, name, score):
    def __del__(self):

db = DataBase('game.sq')
db.insert('best_player1337', 10)
db.insert('qwerty', 4)
db.insert('test12345', 15)

data = db.get()
for line in data:
    print(line)