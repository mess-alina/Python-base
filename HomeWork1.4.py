number = int(input('Введите положительное число'))
maxCifra = 1
while number > 0:
    cifra = number % 10
    if cifra > maxCifra:
        maxCifra = cifra
    number = number // 10
print(maxCifra)