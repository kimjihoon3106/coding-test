n = int(input())

input_values = input()

arr = input_values.split()


max = 0
min = 10000000000000

for i in range(0,n,1):
    if int(max) < int(arr[i]):
        max = arr[i]
    if int(min) > int(arr[i]):
        min = arr[i]
print(int(max) * int(min))
