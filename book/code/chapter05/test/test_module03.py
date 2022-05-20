"""
    Neste código, setup_module() e teardown_module() 
    são fixtures de nível de módulo que são invocados 
    antes e depois de qualquer outra coisa no módulo.
"""
def setup_module(module):
    print("\nIn setup_module()...")


def teardown_module(module):
    print("\nIn teardown_module()...")


"""
    setup_function() e teardown_function() são fixtures 
    de nível de função que são executados antes e depois 
    de cada função de teste no módulo.
"""
def setup_function(function):
    print("\nIn setup_function()...")


def teardown_function(function):
    print("\nIn teardown_function()...")


def test_case01():
    print("\nIn test_case01()...")


def test_case02():
    print("\nIn test_case02()...")


class TestClass02:
    """
        setup_class() e teardown_class() são os fixtures 
        de nível de classe e são executados antes e depois 
        de qualquer outra coisa na classe. Você tem que usar 
        o decorador @classmethod() com eles.
    """
    @classmethod
    def setup_class(cls):
        print("\nIn setup_class()...")

    @classmethod
    def teardown_class(cls):
        print("\nIn teardown_class()...")

    """
        setup_method() e teardown_method() são fixtures de 
        nível de método que são executados antes e depois de cada método de teste.
    """
    def setup_method(self, method):
        print("\nIn setup_method()...")

    def teardown_method(self, method):
        print("\nIn teardown_method()...")

    def test_case03(self):
        print("\nIn test_case03()...")

    def test_case04(self):
        print("\nIn test_case04()...")
