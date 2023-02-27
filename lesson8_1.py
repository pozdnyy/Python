"""
Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

mess_list = list()
def txt(mess):
    mess_list.append(mess)
    if mess != '':
        return (txt(mess=input(f'Введите текст. Для '
                               f'окончания ввода -> ENTER\n')))
    else:
        with open('text.txt', 'w', encoding='utf-8') as text:
            for el in mess_list:
                text.write(f'{el} \n')

        with open('text.txt', 'r', encoding='utf-8') as text:
            content = text.read()
        print(f'Ввод окончен')
        print(content)
        return


txt(mess=input(
    f'Введите строку текста. Для завершения ввода - нажмите ENTER\n'))