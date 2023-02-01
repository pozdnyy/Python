list_1 = input('Введите слова через пробел: ').split()
for i, el in enumerate(list_1, 1):
    print(i, el[0:10])