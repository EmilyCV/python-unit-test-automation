import unittest


class TestClass01(unittest.TestCase):
    """
    - TestClasse01 é uma subclasse da classe TestCase no módulo unittest.

    - assertTrue() e assertFalse() são métodos que verificam 
    se o argumento passado a eles é True ou False, respectivamente. 
    Se o argumento atender à condição assert, o caso de teste será aprovado,
    caso contrário, ele falha.
    """

    def test_case01(self):
        my_str = "ASHWIN"
        my_int = 999
        self.assertTrue(isinstance(my_str, str))
        self.assertTrue(isinstance(my_int, int))

    def test_case02(self):
        my_pi = 3.14
        self.assertFalse(isinstance(my_pi, str))


""" 
Para um teste detalhado executar:
    python caminho-do-teste/nome-do-teste.py -v
"""

if __name__ == '__main__':
    unittest.main()
