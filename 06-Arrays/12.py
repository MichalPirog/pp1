arr=[[2,5,4] , [9,0,3]]

print(arr) #a

print(f'rows: {len(arr)}, columns: {len(arr[0])}') #b

print(arr[0][1])

print(arr[1][2])

for item in arr[1]:
    print(item,end=" ")
print()

for y in arr:
    for x in y:
        print(x,end=" ")
    print()

for y in arr:
    print(y[2])