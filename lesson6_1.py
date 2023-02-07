"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""
from sys import argv

if len(argv) > 1:
    name_script, time_work, rate_per_hour, bonus = argv
    time_work = int(time_work)
    rate_per_hour = int(rate_per_hour)
    bonus = int(bonus)
    print(f'Заработная плата сотрудника составляет - '
          f'{(time_work * rate_per_hour) + bonus} руб.')
else:
    time_work = int(input("Введите количество часов: "))
    rate_per_hour = int(input("Введите ставку в час: "))
    bonus = int(input("Введите премию в рублях: "))
    print(f'Заработная плата сотрудника составляет - '
          f'{(time_work * rate_per_hour) + bonus} руб.')