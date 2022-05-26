def int_func (text):
    WordList = text.split()
    NewList = []
    for i in WordList:
        element = str(i)
        letter1 = element[:1].upper()
        new_word = letter1 + element[1:]
        NewList.append(new_word)
    return (' '.join(NewList))

ask = input('Введите фразу')
print(int_func(ask))