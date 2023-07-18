import tkinter as tk
import random
import requests

gui = tk.Tk()
gui.geometry('1920x1080')
count = 0
taken = []
reqWeb = 'https://dsstlevel.github.io/callouts.json'

class main():
    def genNum():
        while True:
            randNum = random.randint(1,90)
            if not (randNum in taken):
                return randNum
    
    def pressed():
        num = main.genNum()
        taken.append(num)
        for i in gui.winfo_children():
            if isinstance(i, tk.Label):
                if i["text"]==num:
                    i['bg']='blue'
                    i['fg']='white'
                    display['text']=num
                    othervals['text']=main.get_otherVals(num)
    def get_otherVals(num):
        req = requests.get(reqWeb).json()
        for i in req:
            i:dict
            for key, value in i.items():
                if str(key)==str(num):
                    value:str
                    value.replace('/','\n')
                    print(value)
                    return value

for i in range(0,10):
    for g in range(0,9):
        count += 1
        tk.Label(gui,text=count,font=('Comic Sans MS', 40)).place(x=g*100,y=i*100)

button = tk.Button(gui,text='Spin',font=('Comic Sans MS', 40), height=2, width=11, bg="grey",command=lambda:main.pressed())
button.place(x=900,y=20)

display = tk.Label(gui,text='',font=('Comic Sans MS', 80), height=1, width=8, bg="grey", fg='white')
display.place(x=1200,y=20)

othervals = tk.Label(gui,text='',font=('Comic Sans MS', 50), height=3, width=23, bg="grey", fg='white')
othervals.place(x=900,y=140)

gui.mainloop()

