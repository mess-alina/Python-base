ask = int(input('Введите время в секундах'))
hours = ask // 3600
minutes = ask // 60 - hours * 60
seconds = ask - hours*3600 - minutes*60
if seconds < 10:
    seconds = '0' + str(seconds)
print(hours, minutes, seconds, sep=':')