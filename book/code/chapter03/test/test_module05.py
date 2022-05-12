import unittest


def setUpModule():
    """setUpModule é executado antes de qualquer método no módulo de teste."""
    print("In setUpModule()...")


def tearDownModule():
    """tearDownModule é executado após todos os métodos no módulo de teste."""
    print("In tearDownModule()...")


class TestClass06(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """setUpClass chamado uma vez, antes de qualquer teste."""
        print("In setUpClass()...")

    @classmethod
    def tearDownClass(cls):
        """tearDownClass chamado uma vez, após todos os testes, se setUpClass for bem sucedido."""
        print("In tearDownClass()...")

    def setUp(self):
        """setUp chamado várias vezes, antes de cada método de teste."""
        print("\nIn setUp()...")

    def tearDown(self):
        """tearDown chamado várias vezes, após cada método de teste."""
        print("In tearDown()...")

    def test_case01(self):
        self.assertTrue("PYTHON".isupper())
        print("In test_case01()")

    def test_case02(self):
        self.assertFalse("python".isupper())
        print("In test_case02()")


"""
    Ordem da saída do teste em questão:
    1º - setUpModule (é executado após todos os métodos no módulo de teste)
    2º - setUpClass (chamado uma vez, antes de qualquer teste)
    3º - setUp (chamado várias vezes, antes de cada método de teste.)
    4º - test_case01
    5º - tearDown (chamado várias vezes, após cada método de teste.)
    6º - setUp (chamado várias vezes, antes de cada método de teste.)
    7º - test_case02
    8º - tearDown (chamado várias vezes, após cada método de teste.)
    9º - tearDownClass (chamado uma vez, após todos os testes, se setUpClass for bem sucedido.)
    10º - tearDownModule (é executado após todos os métodos no módulo de teste)
"""

if __name__ == '__main__':
    unittest.main()
