INGREDIENTS = {
    'яйцо': {'калории': 78, 'белки': 6, 'жиры': 5},
    'сыр': {'калории': 113, 'белки': 7, 'жиры': 9},
    'помидор': {'калории': 18, 'белки': 1, 'жиры': 0},
    'огурец': {'калории': 15, 'белки': 1, 'жиры': 0},
    'майонез': {'калории': 90, 'белки': 0, 'жиры': 10},
    'оливковое масло': {'калории': 119, 'белки': 0, 'жиры': 14},
}

def calculate_calories(ingredients):
    total_calories = 0
    for ingredient, amount in ingredients.items():
        calories = INGREDIENTS[ingredient]['калории']
        total_calories += (calories / 100) * amount
    return total_calories

ingredients = {
    'яйцо': 50,
    'сыр': 30,
    'помидор': 20,
    'огурец': 30,
    'майонез': 20,
    'оливковое масло': 10
}

total_calories = calculate_calories(ingredients)
print(f"Количество калорий в этом блюде: {total_calories} ккал")
