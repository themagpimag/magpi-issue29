#!/usr/bin/env python
from Tkinter import *

window = Tk()
window.title('GUI Tkinter 1')
window.geometry("300x250") # w x h
window.resizable(0,0)

def btn1():
  print ("button pressed")

btn_tog2 = Button(window, text = "button1", command = btn1)
btn_exit = Button(window, text = "exit", command = exit)

btn_tog2.grid(row = 1, column = 2, padx = 5, pady = 5)
btn_exit.grid(row = 2, column = 2, padx = 5, pady = 5)

#define labels
button1 = Label(window, text="click button")
button2 = Label(window, text="exit program")

button1.grid(row = 1, column = 1, padx = 5, pady = 5)
button2.grid(row = 2, column = 1, padx = 5, pady = 5)

window.mainloop()
