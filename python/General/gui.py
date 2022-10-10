import tkinter as tk
from tkinter import *
#This creates the GUI
gui = Tk()
#The label is the title text of the GUI
#The word "gui" on each line is to signify the name of the GUI to attach each feature to
label=Label(gui, text='Hello, This is a custom GUI!')
#Button, the colours and size are optional
b1=Button(gui, text='Close',command=lambda:[gui.destroy()],height=5,width=15,bg='Grey',fg='White')
#This packs the title and button to the GUI
[label.pack(),b1.pack()]

#You can have as many buttons as you like!
#Unlimited GUI's aswell
#Just make sure each variable is different, for example:
"""
gui=Tk()
gui1=Tk()
people=Tk()
Help=Tk()
"""
