import tkinter as tk
from tkinter import ttk
win = tk.Tk()
canvas = tk.Canvas(win, bg='white', width = 1920, height = 1080)
data = [(1, 'm1hag', 2353, 5), (2, 'hayastan', 4068, 24), (3, 'term1x', 54594, 24), (4, 'term1x', 4068, 50), (5, 'm1hag', 382000, 23)]
def fill_table(User_table, data):
    for i in range (len(data)):
        User_table.insert(parent='', index='end', iid = i, text ='', values=data[i])
win.geometry('1920x1080')
frame = tk.Frame(win)
User_table = ttk.Treeview(frame)
User_table['columns']= ('id','name', 'cash', 'year')
User_table.column('#0', width=0)
User_table.heading('id', text= 'id')
User_table.heading('name', text= 'name')
User_table.heading('cash', text= 'cash')
User_table.heading('year', text= 'year')
search_btn = tk.Button(text = 'search', width = 10, height = 2)
search_btn.config(command = fill_table(User_table, data))
search = ''
search_entry = tk.Entry(textvariable = search)
#fill_table(User_table, data)
search_entry.pack()
search_btn.pack()
User_table.pack()
frame.pack()
canvas.pack()
win.mainloop()