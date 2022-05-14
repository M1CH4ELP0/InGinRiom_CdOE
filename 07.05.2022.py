import sqlite3
from random import choice
class Users:

    def __init__(self,file):
        self.con = sqlite3.connect(file)
        self.cur = self.con.cursor()
        self.create_table('users')

    def create_table(self,table_name):
        que_create = '''CREATE TABLE IF NOT EXISTS {} (
          id INTEGER PRIMARY KEY,
          name TEXT,
          cash INTEGER,
          year INTEGER
        )'''.format(table_name)
        self.cur.execute(que_create)
        self.con.commit()

    def add_money(self , id , money):
        que_create = f''' UPDATE users SET cash = cash + {money} WHERE id = {id} '''

        self.cur.execute(que_create)
        self.con.commit()

    def get(self, que = 'SELECT * FROM users'):
        return self.cur.execute(que).fetchall()

    def get_old_users(self, que = 'SELECT * FROM users Order By year limit 3 '):
        return self.cur.execute(que).fetchall()

    def delete_user(self,name):
        que_insert = f'''
           DELETE FROM users WHERE name = '{name}'
        '''
        self.cur.execute(que_insert)
        self.con.commit()

    def insert(self,name,cash,year):
        que_insert = f'''
        INSERT INTO users (name, cash, year)
        VALUES ('{name}',{cash},{year})
        '''
        self.cur.execute(que_insert)
        self.con.commit()

    def __del__(self):
        '''

        :return:
        '''
        self.con.close()

class Skin:
    def __init__(self, file):
        self.con = sqlite3.connect(file)
        self.cur = self.con.cursor()
        self.create_table('skin')
    def create_table(self, table_name):
        que_create = '''CREATE TABLE IF NOT EXISTS {} (
             id INTEGER PRIMARY KEY,
             name TEXT,
             quality INTEGER,
             price FLOAT,
             rarity TEXT,
             stattrack BOOLEAN
           )'''.format(table_name)
        self.cur.execute(que_create)
        self.con.commit()
    def insert(self,name,quality,price,rarity,stattrack):
        que_insert = f'''
        INSERT INTO skin (name,quality,price,rarity,stattrack)
        VALUES ('{name}',{quality},{price},'{rarity}',{stattrack})
        '''
        self.cur.execute(que_insert)
        self.con.commit()
    def get(self, que = 'SELECT * FROM skin'):
        return self.cur.execute(que).fetchall()
    def get_some_rarity(self,rarity):
        que = f''' SELECT * FROM skin WHERE rarity = ('{rarity}') '''
        return self.cur.execute(que).fetchall()
    def get_some_stattrack(self,stattrack):
        que = f''' SELECT * FROM skin WHERE ststtrack = {stattrack} '''
        return self.cur.execute(que).fetchall()
    def delete_skin(self, name ,id):
        que_insert = f'''
           DELETE FROM skin WHERE name = '{name}' and id= {id}
        '''
        self.cur.execute(que_insert)
        self.con.commit()
    def __del__(self):
        '''

        :return:
        '''
        self.con.close()
class Inventory:
    def __init__(self, file):
        self.con = sqlite3.connect(file)
        self.cur = self.con.cursor()
        self.create_table('inventory')
    def create_table(self, table_name):
        que_create = '''CREATE TABLE IF NOT EXISTS {} (
                     id INTEGER PRIMARY KEY,
                     UserId FOREIGH KEY,
                     SkinId FOREIGH KEY
                   )'''.format(table_name)
        self.cur.execute(que_create)
        self.con.commit()
    def get(self, que = 'SELECT * FROM inventory'):
        return self.cur.execute(que).fetchall()
    def Insert(self, UserId, SkinId):
        que_insert = f'''
                INSERT INTO inventory (UserId, SkinId)
                VALUES ({UserId}, {SkinId})
                '''
        self.cur.execute(que_insert)
        self.con.commit()
    def __del__(self):
        '''
        :return:
        '''
        self.con.close()
    def get_inf(self):
        que = '''SELECT
                Inventory.Id AS id,
                users.name AS User_name,
                skin.name AS Skin_name
                FROM Inventory
                LEFT JOIN users
                ON users.id = UserId
                LEFT JOIN skin
                ON skin.id = SkinId;
                '''
        return self.cur.execute(que).fetchall()
data_base = Users('market.sqlite')
#data_base.delete_user()
#data_base.insert('term1x' , 7629 , 15)
#data_base.insert('m1hag' , 2450 , 12)
#data_base.insert('adamrus' , 4100 , 8)
#data_base.insert('hayastan' , 10000 , 17)
#data_base.insert('govnar' , 1000 , 2)
pool_name = ('term1x','m1hag','adamrus','hayastan','govnar')
pool_cash =(7000,4456,4068,54594,2353)
pool_year = (50,3,24,23,5)
data_base.add_money(5,15000)

'''for i in range(5):
   name_insert = choice(pool_name)
   cash_insert = choice(pool_cash)
   year_insert = choice(pool_year)
   data_base.insert(name_insert,cash_insert,year_insert)'''

data_inv = Inventory('market.sqlite')
data_skin = Skin('market.sqlite')
'''data_skin.insert('M4A1-S | Добро пожаловать в джунгли' , 5 , 105000 , 'Тайное' , False)
data_skin.insert('★ Тычковые ножи | Ультрафиолет' , 3 , 7500 , 'Тайное' , False)
data_skin.insert('AK-47 | Panthera onca' , 4 , 22960 , 'Засекреченное' , False)
data_skin.insert('Glock-18 | Синяя трещина' , 5 , 4000 , 'Армейское' , True)
data_skin.insert('★ Нож с лезвием-крюком | Волны' , 5 , 9800 , 'Тайное' , False)
data_skin.insert('AWP | История о драконе' , 5 , 954000 , 'Тайное' , False)
data_inv.Insert(1, 1)
data_inv.Insert(2, 5)
data_inv.Insert(3, 6)
data_inv.Insert(4, 4)'''


data = data_inv.get_inf()
for line in data:
    print(line)
