with open("study.txt", "r", encoding="utf-8") as st:
    edu_dict = {}
    for line in st:
        b = line[line.find(':')+2 :]
        b = b.replace('-', '0')
        b = b.replace('(л)', '')
        b = b.replace('(лаб)', '')
        b = b.replace('(пр)', '')
        b = b.split(' ')
        b = [int(i) for i in b]
        sum_hours = 0
        sum_hours = sum(b)
        edu_dict[line[0: line.find(':')]] = sum_hours
print(edu_dict)