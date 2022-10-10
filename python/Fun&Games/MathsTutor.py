import math as m
import time as t
def calc():
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
def conv():
     print('---===Measurements===---')
     print('\n'.join(['m1) mm to cm','m2) cm to m','m3) m to km','m4) km to m','m5) m to cm','m6) cm to mm']))
     t.sleep(2)
     print('---===Temperature===---')
     print('\n'.join(['t1) ℃ to ℉','t2) ℉ to ℃']))
     t.sleep(1.5)
     opt=input('Option: ')
     print(opt,'was selected')
     op=int(input('Num: '))
     if opt=='m1':
          print(op/10,'cm')
     elif opt=='m2':
          print(op/100,'m')
     elif opt=='m3':
          print(op/1000,'km')
     elif opt=='m4':
          print(op*1000,'m')
     elif opt=='m5':
          print(op*100,'cm')
     elif opt=='m6':
          print(op*10,'mm')

     elif opt=='t1':
          print((op * 9/5) + 32,'℉')
     elif opt=='t2':
          print((op - 32) * 5/9 ,'℃')
     
#Menu
while True:
     print('\nWelcome to the Math helper')
     print('Please choose from below')
     print('Answer in block CAPS')
     selection=str(input('A) Calculator\nB) Area and Perimeters\nC) Angle Facts\nD) Conversions'))
     if selection=='A':
          calc()
     elif selection=='B':
          AreaAndPerimeters()
     elif selection=='C':
          AngleFacts()
     elif selection=='D':
          conv()
