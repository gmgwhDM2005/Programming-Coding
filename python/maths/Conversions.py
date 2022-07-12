import time as t
#Conversions

#Menu
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


