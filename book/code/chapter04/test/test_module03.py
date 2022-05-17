import collections
from mypackage.mymathlib import *

collections.Callable = collections.abc.Callable
math_obj = 0

"""
    nosetests -vs .\book\code\chapter04\test\test_module03.py
"""

def setUpModule():
    """chamado uma vez, antes de qualquer outra coisa neste módulo"""
    print("In setUpModule()...")
    global math_obj
    math_obj = mymathlib()


def tearDownModule():
    """chamado uma vez, depois de tudo neste módulo"""
    print("In tearDownModule()...")
    global math_obj
    del math_obj


class TestClass02:
    @classmethod
    def setUpClass(cls):
        """chamado uma vez, antes de qualquer teste na classe"""
        print("In setUpClass()...")

    def setUp(self):
        """chamado antes de cada método de teste"""
        print("\nIn setUp()...")

    def test_case01(self):
        print("In test_case01()")
        assert math_obj.add(2, 5) == 7

    def test_case02(self):
        print("In test_case02()")

    def tearDown(self):
        """chamado após cada método de teste"""
        print("In tearDown()...")

    @classmethod
    def tearDownClass(cls):
        """chamado uma vez, após todos os testes, se setUpClass() for bem sucedido"""
        print("\nIn tearDownClass()...")
