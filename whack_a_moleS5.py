import time
from tkinter import Canvas, PhotoImage, Tk, mainloop
from random import choice, randint
from time import sleep, time
from tkinter.constants import HIDDEN, NORMAL

def whack(event):
    global points, end, whacked, show_sec

    x_mole, y_mole = c.coords(mole)
    if abs(x_mole - event.x) <= 25 and abs(y_mole - event.y) <= 25:
        if not whacked and state == 1:
            points += 1
            whacked = True
            if points % 3 == 0:
                end += 10
                show_sec *= 0.8
        c.itemconfig(mole, image=photo_whacked)
        c.update()

def show():
    global whacked
    whacked = False
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

points = 0
whacked = False
show_sec = 1
end = time() + 30
timer = c.create_text(200, 20, text = end - time(), font = ('Consolas', 20))
score = c.create_text(300, 20, text = points, font = ('Consolas', 20))

c.bind_all("<Button-1>", whack)

state = 0
show_time = time() + randint(1, 20) / 10 + 1
hide_time = None
while(running):
    if state == 0 and show_time < time():
        show()
        hide_time = time() + show_sec
        state = 1
    if state == 1 and hide_time < time():
        c.itemconfig(mole, state = HIDDEN)
        show_time = time() + randint(1, 20) / 10 + 1
        state = 0
    c.itemconfig(timer, text = f'{end - time():0.2f}')
    c.itemconfig(score, text = f'{points}')
    running = end > time()
    c.update()
    sleep(0.02)    

mainloop()




    