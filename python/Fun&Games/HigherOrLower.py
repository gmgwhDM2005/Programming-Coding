#Higher, Lower, Equal
import random as r
import time as t
#Settings
game='Higher or Lower'

def random():
     num=r.randint(1, 50)
     return num

def menu(opt):
     if opt=='A' or opt=='a':
          output={
               print('Starting Game....'),
               t.sleep(2),
               print('Please wait while we boot up!'),
               t.sleep(5)
            }
          return output
     elif opt=='B' or opt=='b':
          output={
               print('Instructions on how to play:'),
               t.sleep(2),
               print('Computer will randomly generate a number between 1-50'),
               t.sleep(2),
               print('You will have to guess whether the next random number is higher or lower'),
               t.sleep(2),
               print('If you guess correctly, you get the point'),
               t.sleep(2),
               print('If you guess incorrectly, computer gets the point'),
               t.sleep(2),
               print('10 Rounds, player with highest score wins'),
               t.sleep(3)
            }
          return output
     else:
          return print('Not a valid option')

#Main Menu
while True:
     print('Welcome to the',game,'game')
     print('Starter Menu')
     print('higher or lower MUST be in lowercase')
     t.sleep(1)          
     opt=str(input('A) Start Game\nB) How to play?\n'))
     menu(opt)
     if opt=='A' or opt=='a':
        break

rd=1
userScore=0
compScore=0
for i in range (10):
    while True:
        randNum=random()
        randNum1=random()
        if randNum!=randNum1:
            break
    print('\nRound: ' + str(rd))
    print('Computer has generated a number')
    print('This number is ' + str(randNum))
    hol=str(input('Higher or Lower?'))
    
    if hol=='higher' and randNum1>randNum:
        print('Well done!\nThe number next is: ' + str(randNum1))
        userScore=userScore+1
    elif hol=='lower' and randNum1<randNum:
        print('Well done!\nThe next number is: ' + str(randNum1))
        userScore=userScore+1
    else:
        print('You guessed wrong, try again next round. The next number was ' + str(randNum1))
        compScore=compScore+1
    rd=rd+1

#Results
print('\nResults')
print('User - ' + str(userScore))
print('Computer - ' + str(compScore))

if userScore==compScore:
    print('Tie! Both players win!')
elif userScore<compScore:
    print('Computer wins! Better luck next time')
elif userScore>compScore:
    print('User wins! lets play again')
