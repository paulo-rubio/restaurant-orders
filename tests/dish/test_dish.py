from src.models.ingredient import Ingredient
from src.models.dish import Dish  # noqa: F401, E261, E501
import pytest


# Req 2
def test_dish():
    bolo = Dish('Bolo', 15.00)
    salgadinho = Dish('salgadinho', 9.00)
    manteiga = Ingredient('manteiga')

    assert bolo.name == 'Bolo'
    assert bolo.price == 15

    assert bolo.__eq__(bolo) is True
    assert bolo.__eq__(salgadinho) is False

    bolo.add_ingredient_dependency(manteiga, 0)
    assert bolo.get_ingredients() == {
        Ingredient('manteiga')
    }

    assert bolo.get_restrictions() == manteiga.restrictions

    assert bolo.__hash__() == hash(bolo.__repr__())
    assert salgadinho.__hash__() != hash(bolo.__repr__())

    assert bolo.__repr__() == "Dish('Bolo', R$15.00)"

    with pytest.raises(ValueError):
        Dish('nnada', -100)
