from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient_1 = Ingredient("manteiga")
    ingredient_2 = Ingredient("salmão")
    ingredient_3 = Ingredient("massa de lasanha")
    ingredient_lactose = Ingredient("manteiga")

    assert ingredient_1 == ingredient_lactose
    assert ingredient_1 != ingredient_2
    assert ingredient_2 != ingredient_3
    assert ingredient_3 != ingredient_1
    assert ingredient_lactose.name == "manteiga"
    assert ingredient_1.restrictions == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED
    }
    assert ingredient_2.restrictions == {
        Restriction.ANIMAL_MEAT,
        Restriction.SEAFOOD,
        Restriction.ANIMAL_DERIVED,
    }
    assert ingredient_3.restrictions == {
        Restriction.LACTOSE,
        Restriction.GLUTEN
    }
    assert repr(ingredient_lactose) == "Ingredient('manteiga')"
    assert hash(ingredient_1) == hash(ingredient_lactose)
    assert hash(ingredient_1) != hash(ingredient_2)
    assert hash(ingredient_2) != hash(ingredient_3)
    assert hash(ingredient_3) != hash(ingredient_1)



