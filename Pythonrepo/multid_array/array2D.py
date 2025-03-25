#2D array Rotate 

arr = [
    [1, 2, 3], 
    [4, 5, 6],
    [7, 8, 9]
]
print("starting 2D array is: ")
for row in arr:
    print(row)


for i in range(0,len(arr)):
    for j in range(i+1, len(arr)):
        arr[i][j], arr[j][i] = arr[j][i] , arr[i][j]

print("Array after swap is:")

for row in arr:
    print(row)

print("Array after Rotate is:")

newarr = []
for index in range(0,len(arr)):
    newarr.append(arr[index][::-1])
    print(arr[index][::-1])

print("New Array after rotate is: ")
for row in newarr:
    print(row)