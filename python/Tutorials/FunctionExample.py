#Firstly a function is created by the name of "myFunc"
def myFunc():
  #Code is then inputted inline with this function
  print('Function Called')

#Then call the function, if it is not called, the function will NOT run
myFunc()

#IMPORTANT NOTE: a FUNCTION must always be ABOVE the calling of itself
#if you call a function above the defined function, it will throw a syntax error and say it is undefined

#Another example of a function but with data being transfered to and from
#Import the random module
import random as r

#Create and define the function below as "Dice"
def Dice():
  #Create num as the random integer
  num=r.randint(1,6)
  #We then return the number that was called
  return num

#Next set "Dice" as "num" but "num" can be whatever you want it to be named as
num=Dice()
#Then the result is outputted onto the shell
print(num)
