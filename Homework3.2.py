def personalData (**kwargs):
    return kwargs

ask = input('Введите через пробел Ваше имя, фамилию, год рождения, эл. почту и телефон').split()
Person = personalData(name = ask[0], surname = ask[1], year = ask[2], email = ask[3], phone = ask[4])

print(Person)