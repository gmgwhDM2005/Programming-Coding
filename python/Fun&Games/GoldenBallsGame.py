#A simple GUI game based off the TV-Show "Golden Balls"
#Simply paste the code into the Python IDE/Shell and run the program
#Soon to come:
#Mulitplayer-Friendly game too! (2 Players)
#Text file integration with game logging and scores!

#This game consists of:
#-Main Menu
#-Higher or Lower
#-Double or Nothing
#-Rock Paper Scissors
#-Split or Steal

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
               t.sleep(2)
               game2()
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
          DoN.geometry('1500x1000')#WxH
          label=Label(DoN, text=f'Double or Nothing',font=("Calibri", 40))
          double=Button(DoN,text='Double',fg="black",bg="silver",width=30,height=10,command=lambda:[DoN.destroy(),m()],font=("Calibri",40))
          finish=Button(DoN,text='Finish',fg="white",bg="red",width=20,height=1,command=lambda:DoN.destroy(),font=("Calibri",40))
          [label.pack(), double.pack(),finish.pack()]        
          DoN.mainloop()
     print('Double or Nothing!')
     secondinst=Tk()
     label=Label(secondinst, text='\n'.join(['Welcome to the Second Round',
        'Double or Nothing',
        'You will be given an option to Double or Finish'
        'If you double, there is a 50% of Double.',
        '50% of Getting Nothing (Your Money is set to 0)',
        'This is game of chance, skill and luck',
        'Pressing "Finish" will end round 2'
        'Sooo... Good luck!']),font=("Comic Sans MS", 20))
     b1=Button(secondinst,text='Continue',command=lambda:[secondinst.destroy(),game2()],height=4,width=20,bg='maroon',fg='white')      
     [label.pack(),b1.pack()]
     secondinst.mainloop()
def thirdround():
     print('\nRock Paper Scissors')
     def game3():
            def rock():
                global rpsChoice
                rpsChoice=1
            def paper():
                global rpsChoice
                rpsChoice=2
            def scissors():
                global rpsChoice
                rpsChoice=3
            rps=Tk()
            rps.geometry('1000x2000')#WxH
            label=Label(rps, text=f'Rock Paper Scissors...',font=("Calibri", 40))
            r=Button(rps,text='Rock',fg="black",bg="silver",width=30,height=5,command=lambda:[rps.destroy(),rock()],font=("Calibri",40))
            p=Button(rps,text='Paper',fg="black",bg="white",width=30,height=5,command=lambda:[rps.destroy(),paper()],font=("Calibri",40))
            s=Button(rps,text='Scissors',fg="black",bg="grey",width=30,height=5,command=lambda:[rps.destroy(),scissors()],font=("Calibri",40))
            [label.pack(),r.pack(),p.pack(),s.pack()]         
            rps.mainloop()     
     def game1a():
         game3()
         global compScore, userScore
         userScore=0
         compScore=0
         def system():
                    print('U: = User, C: = Computer')
                    global rpsChoice, compScore, userScore
                    num=rpsChoice
                    game=r.randint(1,3)
                    t.sleep(1)
                    if num==1:
                        print(f'<User> Rock')
                    elif num==2:
                        print(f'<User> Paper')
                    elif num==3:
                        print(f'<User> Scissors')
                    if game==1:
                        print(f'<Computer> Rock')
                    elif game==2:
                        print(f'<Computer> Paper')
                    elif game==3:
                        print(f'<Computer> Scissors')
                    t.sleep(2)
                    if num==game:
                          print('Tie! No one gets the point!')
                    elif game==1 and num==2:
                          print('C:Paper Defeats U:Rock, Computer gets the point!')
                          compScore=compScore + 1
                    elif game==1 and num==3:
                          print('U:Rock Defeats C:Scissors, User gets the point!')
                          userScore=userScore + 1
                    elif game==2 and num==1:
                          print('U:Paper Defeats C:Rock, User gets the point!')
                          userScore=userScore + 1
                    elif game==2 and num==3:
                          print('C:Scissors Defeats U:Paper, Computer gets the point!')
                          compScore=compScore + 1
                    elif game==3 and num==1:
                          print('C:Rock Defeats U:Scissors, Computer gets the point!')
                          compScore=compScore + 1
                    elif game==3 and num==2:
                          print('U:Scissors Defeats C:Paper, User gets the point!')
                          userScore=userScore + 1
         system()
     t.sleep(2)
     thirdinst=Tk()
     label=Label(thirdinst, text='\n'.join(['Welcome to the Third Round',
            'A classical game of Rock Paper Scissors',
            '3 Buttons: Rock, Paper Scissors will be shown'
            'Select the option you wish to play the computer against',
            'The game is best to 3!',
            'Rules:',
            'Rock beats Scissors, Scissors beats Paper, Paper beats Rock',   
            'Let the game begin!']),font=("Comic Sans MS", 20))
     b1=Button(thirdinst,text='Continue',command=lambda:[thirdinst.destroy(),game1a()],height=4,width=20,bg='maroon',fg='white')      
     [label.pack(),b1.pack()]
     thirdinst.mainloop()
     global UserMoney, CompMoney, compScore, userScore
     for i in range(2):
            print(f'\nRound ')
            game1a()
            t.sleep(6)
     print(f'Score: {userScore}-{compScore} (User-Computer)')
     if userScore<compScore:
             CompMoney=CompMoney+750
             print('Computer Wins!')
             print(f'Computer Balance: {CompMoney}\nUsers Balance: {UserMoney}')
     elif userScore>compScore:
             UserMoney=UserMoney+750
             print('User Wins!')
             print(f'Computer Balance: {CompMoney}\nUsers Balance: {UserMoney}')
     elif userScore==compScore:
             print('No one gets the money as it ended up in a tie')
