"""
Задание 6. В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
Решите через рекурсию. В задании нельзя применять циклы.
"""

from random import randint

def random_num(num_user, num_random=randint(0, 100), count_attempt=0):
    if num_user == num_random:
        print(f'Число угадано {num_random}')
        return

    if count_attempt == 10:
        print(f'Попыток больше нет. Загаданное число - {num_random}')
        return
    else:
        if num_user > num_random:
            print(f'Число больше загаданного')
        else:
            print(f'Число меньше загаданного')
    return (random_num(num_user=int(input('Попробуй еще раз - ')), count_attempt=count_attempt + 1))

print('Компьютер загадал число. У тебя есть 10 попыток отгадать его.')
random_num(num_user=int(input('Какое число загадал компьютер? -  ')))