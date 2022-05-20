with open("firms.txt", "r") as fr:
    firm_dict = {}
    general_profit = []

    for line in fr:
        a = line.split(' ')
        profit = int(a[2]) - int(a[3])
        firm_dict[a[0]] = profit
        print(f'Прибыль компании {a[0]} составляет {profit}')
        if profit > 0:
            general_profit.append(profit)
    print(f'Средняя прибыль компаний составляет {sum(general_profit) / len(general_profit)}')

json_list = [firm_dict, {'avarage_profit':sum(general_profit) / len(general_profit)}]
print(json_list)
import json
with open("my_json.json", "w") as jsf:
    json.dump(json_list, jsf)