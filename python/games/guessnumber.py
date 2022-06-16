import random as r
import time as t
#Settings
game='Guess The Number'

def random():
     num=r.randint(1, 100)
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
               print('Computer will randomly generate a number between 1-100'),
               t.sleep(2),
               print('You will have to guess the number'),
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
     t.sleep(1)          
     opt=str(input('A) Start Game\nB) How to play?\n'))
     menu(opt)
     if opt=='A' or opt=='a':
          break

rd=1
compScore=0
userScore=0
for i in range(10):
    print('\nRound: ' + str(rd))
    print('Computer is a generating number')
    t.sleep(1)
    while True:
        while True:
            guess=input('Input your guess:')
            try:
                int(guess)
                break
            except:
                print('Please input a valid integer, between 1-100')        
        guess=int(guess)
        if guess>100 or guess<1:
            print('Not in range of 1-100')
        else:
            break
    num=random()
    if num==guess:
        print('You have guessed correctly, The Computer\'s number is ' + str(num))
        userScore=userScore+1
    else:
        print('You have guess incorrectly!')
        print('The Computer\'s number is ' + str(num))
        compScore=compScore+1
    rd=rd+1
    t.sleep(3)

#Results
print('\n\nResults')
print('User - ' + str(userScore))
print('Computer - ' + str(compScore))

if userScore==compScore:
    print('Tie! Both players win!')
elif userScore<compScore:
    print('Computer wins! Better luck next time')
elif userScore>compScore:
    print('User wins! lets play again')
