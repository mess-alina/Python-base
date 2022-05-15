from sys import argv

argv[0], hours, rate, extraMoney = argv

def salary (hours, rate, extraMoney):
    result = (int(hours) * int(rate) + int(extraMoney))
    return print(result)

print(salary(hours, rate, extraMoney))