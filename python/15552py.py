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

for value in values:
    print(value)


