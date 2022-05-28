import tkinter as tk
from tkinter import ttk
import sqlite3
win = tk.Tk()
canvas = tk.Canvas(win, bg='white', width = 1920, height = 1080)
def fill_table(User_table, data):
    for i in range (len(data)):
        User_table.insert(parent='', index='end', iid = i, text ='', values=data[i])

def button_c_find(search, User_table, data):
    a = search.get
    print(a)
    fill_table(User_table, data)
win.geometry('1920x1080')



frame = tk.Frame(win)
User_table = ttk.Treeview(frame)
User_table['columns']= ('id','name', 'cash', 'year')
User_table.column('#0', width=0)
User_table.heading('id', text= 'id')
User_table.heading('name', text= 'name')
User_table.heading('cash', text= 'cash')
User_table.heading('year', text= 'year')
'''search_btn = tk.Button(text = 'search', width = 10, height = 2)
search = ''
search_entry = tk.Entry(textvariable = search)
search_entry.pack()
search_btn.config(command = button_c_find(search_entry, User_table, data))#fill_table(User_table, data))'''
User_table.pack()
'''def db_resp(req):
    con = sqlite3.connect('market.sqlite')
    cur = con.cursor
    return cur.execute(req).fetchall'''
def getEntry():
    data = [(1, 'm1hag', 2353, 5), (2, 'hayastan', 4068, 24), (3, 'term1x', 54594, 24), (4, 'term1x', 4068, 50),
            (5, 'm1hag', 382000, 23)]
    res = myEntry.get()
    #que = '''{}'''
    #data = (db_resp(que.format(res)))
    fill_table(User_table, data)
myEntry = tk.Entry(win, width= 40)
myEntry.pack(pady = 20)
btn = tk.Button(win, height = 1, width = 10, text = "Read", command = getEntry)
btn.pack()

many_screen = ttk.Notebook(win)
f1 = tk.Frame(many_screen)
f2 = tk.Frame(many_screen)
f3 = tk.Frame(many_screen)
many_screen.add(f1, text = 'Users')
many_screen.add(f2, text = 'Skins')
many_screen.add(f3, text = 'Inventory')
#fill_table(User_table, data)
#search_btn.pack()

frame.pack()
many_screen.pack()
canvas.pack()
win.mainloop()