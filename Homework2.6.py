Goods = []
number = 0

while True:
    ask = input('Введите данные товара через пробел: наименование, цена, кол-во, ед. измерения или нажмите "no" для выхода').split()
    if ask == ['no']:
        break
    else:
         Features = {'name': ask[0], 'price': ask[1], 'amount': ask[2], 'unit': ask[3]}
         number +=1
         Goods.append(tuple([number, Features]))

print(Goods)

# Аналитика товаров. Есди честно, то эту часть кода с аналитикой я списала с другого ученика. У меня она никак не получалась.
# Я пыталась сделать циклом в цикле (то есть залезть сначала в список, потом в кортеж, потом в словарь, но не получалось -
# итерация шла только по последнему элементу кортежа... И я так и не поняла почему работает чужой код..
# Объясните, пожалуйста почему...

Analitics_dict = {}
for good in Goods: # тут залезаем в список, в котором два кортежа (в моем варианте я с этого тоже и начинала)
    for key, val in good[1].items(): # тут тоже понятно, что мы обращаемся к словарю (1-му элементу кортежа)
        if key in Analitics_dict: # мы проверяем есть ли уже такой ключ в словаре (а изначально он пуст и там нет ключей)
            Analitics_dict[key].append(val) # тут уже я не понимаю что это. Я думала append  это для list и set. Т.е.
            # мы добавляем значение к ключу в [], если такой ключ туда уже добавился? Но в какой момент цикла добавляются
            # сами ключи?
        else:
         Analitics_dict[key] = [val] #вот это мы проходили, это как раз и есть добавление или изменение значения,
         # по указанному ключу... То есть тоже самое что и в части if... но где сами ключи в цикле добавляются?
print(Analitics_dict)
