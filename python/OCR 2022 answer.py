loop = input('Num of times in loop')
array=[]
for i in range(int(loop)):
    num=int(input('Num:'))
    array.append(num)
total=sum(array)
average=total/len(array)
print('Total amount: ' + str(total)
print('Average: ' + str(average))
