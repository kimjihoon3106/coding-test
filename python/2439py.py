'''
init = ' '
star = '*'
n = int(input()) 
for i in range(n, 0, -1):
    print(init * (i - 1) + star * (n - (i - 1)))
n = int(input())
for i in range(1, n+1):
    print(" "*(n-i)+"*"*i)
'''

# 런타임 에러 발생으로 바로 출력으로 코드 변경

'''
n = int(input())
for i in range(n, 0, -1):
    print(' ' * (i - 1) + '*' * (n - (i - 1)))

n = int(input())
for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * i)
'''

# 런타임 에러 발생으로 바로 출력으로 코드 변경

a=int(input())
for i in range(1,a+1):
    print(" "*(a-i) + "*"*i)
