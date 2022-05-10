import unittest
import inspect


class TestClass02(unittest.TestCase):
    """
        - O método inspect.stack()[0][3] imprime o nome do método de teste atual.
        É útil para depuração quando você deseja saber a ordem em que os métodos 
        são executados na classe de teste.
    """

    def test_case02(self):
        print("\nRunning Test Method : " + inspect.stack()[0][3])

    def test_case01(self):
        print("\nRunning Test Method : " + inspect.stack()[0][3])

"""
    A saída foi em ordem alfabética:
        test_case01 (__main__.TestClass02) ... 
        Running Test Method : test_case01
        ok
        test_case02 (__main__.TestClass02) ...
        Running Test Method : test_case02
        ok

        ----------------------------------------------------------------------
        Ran 2 tests in 0.023s

        OK
"""

if __name__ == '__main__':
    unittest.main(verbosity=2)
