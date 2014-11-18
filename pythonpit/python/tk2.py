#!/usr/bin/env python
from Tkinter import *

window = Tk()
window.title('GUI Tkinter 1')
window.geometry("300x250") # w x h
window.resizable(0,0)

#define labels
box1 = Label(window,text="Entry 1:")

#place the label in the window object
box1.grid(row = 1, column = 1, padx = 5, pady = 5)

window.mainloop()
