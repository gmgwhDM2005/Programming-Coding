#Casting

#We take the input as a string and assigned it to the variable "x"
x=str(input('Input a num: '))

#Casting in python is the method of converting a data type into another data type
#Here x is converted into an integer from a string and is assigned to the variable "newType"
newType=int(x)

#Using an F-String, we then print the data type value of "newType"
print(f'{type(newType)}')
