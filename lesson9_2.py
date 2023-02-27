"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class DivideNAZero(Exception):
    def __init__(self, text):
        self.text = text

div_ed = float(input(f'Введите делимое - '))
div_er = float(input(f'Введите делитель - '))

try:
    if div_er == 0:
        raise DivideNAZero('Делить на 0 нельзя')
    result = div_ed / div_er
except DivideNAZero as error:
        print(error)
else:
    print(f'Результат: {result}')