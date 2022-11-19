from re import A
from numpy import array, array_repr

#6.	An array contains values: 2, 3, 7, 5, 4. Create a program that displays:

array = [2,3,7,5,4]
print(array) #a
print(len(array)) #b
print(array[0]) #c
print(array[1]) #d
print(array[-1]) #e
print(array[-2]) #f
print(array[0]+array[-1]) #g
print(array[len(array)//2]) #h

for i in array: #i
    print(i, end=" ")

print()

for i in range(len(array)//2+1):
    print(array[i],end=" ")