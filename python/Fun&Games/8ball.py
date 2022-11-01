#8Ball
import random as r

while True:
    question=input('What would you like to ask the 8ball?\n')

    num1=r.randint(1,3)
    if num1==1:
        num2=r.randint(1,10)
        if num2==1:
            print('It is certain')
        elif num2==2:
            print('It is decidedly so')
        elif num2==3:
            print('Without a doubt')
        elif num2==4:
            print('Yes - Definitely')
        elif num2==5:
            print('You may rely on it')
        elif num2==6:
            print('As I see it, yes')
        elif num2==7:
            print('Most likely')
        elif num2==8:
            print('Outlook good')
        elif num2==9:
            print('Yes')
        elif num2==10:
            print('Signs point to yes')
    elif num1==2:
        num2=r.randint(1,5)
        if num2==1:
            print('Reply hazy, try again')
        elif num2==2:
            print('Ask again later')
        elif num2==3:
            print('Better not tell you now')
        elif num2==4:
            print('Cannot predict now')
        elif num2==5:
            print('Concentrate and ask again')
    elif num1==3:
        num2=r.randint(1,5)
        if num2==1:
            print('Don\'t count on it')
        elif num2==2:
            print('My reply is no')
        elif num2==3:
            print('My sources say no')
        elif num2==4:
            print('Outlook not so good')
        elif num2==5:
            print('Very doubtful')
