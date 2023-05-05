import os, platform, psutil, tkinter as tk
from tkinter import scrolledtext, ttk

"""
The psutil library may need to be installed
Follow something like this: "pip install psutil"


"""

class Conversions():
    def b_to_gb(b):
        kb=b/1000
        mb=kb/1000
        gb=round(mb/1000,2)
        return gb

class dashboard():
    class CPU:
        info=[
            f'CPU Runtime Percentage: {psutil.cpu_percent()}%',
            f'Number of Cores: {psutil.cpu_count()}cores',
            f'CPU Runtime Frequency: {psutil.cpu_freq()[0]}',
            f'CPU System-wide CPU Times: {psutil.cpu_times()[0]}'
        ]
    class DISK:
        def get_info():
            partitions=[]
            for disk in psutil.disk_partitions():
                use=[psutil.disk_usage(disk[0])[0],psutil.disk_usage(disk[0])[1],psutil.disk_usage(disk[0])[2],psutil.disk_usage(disk[0])[3]]
                partitions.append(f'---{disk[0]} Drive---\nFile System: {disk[2]}\nPermissions: {disk[3:]}\nTotal Cap: {Conversions.b_to_gb(use[0])}GB\nUsed: {Conversions.b_to_gb(use[1])}GB\nFree: {Conversions.b_to_gb(use[2])}\nPercentage Used: {use[3]}%')
            return partitions
        
    class Comp:
        info=[
            f'User Name: {os.getlogin()}',
            f'Desktop Battery: {psutil.sensors_battery()[0]}%',
            f'OS Version: {platform.platform()}',
            f'Windows Version: {platform.win32_edition()}',
            f'Node Name: {platform.node()}',
            f'OS: {platform.system()}'
        ]

    class Users:
        def info():
            array=[]
            for i in psutil.users():
                array.append(str(f'User: {i.name}\nHost: {i.host}\nID: {i.pid}\nStarted: {i.started}\nTerminal: {i.terminal}'))
            return list(array)
    def tasks():
        array=[]
        for i in psutil.process_iter():
            array.append(f'{i.name()} | CPU: {i.cpu_percent()} | Memory: {i.memory_percent()}')
        return list(set(array))
    
    def task_ref():
        array=[]
        x.config(state='normal')
        x.delete(1.0, tk.END)
        array=[]
        for i in psutil.process_iter():
            array.append(f'{i.name()} | CPU: {i.cpu_percent()} | Memory: {i.memory_percent()}')
        array=list(set(array))
        x.insert(tk.END, '\n'.join(array))
        x.config(state='disabled')


global x
dash = tk.Tk()
dash.title('Computer Data Dashboard')
notebook=ttk.Notebook(dash)
mainFrame=tk.Frame(notebook)
tk.Label(mainFrame,text='Desktop',font=('Comic Sans MS',25)).pack()
tk.Label(mainFrame,text='\n'.join(dashboard.Comp.info),font=("Comic Sans MS",15)).pack()
tk.Label(mainFrame,text='CPU',font=('Comic Sans MS',25)).pack()
tk.Label(mainFrame,text='\n'.join(dashboard.CPU.info),font=("Comic Sans MS",15)).pack()
tk.Label(mainFrame,text='Disk Drives',font=('Comic Sans MS',25)).pack()
tk.Label(mainFrame,text='\n'.join(dashboard.DISK.get_info()),font=("Comic Sans MS",15)).pack()
notebook.add(mainFrame,text='Dashboard')
taskFrame=tk.Frame(notebook)
tk.Button(taskFrame,text='Refresh',command=dashboard.task_ref).pack()
x=scrolledtext.ScrolledText(taskFrame)
x.insert(tk.END,'\n'.join(dashboard.tasks()))
x.pack()
x.config(state='disabled',font=("Arial",14))
notebook.add(taskFrame,text='Tasks')
usersFrame=tk.Frame(notebook)
p=scrolledtext.ScrolledText(usersFrame)
p.insert(tk.END, dashboard.Users.info())
p.config(state='disabled')
p.pack()
notebook.add(usersFrame,text='Users')
notebook.pack()
dash.mainloop()
