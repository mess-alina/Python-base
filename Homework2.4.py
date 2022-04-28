ask = input('Введите Вашу фразу').split()

for i, j in enumerate (ask):
    j = j[0:10]
    print(i+1, j)
