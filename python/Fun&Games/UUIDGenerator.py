import uuid as u, time as t
while True:
     while True:
          loop=input('How many UUID\'s would you like to create? ')
          break
          try:
               int(loop)
               break
          except:
               print('Please input a number (int)')
     loop=int(loop)
     if loop<=500:
          break
     else:
          print('The max amount of UUID\'s is 500.')

TextToF=str(input('Would you like to download these UUID\'s (y/n)? '))
def uuidGen():
     uuid=u.uuid4()
     return uuid
if TextToF.lower()=='y':
     file=open("GenUUIDs.txt", "w")
     for i in range(loop):
          file.write(f"{uuidGen()}\n")
          if i == loop/2:
               t.sleep(1)
               print('Halfway Downloaded..')
               t.sleep(1)
     file.close()
     print('Success!')
     print('Downloaded GenUUIDs.txt')
else:
     for i in range(loop):
          print(f'[{i+1}]{uuidGen()}')


     
          
     


