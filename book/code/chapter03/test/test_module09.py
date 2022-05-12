from book.code.chapter03.mypackage.mymathlib import *
import unittest


math_obj = 0


def setUpModule():
    """Chamado uma vez, antes de qualquer outra coisa no módulo"""
    print("In setUpModule()...")
    global math_obj
    math_obj = mymathlib()


def tearDownModule():
    """Chamado uma vez, depois de todo no módulo"""
    print("In tearDownModule()...")
    global math_obj
    del math_obj


class TestClass10(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Chamado apenas uma vez, antes de qualquer teste na classe"""
        print("In setUpClass()...")

    def setUp(self):
        """Chamado uma vez antes de cada método de teste"""
        print("\nIn setUp()...")

    def test_case01(self):
        print("In test_case01()")
        self.assertEqual(math_obj.add(2, 5), 7)

    def test_case02(self):
        print("In test_case02()")

    def tearDown(self):
        """Chamado uma vez após cada método de teste"""
        print("In tearDown()...")

    @classmethod
    def tearDownClass(cls):
        """Chamado uma vez, depois de todos os testes da classe"""
        print("In tearDownClass()...")
