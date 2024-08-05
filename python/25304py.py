X = int(input())
N = int(input())
sum = 0
for i in range(N):
    result, num = map(int, input().split())
    sum = int(result * num) + sum

if sum == X:
    print("Yes")
else:
    print("No")
