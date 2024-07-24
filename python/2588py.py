x = int(input())
y = int(input())
y1 = int(y/100)
y2 = int((y%100)/10)
y3 = int((y%100)%10)

print(x * y3)
print(x * y2)
print(x * y1)
print(x * y)
# successful