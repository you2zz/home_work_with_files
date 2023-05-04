# Задача №1

from pprint import pprint
with open('recipes.txt', 'rt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dish_name = line.strip()
        ingredient_count = int(file.readline().strip())
        ingredients = []
        for _ in range(ingredient_count):
            ingredient_name, quantity, measure = file.readline().strip().split(' | ')
            ingredients.append({
                'ingredient_name': ingredient_name,
                'quantity': int(quantity),
                'measure': measure
            })
        file.readline()
        cook_book[dish_name] = ingredients
    pprint(cook_book, width=100, sort_dicts = False) 

print('\n'*3)

    # Задача №2

def get_shop_list_by_dishes(dishes, person_count):
    all_ingredients = []
    for dish in dishes:
        for ingr in cook_book[dish]:
            gf = []
            all_ingredients.append(gf)
            for k, v in ingr.items():
                gf.append(v)
    
    ingred_name = []
    uniq_ingredients = []
    for s in all_ingredients:
        if s[0] not in ingred_name:
            ingred_name.append(s[0])
            uniq_ingredients.append(s)
        else:
            uniq_ingredients[ingred_name.index(s[0])][1] += s[1]

    ingredients_dict = {}
    for l in uniq_ingredients:
        ingredients_dict.setdefault(l[0], {'measure': l[2], 'quantity': l[1] * person_count})
    return ingredients_dict

pprint(get_shop_list_by_dishes(['Омлет', 'Запеченный картофель', 'Фахитос'], 5))