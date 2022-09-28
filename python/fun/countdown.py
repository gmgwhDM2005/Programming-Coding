#Customisable countdown
#With an in-built GUI!

import tkinter as tk
from tkinter import *
import time as t
x = Tk()

#Load the countdown
def start():
    f=open('count.txt','r')
    x=int(f.read())
    for i in range(x):
        print(x)
        t.sleep(1)
        x=x-1
    print('Press "Begin Countdown" to restart')
def edit():
    count=str(input('What new number would you like to countdown? '))
    f=open('count.txt','w')
    f.write(count)
#GUI
label = tk.Label(text="Welcome to the countdown ⏲", height=5, width=30)
b1 = Button(x, text="Begin countdown", command=lambda:[start()], height=2)
b2 = Button(x, text="Edit countdown", command=lambda:[edit()], height=2)
label.pack()
[b1.pack(), b2.pack()]
