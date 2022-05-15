from itertools import count, cycle

for i in count(int(input('Введите число с которого начать список'))):
    if i > 10:
        break
    else: print(i)

print('_' * 100)

List1 = [2, 7, 9, 6, 90, 5]
a = 0
for j in cycle(List1):
    if a > 8:
        break
    else: print(j)
    a+=1