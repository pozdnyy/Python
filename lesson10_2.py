"""

Задание 2.

Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов
не используя!!! методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.

Подсказки:
--- b'class' - используйте маркировку b''
--- используйте списки и циклы, не дублируйте функции
"""

words = [b'class', b'function', b'method']

for word in words:
    print(f'Слово: {word}, тип: {type(word)}, '
          f'количество букв: {len(word)}')