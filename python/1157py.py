word = list(input())
word_num = [0] * len(word)
min = 0
maxchar = ""
existcount = 0
for i in range(len(word)):
    cnt = 0
    for j in range(len(word)):
        if word[i] == word[j]:
            cnt += 1
        word_num[i] = cnt

for i in range(len(word)):
    if word_num[i] > min:
        min = word_num[i]
        maxchar = word[i]
        existcount = 1
    elif word_num[i] == min:
        if word[i] != maxchar:
            existcount += 1


if existcount > 1:
    print('?')
else:
    if 'a' <= maxchar <= 'z':
        Bitmaxchar = ord(maxchar) - 32
    else:
        Bitmaxchar = ord(maxchar)
    print(chr(Bitmaxchar))

# 그러나 이 코드는 BeakJoon에서 시간초과라는 답변을 받는다 그러기에 같은 코드이지만 시간을 줄인 아래코드로 제출
'''
from collections import Counter

word = input().upper()

counter = Counter(word)

max_count = max(counter.values())
max_chars = [char for char, count in counter.items() if count == max_count]

if len(max_chars) > 1:
    print('?')
else:
    print(max_chars[0])

'''