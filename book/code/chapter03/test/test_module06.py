import unittest


""" 
Para rodar tente:
    python -m unittest book.code.chapter03.test_module06
"""


class TestClass07(unittest.TestCase):
    def test_case01(self):
        self.assertTrue("PYTHON".isupper())
        print("\nIn test_case01()")
