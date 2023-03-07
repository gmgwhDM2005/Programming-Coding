from tkinter import *
import smtplib

def send_message(server,sender_email):
    address_info=address.get()
    email_body_info=email_body.get()
    server.sendmail(sender_email,address_info,email_body_info)
    print('Message Sent')
    address_entry.delete(0,END)
    email_body_entry.delete(0,END)

def login():
    while True:
        gui1=Tk()
        Label(gui1,text='Email').pack()
        sender_email,password=StringVar(),StringVar()
        Entry(gui1,textvariable=sender_email).pack()
        Label(gui1,text='Password').pack()
        Entry(gui1,textvariable=password).pack()
        Button(gui1,text="Submit",bg="grey",command=lambda:gui1.destroy(),width="30",height=2).pack()
        gui1.mainloop()
        try:
            server=smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login(sender_email.get(),password.get())
            return server,sender_email.get()
        except smtplib.SMTPAuthenticationError as e:
            print('Invalid Email Address Or Password\nOften If your account uses 2-factor authentication (e.g. google), you may need to create an app password, under Security of your Google Account.')

server,sender_email=login()

gui=Tk()
gui.geometry("500x500")
gui.title("Email App")
Label(gui,text="Python Mail").pack()
address_field,email_body_field=Label(gui,text='Recipient Email: '),Label(gui,text="Message: ")
address,email_body=StringVar(),StringVar()
address_entry,email_body_entry=Entry(textvariable=address,width="30"),Entry(textvariable=email_body,width="30")
[address_entry.place(x=15,y=100),email_body_entry.place(x=15,y=180),address_field.place(x=15,y=70),email_body_field.place(x=15,y=140)]

button=Button(gui,text="Send",bg="grey",command=lambda:send_message(server,sender_email),width="30",height=2)
button.place(x=15,y=220)
gui.mainloop()
