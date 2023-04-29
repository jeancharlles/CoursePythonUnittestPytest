from module_02.cg00_apps.calculator import Calculator


def test_addition():
    calci = Calculator(10, 20)
    result = calci.calc_add()
    assert result == 30
