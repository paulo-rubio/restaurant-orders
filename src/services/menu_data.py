from models.dish import Dish
from models.ingredient import Ingredient
import pandas as pd


# Req 3
def create_dishes(file):
    dishes = set()
    for line in file:
        dish = Dish(line['dish'], line['price'])
        dishes.add(dish)
    return dishes

def add_recipes(file, dishes):
    for line in file:
        dish = next((d for d in dishes if d.name == line['dish']), None)
        if dish:
            ingredient = Ingredient(line['ingredient'])
            dish.add_ingredient_dependency(ingredient, line['recipe_amount'])

def read_dishes(path):
    data = pd.read_csv(path).to_dict('records')
    dishes = create_dishes(data)
    add_recipes(data, dishes)
    return dishes

class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = read_dishes(source_path)
