import os
file_path = os.path.join(os.getcwd(), 'hw7_1.txt')
with open(file_path, 'rt', encoding='UTF-8') as file:

    cook_book = {}
    for line in file:
        name = line.strip()
        cook_book[name] = []
        quantity = int(file.readline().strip())
        for i in range(quantity):
            dict1 = {}
            string = (file.readline().strip()).split('|')
            dict1['ingredient_name'] = string[0]
            dict1['quantity'] = string[1]
            dict1['measure'] = string[2]
            cook_book[name] += [dict1]
        file.readline()
print(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    ingredients = []
    shop_list = {}
    for dish in dishes:
        for items in cook_book[dish]:
            little_list = {}
            little_list['measure'] = items['measure']
            little_list['quantity'] = int(items['quantity']) * person_count
            if not items['ingredient_name'] in ingredients:
                shop_list[items['ingredient_name']] = little_list
            else:
                shop_list[items['ingredient_name']+f'({dish})'] = little_list
            ingredients += [items['ingredient_name']]
    print(shop_list)


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
