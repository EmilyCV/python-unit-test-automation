from book.code.chapter06.mypackage.calculator import Calculator
import pytest


class TestClass01:
    def test_case01(self):
        calc = Calculator()
        result = calc.add(2, 2)
        assert 4 == result

    def test_case02(self):
        with pytest.raises(ValueError):
            Calculator().add(2, 'two')

    def test_case03(self):
        with pytest.raises(ValueError):
            Calculator().add('two', 2)

    def test_case04(self):
        with pytest.raises(ValueError):
            Calculator().add('two', 'two')
