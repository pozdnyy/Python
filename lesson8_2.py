"""
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

count_line = 0
count_symbol = 0
count_word = 0

with open('text1.txt', 'r', encoding='utf-8') as text:
    for line in text:
        print()
        count_line += 1
        count_word = len(line.split())
        print(f'Слов в строке "{line}" - {count_word}')
        print()
        for el in line.split():
            count_symbol = len(el.strip('\n'))
            print(f'Символов в слове "{el}" - {count_symbol}')
    print()
    print(f'Строк в тексте - {count_line}')