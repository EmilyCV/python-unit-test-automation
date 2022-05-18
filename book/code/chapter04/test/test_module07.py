from nose.tools import raises

"""
    Quando você usa o decorador raises antes do teste, 
    ele deve lançar uma das exceções mencionadas na lista 
    de exceções associadas ao decorador @raises().
"""


@raises(TypeError, ValueError)
def test_case01():
    raise TypeError("This test passes")


@raises(Exception)
def test_case02():
    """
        Como você pode ver, test_case02() falha, 
        pois não gera uma exceção quando deveria. 
        Você pode habilmente usar isso para escrever casos de teste negativos.
    """
    pass
