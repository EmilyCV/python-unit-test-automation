import pytest

"""
    Em test_case01(), uma exceção é lançada, 
    então ela passa. test_case02() não gera nenhuma exceção, 
    então falha. Como mencionado anteriormente, 
    isso é extremamente útil para testar cenários negativos.
"""
def test_case01():
    with pytest.raises(Exception):
        x = 1 / 0


def test_case02():
    with pytest.raises(Exception):
        x = 1 / 1
