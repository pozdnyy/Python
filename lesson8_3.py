"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

translation = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
support_text = []
with open('text3.txt', 'r', encoding='utf-8') as t:
    for el in t:
        el_word = el.split(' ', 1)
        el_number = el_word[1].split(' ', 1)
        support_text.append(translation[el_word[0]] + ' - ' + el_number[1])

with open('text3_new.txt', 'w', encoding='utf-8') as text_2:
    text_2.writelines(support_text)

with open('text3_new.txt', 'r', encoding='utf-8') as text_2:
    content = text_2.read()
    print(content)