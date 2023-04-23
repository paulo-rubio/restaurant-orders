from src.models.ingredient import Ingredient  # noqa: F401, E261, E501
from src.models.ingredient import Restriction


# Req 1
def test_ingredient():
    bacon = Ingredient('bacon')
    sorvete = Ingredient('sorvete')

    assert bacon.restrictions == {
        Restriction.ANIMAL_DERIVED, Restriction.ANIMAL_MEAT
        }

    assert bacon.__repr__() == "Ingredient('bacon')"

    assert sorvete.__eq__(sorvete) is True
    assert bacon.__eq__(sorvete) is False

    assert sorvete.name == 'sorvete'

    assert hash('sorvete') == sorvete.__hash__()
    assert bacon.__hash__() != sorvete.__hash__()
