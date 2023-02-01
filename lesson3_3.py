list_rate= [7, 5, 3, 3, 2]
print('Для выхода - введите "999"')
print(f"Рейтинг - {list_rate}")
num = int(input("Введите число: "))
while num != 999:
    for el in range(len(list_rate)):
        if list_rate[el] == num:
            list_rate.insert(el + 1, num)
            break
        elif list_rate[0] < num:
            list_rate.insert(0, num)
        elif list_rate[-1] > num:
            list_rate.append(num)
        elif list_rate[el] > num and list_rate[el + 1] < num:
            list_rate.insert(el + 1, num)
    print(f"Текущий список - {list_rate}")
    num = int(input("Введите число: "))