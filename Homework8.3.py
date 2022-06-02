class CheckList(Exception):
    def __init__(self, txt):
        self.txt = txt

my_list = []
while True:
    ask = input('Введите число или нажмиите "stop" для выхода')

    try:
        if ask.isdigit():
            my_list.append(ask)
        elif ask == 'stop':
            break
        else:
            raise CheckList("Введено не число")
    except CheckList as err:
        print(err)
print(my_list)

