#!python3
from tkinter import *
from random import *
data = Tk()
root = Tk()

def setup():
    x = p1.get()
    y = p2.get()
    Label(root, text = x, fg = 'white', bg = 'blue', width = 10, font = ('Ariel', 20, '')).grid(row = 0, column = 0)
    Label(root, text = y, fg = 'white', bg = 'red', width = 10, font = ('Ariel', 20, '')).grid(row = 0, column = 2)


i = 0
pts1 = 0
pts2 = 0
def start():
    z = r.get()
    global i
    global pts1
    global pts2
    if i == z:
        if pts1 > pts2:
            Label(root, text = 'WINNER!', fg = 'white', bg = 'black', width = 10, font = ('Ariel', 20, '')).grid(row = i+1, column = 0)
        elif pts1 < pts2:
            Label(root, text = 'WINNER!', fg = 'white', bg = 'black', width = 10, font = ('Ariel', 20, '')).grid(row = i+1, column = 2)
        data.destroy()
    else:
        i = i+1
        things = ['stone', 'paper', 'scissor']
        v1 = str(choice(things))
        v2 = str(choice(things))
        Label(root, text = v1, fg = 'white', bg = 'green', width = 10, font = ('Ariel', 20, '')).grid(row = i, column = 0)
        Label(root, text = v2, fg = 'white', bg = 'green', width = 10, font = ('Ariel', 20, '')).grid(row = i, column = 2)
        if v1==v2:
            Label(root, text = str(pts1)+':'+str(pts2), fg = 'white', bg = 'black', width = 3, font = ('Ariel', 20, '')).grid(row = i, column = 1)
        elif v1 == 'stone':
            if v2 == 'scissor':
                pts1 = pts1+1
                Label(root, text = str(pts1)+':'+str(pts2), fg = 'white', bg = 'black', width = 3, font = ('Ariel', 20, '')).grid(row = i, column = 1)
            if v2 == 'paper':
                pts2 = pts2+1
                Label(root, text = str(pts1)+':'+str(pts2), fg = 'white', bg = 'black', width = 3, font = ('Ariel', 20, '')).grid(row = i, column = 1)
        elif v1 == 'paper':
            if v2 == 'stone':
                pts1 = pts1+1
                Label(root, text = str(pts1)+':'+str(pts2), fg = 'white', bg = 'black', width = 3, font = ('Ariel', 20, '')).grid(row = i, column = 1)
            if v2 == 'scissor':
                pts2 = pts2+1
                Label(root, text = str(pts1)+':'+str(pts2), fg = 'white', bg = 'black', width = 3, font = ('Ariel', 20, '')).grid(row = i, column = 1)
        elif v1 == 'scissor':
            if v2 == 'paper':
                pts1 = pts1+1
                Label(root, text = str(pts1)+':'+str(pts2), fg = 'white', bg = 'black', width = 3, font = ('Ariel', 20, '')).grid(row = i, column = 1)
            if v2 == 'stone':
                pts2 = pts2+1
                Label(root, text = str(pts1)+':'+str(pts2), fg = 'white', bg = 'black', width = 3, font = ('Ariel', 20, '')).grid(row = i, column = 1)
    print (i, pts1, pts2)


Label(data, text = 'Enter Data', bg = 'black', fg = 'white', font = ('Ariel', 20, '')).grid(row = 0, column = 1, sticky = 'W')
p1 = StringVar()
Label(data, text = 'Player-1:', font = ('Ariel', 15, '')).grid(row = 1, column = 0, sticky = 'E')
Entry(data, textvariable = p1, font = ('Ariel', 15, '')).grid(row = 1, column = 1)
p2 = StringVar()
Label(data, text = 'Player-2:', font = ('Ariel', 15, '')).grid(row = 2, column = 0, sticky = 'E')
Entry(data, textvariable = p2, font = ('Ariel', 15, '')).grid(row = 2, column = 1)
r = IntVar()
Label(data, text = 'Rounds:', font = ('Ariel', 15, '')).grid(row = 3, column = 0, sticky = 'E')
Entry(data, textvariable = r, font = ('Ariel', 15, '')).grid(row = 3, column = 1)
Button(data, text = 'GO!', fg = 'white', bg = 'black', font = ('Ariel', 15, ''), command = setup).grid(row = 4, column = 1, sticky = 'E')
Button(root, text = 'Start', fg = 'white', bg = 'black', width = 5, font = ('Ariel', 15, ''), command = start).grid(row = 0, column = 1)

data.title('Settings')
data.geometry('330x200+700+100')
root.title('Stone Paper Sicssor')
root.geometry('400x700+0+0')
root.mainloop()
data.mainloop()
