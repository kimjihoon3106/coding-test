a, b = map(int, input().split())
arr = [0]

for i in range(1000):
    for j in range(i):
        arr.append(i)

result = sum(arr[a:b+1])
print(result)