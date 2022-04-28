ask = input('Введите месяц цифрой от 1 до 12')
Seasons = {'winter': ['1', '2', '12'], 'spring': ['3', '4', '5'], 'summer': ['6', '7', '8'], 'fall': ['9', '10', '11']}

for key in Seasons.keys():
    if ask in Seasons[key]:
        print(key)
