x, y, z = map(int, input().split())

if(x == y):
    if(x==z):
        print(10000+x*1000)
    elif(x!=z):
        print(1000+x*100)
elif(x == z):
    if(x == y):
        print(10000+x*1000)
    elif(x != y):
        print(1000+x*100)
elif(y == z):
    if(y == x):
        print(10000+x*1000)
    elif(y != x):
        print(1000+y*100)
elif(x!=y):
    if(x!=z):
        if(x>y):
            if(x>z):
                print(100*x)
            else:
                print(100*z)
        else:
            if(y>z):
                print(100*y)
            elif(y<z):
                print(100*z)
elif(x!=z):
    if(x!=y):
        if(x>y):
            if(x>z):
                print(100*x)
            else:
                print(100*z)
        else:
            if(y>z):
                print(100*y)
            elif(y<z):
                print(100*z)
elif(z!=y):
    if(z!=x):
        if(x>y):
            if(x>z):
                print(100*x)
            else:
                print(100*z)
        else:
            if(y>z):
                print(100*y)
            elif(y<z):
                print(100*z)

# 최적화
x, y, z = map(int, input().split())

if x == y == z:
    print(10000 + x * 1000)
elif x == y or x == z:
    print(1000 + x * 100)
elif y == z:
    print(1000 + y * 100)
else:
    print(100 * max(x, y, z))
