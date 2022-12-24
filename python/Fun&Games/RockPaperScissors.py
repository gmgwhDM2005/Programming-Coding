import random as r,time as t
#Settings
game,rps,loop='Rock Paper Scissors',['1-Rock','2-Paper','3-Scissors'],True
def random():
     num=r.randint(1, 3)
     return num
def menu(opt):
     if opt=='A' or opt=='a':
          output={print('Starting Game....'),t.sleep(2),print('Please wait while we boot up!')}
          return output
     elif opt=='B' or opt=='b':
          output={print('Instructions on how to play:'),t.sleep(2),print('The aim of the game is to win all 3 rounds'),t.sleep(3),print('The user goes 1st with choosing either: Rock, Paper or Scissors'),t.sleep(3),print('The computer then replies with: Rock, Paper or Scissors'),t.sleep(3),print('U=User, C=Computer'),t.sleep(2),print('U=Rock, C=Paper, Paper Wins'),print('U=Rock, C=Scissors, Rock Wins'),print('U=Paper, C=Scissors, Scissors Wins'),print('If U = C, Tie no one wins\n '),t.sleep(5)}
          return output
     else:
          return print('Not a valid option')
#Main Menu
while loop==True:
     print('Welcome to the',game,'game')
     print('Starter Menu')
     t.sleep(1)          
     opt=str(input('A) Start Game\nB) How to play?\n'))
     menu(opt)
     if opt=='A' or opt=='a':break
rd,compScore,userScore=1,0,0
#Round Loop
for i in range(3):
     t.sleep(5)
     print('\nRound:', rd)
     t.sleep(1)
     while True:
          game=input(', '.join(rps) + '\nUser: ')
          try:
               int(game)
               break
          except: print('The option is not valid')        
     num,game=random(),int(game)
     #Computer Results
     if num==1:print('Computer: ' + rps[0])
     elif num==2:print('Computer: ' + rps[1])
     else:print('Computer: ' + rps[2])
     t.sleep(1)
     #Game and Num Comparing
     if num==game:print('Tie! No one gets the point!')
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
     rd=rd+1
#Results     
{print('Results'),t.sleep(2),print('User: ' + str(userScore)),t.sleep(2),print('Computer: ' + str(compScore))}
#File
f=open('scores.txt','a')
f.write('\n\nGame\nUser: ' + str(userScore) + '\nComputer' + str(compScore))
f.close()
