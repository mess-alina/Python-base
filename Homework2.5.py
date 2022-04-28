myList = [7, 6, 6, 4, 3, 3]
ask = int(input('Введите цифру'))

# чтобы повторяющиеся элементы не вставали перед таким же элементами в списке,
# а точно встали после, то задано условие if. Хотя рез-т все равно был бы тот же и без if.

if ask in myList:
    index = myList.index(ask) + myList.count(ask)
    myList.insert(index, ask)
else:
    myList.append(ask)
    myList.sort(reverse=True)
print(myList)


