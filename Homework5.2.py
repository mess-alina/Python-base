with open("text_file.txt", "r") as f:
    str_number = 0
    for line in f:
        str_number +=1
        a = line.split()
        word = len(a)
        print(str_number, word)