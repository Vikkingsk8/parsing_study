
with open('numbers.txt', encoding='utf-8') as file:
    nums_1 = []
    nums_2 = []
    for i in file:
        if 99 < int(i) <=999:
            nums_1.append(i)
        elif 9 < int(i) <= 99:
            nums_2.append(int(i))
print(len(nums_1))
print(sum(nums_2))
