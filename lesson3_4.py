product = []
prod_card = {'наименование': '', 'цена': '', 'количество': '', 'единица измерения': ''}
analytics = {'наименование': [], 'цена': [], 'количество': [], 'единица измерения': []}
num = 0
feature = None
control = None
while True:
    control = input("Для выхода нажмите: 'Q', для продолжения нажмите: 'Enter', для анализа нажмите: 'A'").upper()
    if control == 'Q':
        break
    num += 1
    if control == 'A':
        print(f'Текущая аналитика: ')
        for key, value in analytics.items():
            print(f'{key[:25]:>30}: {value}')
    for f in prod_card.keys():
        feature = input(f'Введите поле "{f}": ')
        prod_card[f] = int(feature) if (f == 'цена' or f == 'единица измерения') else feature
        analytics[f].append(prod_card[f])
    product.append((num, prod_card))

# ////////////////////////////////////////////////////////////////////////////////////////////////
#
# goods = int(input("Введите количество товара: "))
# i = 1
# shop_dict = []
# shop_list = []
# shop_anatics = {}
# while i <= goods:
#     shop_dict = dict({'наименование': input("Введите название: "), 'цена': input("Введите цену: "),
#                     'количество': input('Введите количество: '), 'eд': input("Введите единицу измерения: ")})
#     shop_list.append((i, shop_dict))
#     i += 1
#     shop_anatics = dict(
#         {'наименование': shop_dict.get('наименование'), 'цена': shop_dict.get('цена'), 'количество': shop_dict.get('количество'),
#          'ед': shop_dict.get('ед')})
# print(shop_list)
# print(shop_anatics)