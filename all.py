import sqlite3 as sq
from random import choice

class Users:
    def __init__(self, file):
        self.con = sq.connect(file)
        self.cur = self.con.cursor()
        self.create_table('USERS')
    def create_table(self, table_name):
        que = '''
        CREATE TABLE IF NOT EXISTS {} (
            id INTEGER PRIMARY KEY,
            name TEXT,
            cash INTEGER,
            year INTEGER
        )
        '''.format(table_name)
        self.cur.execute(que)
        self.con.commit()
    def get(self, que = 'select * from USERS ORDER BY year ASC'):
        return self.cur.execute(que).fetchall()
    #def get(self, que = 'select name, cash, year from USERS'):
        #return self.cur.execute(que).fetchall()
    def delete(self, name):
        que_del = f'''
        DELETE from USERS WHERE name = '{name}'
        '''
        self.cur.execute(que_del)
        self.con.commit
    def insert(self, name, cash, year):
        que_insert = f'''
        INSERT INTO USERS (name, cash, year)
        VALUES ('{name}', {cash}, {year})
        '''
        self.cur.execute(que_insert)
        self.con.commit
    def add_money(self, id, money):
        que_add = f'''
        UPDATE USERS SET cash = cash + {money} WHERE id = {id}
        '''
        self.cur.execute(que_add)
        self.con.commit
    def __del__(self):
        self.con.close()

pool_1 = ('best_player1337','qwerty', 'test12345', 'xXxlox228xXx', '___xXxlox228xXx___')
pool_2 = tuple(range(0, 10000))
pool_3 = tuple(range(2003, 2022))
db = Users('market.sqlite')



for i in range(12):
    name_ins = choice(pool_1)
    USERS_ins = choice(pool_2)
    year_ins = choice(pool_3)
    db.insert(name_ins, USERS_ins, year_ins)
db.add_money(3, 50000)
data = db.get()
for line in data:
    print(line)