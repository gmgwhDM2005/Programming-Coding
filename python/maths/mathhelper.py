import math as m
import time as t
def calcop(num1, operation, num2):
     if operation=='+':
          ans=num1+num2
     elif operation=='-':
          ans=num1-num2
     elif operation=='/':
          ans=num1/num2
     elif operation=='*':
          ans=num1*num2
     return ans
def calc():
     num1=int(input('Number 1: '))
     num2=int(input('Number 2: '))
     operation=str(input('Operation: '))
     ans=calcop(num1, operation, num2)
     print(str(ans))
def circlearea():
     radius=int(input('Radius of the cirle: '))
     ans=m.ceil(m.pi*(radius*radius))
     return ans
def trianglearea():
     base=int(input('Base: '))
     height=int(input('Height: '))
     ans=0.5*(base*height)
     return ans
def rectanglearea():
     base=int(input('Base: '))
     height=int(input('Height: '))
     ans=(base*height)
     return ans
def trapeziumarea():
     base=int(input('Base: '))
     top=int(input('Top: '))
     height=int(input('Height: '))
     ans=((base+top)/2)*height
     return ans
def sqaureperimeter():
     length=int(input('Length: '))
     ans=length*4
     return ans
def rectangleperimeter():
     length=int(input('Length: '))
     width=int(input('Width: '))
     ans=(length*2)+(width*2)
     return ans
def AreaAndPerimeters():
     print('\nArea And Perimeters')
     print('Please choose from below')
     print('Answer in block CAPS')
     selection=input('\n'.join(['Area','A1) Triangle','A2) Rectangle','A3) Circle','A4) Trapezium','','Perimeters','P1) Square', 'P2) Rectangle'])+'\n')
     if selection=='A1':
          ans=trianglearea()
     elif selection=='A2':
          ans=rectanglearea()
     elif selection=='A3':
          ans=circlearea()
     elif selection=='A4':
          ans=trapeziumarea()
     elif selection=='P1':
          ans=squareperimeter()
     elif selection=='P2':
          ans=rectangleperimeter()
     print('Answer: ' + str(ans))
def AngleFacts():
     print('\nAngle Facts')
     print('\n'.join(
          ['Sum of all angles in a triangle = 180°',
           'Sum of all angles on a straight line = 180°',
           'Sum of exterior angles in a polygon = 360°',
           'Sum of interior angles in a polygon = 180x(n-2), n being num of sides'
           ]))
     t.sleep(5)
#Menu
while True:
     print('\nWelcome to the Math helper')
     print('Please choose from below')
     print('Answer in block CAPS')
     selection=str(input('A) Calculator\nB) Area and Perimeters\nC) Angle Facts\n'))
     if selection=='A':
          calc()
     elif selection=='B':
          AreaAndPerimeters()
     elif selection=='C':
          AngleFacts()
     


     
