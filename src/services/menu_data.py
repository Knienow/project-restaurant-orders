from models.dish import Dish
from models.ingredient import Ingredient
import csv

# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        
        with open(source_path, encoding="utf-8", mode="r") as file:
            reader = csv.DictReader(file, delimiter=",", quotechar='"')
            dishes = {}
            for row in reader:
                dish = row['dish']
                if dish not in dishes:
                    new_dish = Dish(dish, float(row['price']))
                    dishes[dish] = new_dish

                ingredient = Ingredient(row['ingredient'])
                amount = int(row['recipe_amount'])
                dishes[dish].add_ingredient_dependency(
                    ingredient,
                    amount
                )

        self.dishes = dishes.values()

