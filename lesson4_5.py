"""
5. Сделайте профилирование кода любого или любых выполненных заданий
с помощью модуля timeit, опишите результат
"""

# используя функцию sort()
from timeit import timeit


def my_func_sort(a, b, c=0):
    list_1 = [a, b, c]
    list_1.sort()
    summa = b + c
    return summa

# без функции

def my_func(a, b, c = 0):
    sum_f = 0
    if a > b:
        sum_f = sum_f + a
        if b > c:
            sum_f = sum_f + b
        else:
            sum_f = sum_f + c
    else:
        sum_f = sum_f + b
        if a > c:
            sum_f = sum_f + a
        else:
            sum_f = sum_f + c
    return sum_f


print('Время выполнения функций')
print('my_func_sort :', timeit(
    "my_func_sort(3,4,6)", globals=globals(), number=10000))
print('my_func :', timeit("my_func(3,4,6)", globals = globals(), number = 10000))