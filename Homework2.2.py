MyList = list(input('Введите значения списка'))
for i in range(0, len(MyList)-1, 2):
    MyList[i], MyList[i+1] = MyList[i+1], MyList[i]
print(MyList)