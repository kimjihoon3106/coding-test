n = int(input())
n_10 = 0
n_1 = 0
nn_1 = 0
nn_10 = 0
temp = 0
turn = 0

if n<10:
    n_1 = n
else:
    n_10 = int(n / 10)
    n_1 = n % 10

while True:
    turn += 1
    nn_10 = n_1 
    nn_1 = ( n_10 + n_1 ) % 10 
    n_1 = nn_1 
    n_10 = nn_10 

    if(n_10 * 10 + n_1) == n:
        break

print(f"{turn}")
        
        
    

