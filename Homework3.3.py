def my_func(a, b, c):
    d = [a, b, c]
    for i in d:
        if i == min(d):
            d.remove(min(d))
    return sum(d)

#Example:
print(my_func(5, 6, 8))