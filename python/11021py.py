import sys
input = sys.stdin.read

data = input().split()

n = int(data[0])
values = []

index = 1
for i in range(n):
    a = int(data[index])
    b = int(data[index + 1])
    values.append(a + b)
    index += 2

for i, value in enumerate(values):
    print("Case #" + str(i + 1) + ":", value)

# 같은 코드

'''
n = int(input())

values = []

for i in range(n):
    a, b = map(int, input().split())
    values.append(a + b)

for i, value in enumerate(values):
    print("Case #" + str(i + 1) + ":", value)

'''