def help1():
    helpPage=Tk()
    helpPage.geometry('1050x300')
    label=Label(helpPage,text='\n'.join(['Welcome to Golden Balls',
        'This game is based from the TV SHow "Golden Balls"',
        'You can only select to go against a computer for now',
        'Instructions for each round will be provided',
        'This game is worth: £750',
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
    print('Finale - Split or Steal')
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
               CompMoney, UserMoney=0,0
               {t.sleep(2),print("Please both show your balls"),t.sleep(2),print('You both have selected Steal'),t.sleep(2),print("Both of you walk away with nothing"),t.sleep(2),print(f'Computer Balance: {CompMoney}\nUsers Balance: {UserMoney}'),t.sleep(2),print('Thanks for playing!')}
          elif compresult=="Steal" and playerresult=="Split":
               CompMoney,UserMoney=TotalMoney,0
               {t.sleep(2),print("Please both show your balls"),t.sleep(2),print('You have Splitten, but the Computer has Stolen'),t.sleep(2),print("The computer walks away with ALL the money"),t.sleep(2),print(f'Computer Balance: {CompMoney}\nUsers Balance: {UserMoney}'),t.sleep(2),print('Thanks for playing!')}
          elif playerresult=="Steal" and compresult=="Split":
               CompMoney,UserMoney=0,TotalMoney
               {t.sleep(2),print("Please both show your balls"),t.sleep(2),print('You have Stolen, but the Computer has Splitten'),t.sleep(2),print("You walk away with ALL the money"),t.sleep(2),print(f'Computer Balance: {CompMoney}\nUsers Balance: {UserMoney}'),t.sleep(2),print('Thanks for playing!')}
          elif compresult=="Split" and playerresult=="Split":
               CompMoney,UserMoney=TotalMoney/2,TotalMoney/2
               {t.sleep(2),print("Please both show your balls"),t.sleep(2),print('You both have selected Split'),t.sleep(2),print("Both of you walk away with half the money"),t.sleep(2),print(f'Computer Balance: {CompMoney}\nUsers Balance: {UserMoney}'),t.sleep(2),print('Thanks for playing!'),t.sleep(2)}
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
thirdround()
finalinst()
