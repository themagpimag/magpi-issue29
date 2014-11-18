#!/usr/bin/env python

import random
from Tkinter import *

def response():
  response_phrase = random.choice(RESPONSES)
  #print response_phrase
  #clear prev output
  circletext2.delete(0, END)
  circletext2.insert(0, str(response_phrase))

window = Tk()
window.title('Magic 8')
window.geometry("300x100") # w x h
window.resizable(0,0)

RESPONSES = ["It is certain", "It is decidely so", "Without a doubt", "Yes, definitely", "You may rely on it", "As I see it yes", "Most likely", "Outlook good", "Yes", "Signs point to yes", "Reply hazy try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]

#define and place labels
box1 = Label(window, text="Q: ")
box2 = Label(window, text="Answer: ")

box1.grid(row = 1, column = 1, padx = 5, pady = 5)
box2.grid(row = 2, column = 1, padx = 5, pady = 5)

#define entry box
circleVar = StringVar()
circletext = Entry(window, textvariable=circleVar)

#define output box
circleVar2 = StringVar()
circletext2 = Entry(window, textvariable=circleVar2)

#display boxes
circletext.grid(row = 1, column = 2)
circletext2.grid(row = 2, column = 2)

response = Button(window, text='response', command=response)
exitbtn = Button(window, text='Exit', command=exit)

response.grid(row = 4, column = 1, padx = 1, pady = 1)
exitbtn.grid(row = 4, column = 2, padx = 1, pady = 1)

window.mainloop()
