a = int(input())
evalues = list(input())
length = len(evalues)

for i in range(0,a-1,1):
    input_values = list(input())
    for j in range(length):
        if (evalues[j] != input_values[j]):
            evalues[j] = '?'

print(''.join(evalues))