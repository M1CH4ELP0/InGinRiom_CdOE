import tkinter as tk

win = tk.Tk()
canvas = tk.Canvas(win, bg='white', width = 400, height = 400)
for i in range(0, 400, 50):
    line_gor = canvas.create_line((50 + i, 0), (50 + i, 400))
for i in range(0, 400, 50):
    line_ver = canvas.create_line((0, 50 + i), (400, 50 + i))
for i in range(0, 400, 100):
    oval = canvas.create_oval((0+i, 0), (50+i,50), fill="#EE82EE" )
    oval = canvas.create_oval((50+i, 50), (100+i,100), fill="#EE82EE" )
    oval = canvas.create_oval((0+i, 100), (50+i,150), fill="#EE82EE" )
for i in range(0, 400, 100):
    oval = canvas.create_oval((0+i, 250), (50+i,300), fill="#66f58a" )
    oval = canvas.create_oval((50+i, 300), (100+i,350), fill="#66f58a" )
    oval = canvas.create_oval((0+i, 350), (50+i,400), fill="#66f58a" )
canvas.pack()
win.mainloop()