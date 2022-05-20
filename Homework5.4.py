with open("numbers.txt", "r") as N:
    num_list =  []
    for line in N:
        str_list = line.split('-')
        num_list.append(str_list[1])
    russian = ['Один', 'Два', 'Три', 'Четыре']
    my_str = [i + '-' + j for i,j in zip(russian,num_list)]
    with open("new_number.txt", "w", encoding="utf-8") as NN:
        NN.writelines(my_str)
