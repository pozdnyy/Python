"""
Задание 2.

Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.

Пример:
Введите время в секундах: 3600
Время в формате ч:м:с - 1.0 : 60.0 : 3600
"""

number = int(input('Введите время в секундах:'))
hours = number // 3600
hours_done = (hours) if hours > 10 else ('0' + str(hours))
minutes = (number % 3600) // 60
minutes_done = (minutes) if minutes > 10 else ('0' + str(minutes))
seconds = (number % 3600) % 60
seconds_done = (seconds) if seconds > 10 else ('0' + str(seconds))
if hours > 24:
    print('Значение слишком большое')
else:
    print(f'{hours_done}:{minutes_done}:{seconds_done}')
