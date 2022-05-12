import unittest


class TestClass11(unittest.TestCase):
    def test_case01(self):
        """This is a test method..."""
        print("\nIn test_case01()")
        # retorna o nome do método
        print(self.id())
        # retorna a descrição do método
        print(self.shortDescription())
