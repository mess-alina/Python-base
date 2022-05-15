ask = int(input('Веедите число, факториал которого хотите узнать'))

def fact(ask):
    result = 1
    for i in range(1, ask+1):
        result = result * i
    yield result

for n in fact(ask):
    print(n)