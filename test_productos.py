import unittest
from productos import Prodcutos

class TestProductos(unittest.TestCase):

    def test_nombre(self):
        products = Prodcutos("Manzana", 12)
        self.assertEqual(products.name, "Manzana")