#A simple GUI game based off the TV-Show "Golden Balls"
#Simply paste the code into the Python IDE/Shell and run the program
#I hope to add a round three and a Mulitplayer-Friendly game too! (2 Players)
#I also hope to add text file integration with game logging and scores!

import tkinter as tk, random as r, time as t
from tkinter import *
CompMoney,UserMoney=0,0
def randNum():
     num=r.randint(1,2)
     return num
def r1Num():
     num=r.randint(1,10)
     return num
def firstround():
     def game1():
          global CompMoney, UserMoney
          CUpoints, Ppoints=0, 0
          guessNum=r1Num()
          while True:
               if CUpoints == 3 or Ppoints == 3:
                    if CUpoints == 3 and Ppoints == 3:
                         CompMoney=500
                         Ppoints=500
                         print(f'Computer Balance: {CompMoney}\nUsers Balance: {UserMoney}')
                    if CUpoints == 3:
                         CompMoney=500
                         print(f'Computer Balance: {CompMoney}\nUsers Balance: {UserMoney}')
                    elif Ppoints == 3:
                         UserMoney=500
                         print(f'Computer Balance: {CompMoney}\nUsers Balance: {UserMoney}')
                    break
               else:
                    newNum=r1Num()
                    print('Your Turn!')
                    print(f'Number: {guessNum}')
                    guess=input('Higher (H) or Lower (L)? ')
                    if ((guess.lower()=='h' or guess.lower()=='higher') and guessNum < newNum) or guessNum==newNum:
                         print('Correct, +1 point')
                         Ppoints=Ppoints+1
                    elif (guess.lower()=='l' or guess.lower()=='lower') and guessNum > newNum:
                         print('Correct, +1 point')
                         Ppoints=Ppoints+1
                    else:
                         print('Oof! You guessed incorrectly')
                    print(f'Next Card Value: {newNum}')
                    newNum=r1Num()
                    t.sleep(2)
                    print('\nComputer\'s Turn!')
                    print(f'Number: {newNum}')
                    guess=randNum()
                    if guess==1:
                         guess="Higher"
                    elif guess==2:
                         guess="Lower"
                    print(f'<Computer> {guess}')
                    t.sleep(2)
                    if ((guess.lower()=='h' or guess.lower()=='higher') and guessNum<newNum) or guessNum==newNum:
                         print('Correct, +1 point')
                         CUpoints=CUpoints+1
                    elif (guess.lower()=='l' or guess.lower()=='lower') and guessNum>newNum:
                         print('Correct, +1 point')
                         CUpoints=CUpoints+1
                    else:
                         print('Oof! You guessed incorrectly')
                    t.sleep(2)
                    print(f'Next Card Value: {newNum}')
                    print(f'\n------====+=+=+====------\nScore: {Ppoints}-{CUpoints} (User-Computer)\n------====+=+=+====------\n')            
     firstinst=Tk()
     label=Label(firstinst, text='\n'.join(['Welcome to the First Round',
        'You and the computer will play for up to 3 points',
        '1st one to 3 points wins!',
        'How to play:',
        'You will guess whether a number is higher or lower from the previous number (1-10)',
        'Both players will be able to see each others scores',
        'This game is worth: £500',
        'Good luck!']),font=("Comic Sans MS", 20))
     b1=Button(firstinst,text='Continue',command=lambda:[firstinst.destroy(),game1()],height=4,width=20,bg='maroon',fg='white')      
     [label.pack(),b1.pack()]
     firstinst.mainloop()
def secondround():
     def game2():
          def d():
               global UserMoney
               oldBalance=UserMoney
               UserMoney=UserMoney*2
               newBalance=UserMoney
               print(f'Double!\nOld Balance: {oldBalance}\nNew Balance: {newBalance}')
               game2()
               t.sleep(2)
          def n():
               global UserMoney
               UserMoney=0
               print('Big fail!\nBalance: 0')
               t.sleep(2)
          def m():
               num=randNum()
               if num==1:
                    d()
               elif num==2:
                    n()
          DoN=Tk()
          DoN.geometry('3000x2000')#WxH
          label=Label(DoN, text=f'Double or Nothing',font=("Calibri", 40))
          double=Button(DoN,text='Double',fg="black",bg="silver",width=30,height=10,command=lambda:[DoN.destroy(),m()],font=("Calibri",40)).place(x=550,y=80)
          finish=Button(DoN,text='Finish',fg="white",bg="red",width=20,height=1,command=lambda:DoN.destroy(),font=("Calibri",40)).place(x=700,y=800)
          label.pack()         
          DoN.mainloop()
     secondinst=Tk()
     label=Label(secondinst, text='\n'.join(['Welcome to the Second Round',
        'Double or Nothing',
        'You will be given an option to Double or Finish'
        'If you double, there is a 50% of Double.',
        '50% of Getting Nothing (Your Money is set to 0)',
        'This is game of chance, skill and luck',   
        'Sooo... Good luck!']),font=("Comic Sans MS", 20))
     b1=Button(secondinst,text='Continue',command=lambda:[secondinst.destroy(),game2()],height=4,width=20,bg='maroon',fg='white')      
     [label.pack(),b1.pack()]
     secondinst.mainloop()
