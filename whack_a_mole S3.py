import time
from tkinter import Canvas, PhotoImage, Tk, mainloop
from random import choice, randint
from time import sleep, time
from tkinter.constants import HIDDEN, NORMAL

def whack(event):
    x_mole, y_mole = c.coords(mole)
    if abs(x_mole - event.x) <= 25 and abs(y_mole - event.y) <= 25:
        c.itemconfig(mole, image=photo_whacked)
        c.update()

def show():
    c.coords(mole, choice(places))
    c.itemconfig(mole, image = photo_mole)
    c.itemconfig(mole, state = NORMAL)
places = [
    [120, 50],
    [245, 50],
    [370, 50],
    [85, 105],
    [190, 95],
    [300, 95],
    [405, 95],
    [110, 170],
    [245, 170],
    [385, 170]
]
running = True

tk = Tk()
c = Canvas(tk, width=500, height=250)
c.pack()
photo_bg = PhotoImage(file="back.png")
c.create_image(0, 0, image=photo_bg, anchor='nw')
photo_mole = PhotoImage(file="mol1.png")
photo_whacked = PhotoImage(file="mol2.png")
mole = c.create_image(0, 0, image=photo_mole) 
c.itemconfig(mole, state = HIDDEN)

c.bind_all("<Button-1>", whack)

state = 0
show_time = time() + randint(1, 20) / 10 + 1
hide_time = None
while(running):
    if state == 0 and show_time < time():
        show()
        hide_time = time() + 1
        state = 1
    if state == 1 and hide_time < time():
        c.itemconfig(mole, state = HIDDEN)
        show_time = time() + randint(1, 20) / 10 + 1
        state = 0
    c.update()
    sleep(0.02)    

mainloop()