"""
Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.
Класс-исключение должен контролировать типы данных элементов списка.
"""


class ErrorElement(Exception):
    def __init__(self, text):
        self.text = text


def stop_add(stop_input):
    if stop_input == 'Y' or stop_input == 'y':
        return add_unit(number=input('Введите только число - '))
    else:
        print(f'Ввод окончен')
        quit()


def add_unit(number, list_unit=[]):
    try:
        if number.isnumeric() == False:
            raise ErrorElement(
                'В список можно добавить только числа')
        while True:
            list_unit.append(number)
            print(f'Текущий список - {list_unit} \n ')
            stop_add(stop_input=input(f'Продолжать ввод? Y/N '))
    except ErrorElement as error:
        print(error)
        print(f'Текущий список - {list_unit} \n ')
        stop_add(stop_input=input(f'Продолжать ввод? Y/N '))


add_unit(number=input('Введите число - '))
