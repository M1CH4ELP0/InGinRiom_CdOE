import tkinter
import random
from tkinter import PhotoImage

def prep():
    global player

    canvas.delete('all')
    player_pos = (random.randint(1, N_X - 1)*step,
                    random.randint(1,N_Y -1)*step)
    player= canvas.create_image(
        (player_pos[0], player_pos[1]), image=player_pic, anchor='nw')
    label.config(text='ESCAPE!')
    master.bind('<KeyPress>', key_pressed)

def move_wrap(obj, move_x, move_y):
    xy = canvas.coords(obj)
    canvas.move(obj, move_x, move_y)
    print(xy)
    if xy[0] <= 0:
        canvas.move(obj, WIDTH, 0)
    if xy[0] >= WIDTH:
        canvas.move(obj, -WIDTH, 0)
    if xy[1] <= 0:
        canvas.move(obj, 0, HEIGHT)
    if xy[1] >=HEIGHT:
        canvas.move(obj, 0, -HEIGHT)
    
def key_pressed(event):
    if event.keysym == 'Up':
        move_wrap(player, 0, -step)
    elif event.keysym == 'Down':
        move_wrap(player, 0, step)
    elif event.keysym == 'Right':
        move_wrap(player, step, 0)
    elif event.keysym == 'Left':
        move_wrap(player, -step, 0)

master = tkinter.Tk()

step = 32
N_X = 10
N_Y = 10
WIDTH = step * N_X
HEIGHT = step * N_Y
a = False
player_pic = tkinter.PhotoImage(file=r'.\pixil-frame-0.png')

canvas= tkinter.Canvas(master, bg = '#d5f05f',
                        width=WIDTH, height=HEIGHT)

player_pos = (random.randint(0,N_X - 1)* step,
                random.randint(0,N_Y -1)*step)
print(player_pos)
label= tkinter.Label(master, text= 'ЫЫЫЫЫЫ!')
restart= tkinter.Button(master, text = 'Restart',
                            command= prep)
restart.pack()
label.pack()
canvas.pack()
prep()
master.bind('<KeyPress>', key_pressed)
master.mainloop()