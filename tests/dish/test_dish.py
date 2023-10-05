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

    plate_1 = Dish("Ravioli com molho de queijos", 39.99)
    plate_2 = Dish("Salmão na manteiga", 37.99)

    assert plate_1.name == "Ravioli com molho de queijos"
    assert plate_1.price == 39.99
    assert plate_1.recipe == {}

    assert plate_2.name == "Salmão na manteiga"
    assert plate_2.price == 37.99
    assert plate_2.recipe == {}

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

    assert repr(plate_1) == "Dish('Ravioli com molho de queijos', R$39.99)"
    assert repr(plate_2) == "Dish('Salmão na manteiga', R$37.99)"

    assert hash(plate_1) == hash(
        "Dish('Ravioli com molho de queijos', R$39.99)"
    )
    assert hash(plate_2) == hash(
        "Dish('Salmão na manteiga', R$37.99)"
    )
    assert hash(plate_1) != hash(plate_2)
    assert hash(plate_1) == hash(Dish("Ravioli com molho de queijos", 39.99))
    assert hash(plate_2) == hash(Dish("Salmão na manteiga", 37.99))

    assert (plate_1 == plate_1) is True
    assert (plate_1 == plate_2) is False
    assert (plate_1 != plate_2) is True

    plate_1.add_ingredient_dependency(ingredient_1, 3)
    plate_1.add_ingredient_dependency(ingredient_2, 1)
    plate_1.add_ingredient_dependency(ingredient_3, 15)
    plate_1.add_ingredient_dependency(ingredient_4, 1)

    assert ingredient_1 in plate_1.recipe
    assert ingredient_2 in plate_1.recipe
    assert ingredient_3 in plate_1.recipe
    assert ingredient_4 in plate_1.recipe

    assert plate_1.recipe[ingredient_1] == 3
    assert plate_1.recipe[ingredient_2] == 1
    assert plate_1.recipe[ingredient_3] == 15
    assert plate_1.recipe[ingredient_4] == 1

    assert plate_1.get_restrictions() == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,
        Restriction.GLUTEN,
    }

    assert plate_1.get_ingredients() == {
        ingredient_1,
        ingredient_2,
        ingredient_3,
        ingredient_4,
    }

    plate_2.add_ingredient_dependency(ingredient_5, 1)
    plate_2.add_ingredient_dependency(ingredient_6, 1)

    assert ingredient_5 in plate_2.recipe
    assert ingredient_6 in plate_2.recipe

    assert plate_2.recipe[ingredient_5] == 1
    assert plate_2.recipe[ingredient_6] == 1

    assert plate_2.get_restrictions() == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,
        Restriction.ANIMAL_MEAT,
        Restriction.SEAFOOD,
    }

    assert plate_2.get_ingredients() == {
        ingredient_5,
        ingredient_6,
    }
