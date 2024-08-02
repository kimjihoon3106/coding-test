values = []
sum = 0

for i in range(5):
    input_values = int(input())
    if input_values % 5 == 0:
        if input_values < 40:
            input_values = 40
        values.append(input_values)
        sum = sum + input_values
    else:
        print("잘못된범위")

print(int(sum/5))
