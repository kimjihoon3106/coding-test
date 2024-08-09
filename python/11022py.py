# input으로 입력받기

n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    result = a + b
    print(f"Case #{i + 1}: {a} + {b} = {result}")

# input은 한줄씩 sys.stdin.read는 여러 줄이지만 한번에

# sys.stdin.read로 입력받기

'''
import sys
input = sys.stdin.read

data = input().split()

n = int(data[0])
values = []

index = 1
for i in range(n):
    a = int(data[index])
    b = int(data[index + 1])
    values.append((a, b, a + b))  # (a, b, a + b) 형태로 저장
    index += 2

for i, (a, b, result) in enumerate(values):
    print(f"Case #{i + 1}: {a} + {b} = {result}")
'''