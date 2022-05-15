first_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
second_list = ([i for i in first_list[1:] if i > first_list[first_list.index(i) - 1] ])

print(second_list)


