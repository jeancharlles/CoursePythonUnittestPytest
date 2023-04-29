import module_02.cg00_apps.magic as mg


def test_magic_get_a_number_1():
    result = mg.get_a_number()
    assert result < 30


def test_magic_get_a_number_2():
    result = mg.get_a_number()
    assert result > 10


def test_magic_get_double():
    result = mg.get_double(25)
    assert result > 25


def test_get_a_list():
    result = mg.get_a_list("Dog", "Cat", "Chicken", "Rabbit")
    assert result == ["Dog", "Cat", "Chicken", "Rabbit"]
