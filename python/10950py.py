n = int(input())
values = []

for i in range(n):
    f, b = map(int, input().split())
    values.append(f+b)

for i in values:
    print(i)
    