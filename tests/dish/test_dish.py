from src.models.dish import Dish
from src.models.ingredient import Ingredient, Restriction
import pytest # noqa: F401, E261, E501


# Req 2
def test_dish():
    ingredient_1 = Ingredient("queijo mussarela")
    ingredient_2 = Ingredient("queijo parmesão")
    ingredient_3 = Ingredient("massa de ravioli")
    ingredient_4 = Ingredient("creme de leite")
    ingredient_5 = Ingredient("salmão")
    ingredient_6 = Ingredient("manteiga")

    dish_1 = Dish("Ravioli com molho de queijos", 39.99)
    dish_2 = Dish("Salmão na manteiga", 37.99)

    assert dish_1.name == "Ravioli com molho de queijos"
    assert dish_1.price == 39.99
    assert dish_1.recipe == {}

    assert dish_2.name == "Salmão na manteiga"
    assert dish_2.price == 37.99
    assert dish_2.recipe == {}

    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish("tiramisu", "15%")
    with pytest.raises(
        ValueError,
        match="Dish price must be greater then zero."
    ):
        Dish("tiramisu", 0)
    with pytest.raises(
        ValueError,
        match="Dish price must be greater then zero."
    ):
        Dish("tiramisu", -20)

    assert repr(dish_1) == "Dish('Ravioli com molho de queijos', R$39.99)"
    assert repr(dish_2) == "Dish('Salmão na manteiga', R$37.99)"

    assert hash(dish_1) == hash(
        "Dish('Ravioli com molho de queijos', R$39.99)"
    )
    assert hash(dish_2) == hash(
        "Dish('Salmão na manteiga', R$37.99)"
    )
    assert hash(dish_1) != hash(dish_2)
    assert hash(dish_1) == hash(Dish("Ravioli com molho de queijos", 39.99))
    assert hash(dish_2) == hash(Dish("Salmão na manteiga", 37.99))

    assert (dish_1 == dish_1) is True
    assert (dish_1 == dish_2) is False
    assert (dish_1 != dish_2) is True

    dish_1.add_ingredient_dependency(ingredient_1, 3)
    dish_1.add_ingredient_dependency(ingredient_2, 1)
    dish_1.add_ingredient_dependency(ingredient_3, 15)
    dish_1.add_ingredient_dependency(ingredient_4, 1)

    assert ingredient_1 in dish_1.recipe
    assert ingredient_2 in dish_1.recipe
    assert ingredient_3 in dish_1.recipe
    assert ingredient_4 in dish_1.recipe

    assert dish_1.recipe[ingredient_1] == 3
    assert dish_1.recipe[ingredient_2] == 1
    assert dish_1.recipe[ingredient_3] == 15
    assert dish_1.recipe[ingredient_4] == 1

    assert dish_1.get_restrictions() == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,
        Restriction.GLUTEN,
    }

    assert dish_1.get_ingredients() == {
        ingredient_1,
        ingredient_2,
        ingredient_3,
        ingredient_4,
    }

    dish_2.add_ingredient_dependency(ingredient_5, 1)
    dish_2.add_ingredient_dependency(ingredient_6, 1)

    assert ingredient_5 in dish_2.recipe
    assert ingredient_6 in dish_2.recipe

    assert dish_2.recipe[ingredient_5] == 1
    assert dish_2.recipe[ingredient_6] == 1

    assert dish_2.get_restrictions() == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,
        Restriction.ANIMAL_MEAT,
        Restriction.SEAFOOD,
    }

    assert dish_2.get_ingredients() == {
        ingredient_5,
        ingredient_6,
    }
