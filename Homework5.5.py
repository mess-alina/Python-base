with open("hw_5.5.txt", "r+") as hw:
    hw.write("1 3 4 7 89 15")
    hw.seek(0)
    for line in hw:
        my_list = line.split(' ')
        result = sum([int(i) for i in my_list])
        print(result)