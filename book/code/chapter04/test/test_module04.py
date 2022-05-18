from nose.tools import with_setup

"""
    - No código test_case01(), test_case02(), test_case03(), setup_function() e teardown_function() 
    são as funções. Eles não estão associados a uma classe. 
    - Você tem que usar o decorador @with_setup(), que é importado de nose.tools,
    para atribuir setup_function() e teardown_function() como fixtures de test_case03(). 
"""


def setUpModule():
    """chamado uma vez, antes de qualquer outra coisa neste módulo"""
    print("\nIn setUpModule()...")


def tearDownModule():
    """chamado uma vez, depois de tudo neste módulo"""
    print("\nIn tearDownModule()...")


def setup_function():
    """setup_function(): use-o com o decorador @with_setup()"""
    print("\nsetup_function()...")


def teardown_function():
    """teardown_function(): use-o com o decorador @with_setup()"""
    print("\nteardown_function()...")


def test_case01():
    print("In test_case01()...")


def test_case02():
    print("In test_case02()...")


"""
    setup_function() e teardown_function() são executados antes 
    e depois de test_case03(), respectivamente.
"""


@with_setup(setup_function, teardown_function)
def test_case03():
    print("In test_case03()...")
