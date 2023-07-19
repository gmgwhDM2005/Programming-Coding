import requests 
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
global url, count
url='https://queue-times.com/parks/1/queue_times.json'
count=1

def refresh(url):
    scrltxt.delete('1.0',tk.END)
    req:dict=requests.get(url).json()
    try:
        data:list = req['lands']
    except:
        return scrltxt.insert(tk.END,'No Data')
    array = []
    for i in data:
        i:dict
        for k1, v1 in i.items():
            if k1=='rides':
                v1:list
                for j in v1:
                    j:dict
                    array.append(f"Name: {j['name']}\nWait Time: {j['wait_time']}\nOpen?: {j['is_open']}")
    scrltxt.insert(tk.END,'\n'.join(array))

def NextPark():
    global count
    count+=1
    if count==71:
        count=1
    global url
    url=f'https://queue-times.com/parks/{count}/queue_times.json'
    refresh(url)

gui = tk.Tk()
gui.geometry('900x1080')

scrltxt = ScrolledText(gui,font=('Comic Sans MS',20))
scrltxt.pack()
refresh(url)

tk.Button(gui, text='Refresh', font=('Comic Sans MS', 30), command=lambda:refresh(url)).pack()
tk.Button(gui,text='Next Park', font=('Comic Sans MS', 30), command=lambda:NextPark()).pack()

gui.mainloop()
