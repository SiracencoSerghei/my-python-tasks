def format_ingredients(items):
    if not items:
        return""
    if len(items) == 1:
        retirn f"{items[0]}"
    ingredients_except_last = ", ".join(items[:-1])
    ingredients_string = f"{ingredients_except_last} and {items[-1]}"

    return ingredients_string

# Пример использования функции
ingredient_list = ["2 eggs", "1 liter sugar", "1 tsp salt", "vinegar"]
formatted_ingredients = format_ingredients(ingredient_list)
print(formatted_ingredients)