def help1():
    helpPage=Tk()
    helpPage.geometry('1050x300')
    label=Label(helpPage,text='\n'.join(['Welcome to Golden Balls',
        'This game is based from the TV SHow "Golden Balls"',
        'You can only select to go against a computer for now',
        'Instructions for each round will be provided',
        'Good luck!']),font=("Comic Sans MS", 20))
    b1=Button(helpPage,text='Continue',command=lambda:[helpPage.destroy()],height=4,width=20,bg='maroon',fg='white')      
    [label.pack(),b1.pack()]
#GUI Main Menu
#Contains: Begin, Help
def mainmenu():
    tk=Tk()
    tk.geometry('600x800')#WxH
    label=Label(text='Main Menu',fg='PeachPuff4',font=("Calibri", 27))
    b1=Button(text='Begin',command=lambda:[tk.destroy()],height=15,width=50,fg='black',bg='PeachPuff2',font=("Calibri", 15))
    b2=Button(text='Help',command=lambda:[help1(),tk.destroy()],height=15,width=50,fg='black',bg='PeachPuff2',font=("Calibri", 15))
    [label.pack(),b1.pack(),b2.pack()]
    tk.mainloop()

def finalinst():
    def sporst(res,final):
          global CompMoney, UserMoney 
          final.destroy()
          if res=="split":
               print("You want to split the money")
               playerresult="Split"
          elif res=="steal":
               print("You want to steal the money")
               playerresult="Steal"
          t.sleep(1)
          compresult=randNum()
          if compresult==1:
               compresult="Split"
          elif compresult==2:
               compresult="Steal"
          print('The computer has chosen whether they want to Split or Steal')
          TotalMoney=CompMoney+UserMoney
          if compresult=="Steal" and playerresult=="Steal":
               t.sleep(2)
               print("Please both show your balls")
               t.sleep(2)
               print('You both have selected Steal')
               t.sleep(2)
               print("Both of you walk away with nothing")
               CompMoney,UserMoney=0,0
               t.sleep(2)
               print(f'Computer Balance: {CompMoney}\nUsers Balance: {UserMoney}')
               t.sleep(2)
               print('Thanks for playing!')
          elif compresult=="Steal" and playerresult=="Split":
               t.sleep(2)
               print("Please both show your balls")
               t.sleep(2)
               print('You have Splitten, but the Computer has Stolen')
               t.sleep(2)
               print("The computer walks away with ALL the money")
               CompMoney,UserMoney=TotalMoney,0
               t.sleep(2)
               print(f'Computer Balance: {CompMoney}\nUsers Balance: {UserMoney}')
               t.sleep(2)
               print('Thanks for playing!')
          elif playerresult=="Steal" and compresult=="Split":
               t.sleep(2)
               print("Please both show your balls")
               t.sleep(2)
               print('You have Stolen, but the Computer has Splitten')
               t.sleep(2)
               print("You walk away with ALL the money")
               CompMoney,UserMoney=0,TotalMoney
               t.sleep(2)
               print(f'Computer Balance: {CompMoney}\nUsers Balance: {UserMoney}')
               t.sleep(2)
               print('Thanks for playing!')
          elif compresult=="Split" and playerresult=="Split":
               t.sleep(2)
               print("Please both show your balls")
               t.sleep(2)
               print('You both have selected Split')
               t.sleep(2)
               print("Both of you walk away with half the money")
               CompMoney,UserMoney=TotalMoney/2,TotalMoney/2
               t.sleep(2)
               print(f'Computer Balance: {CompMoney}\nUsers Balance: {UserMoney}')
               t.sleep(2)
               print('Thanks for playing!')
               t.sleep(2)
    def finale():
         global CompMoney, UserMoney 
         CashPrize=CompMoney+UserMoney
         final=Tk()
         final.geometry('3000x2000')#WxH
         label=Label(final, text=f'Split or Steal (£{CashPrize})',font=("Calibri", 40))
         split=Button(final,text='Split',fg="white",bg="gold",width=30,height=10,command=lambda res="split":sporst(res,final),font=("Calibri",40)).place(x=100,y=80)
         steal=Button(final,text='Steal',fg="white",bg="red",width=30,height=10,command=lambda res="steal":sporst(res,final),font=("Calibri",40)).place(x=1000,y=80)
         label.pack()
    inst=Tk()
    inst.geometry('1050x300')
    label=Label(inst,text='\n'.join(['Welcome to the final round',
        'You and the computer will chose to either Split or Steal the money',
        'If you both pick SPLIT, the money will go to both of you in half the amount',
        'If either one of you pick STEAL, you will go away with ALL the money, leaving your opponent with nothing',
        'If you both STEAL, you both go away with nothing']),font=("Comic Sans MS", 20))
    b1=Button(inst,text='Continue',command=lambda:[inst.destroy(),finale()],height=4,width=20,bg='maroon',fg='white')      
    [label.pack(),b1.pack()]
    inst.mainloop()
mainmenu()
firstround()
secondround()
finalinst()


