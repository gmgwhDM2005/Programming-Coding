import uuid

loop=input('How many uuid\'s would you like generated?')

for i in range(int(loop)):
     print(i+1, uuid.uuid4())

