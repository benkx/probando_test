import unittest
from productos import Prodcutos

class TestProductos(unittest.TestCase):

    def test_nombre(self):
        producto = Prodcutos()
        assert 2 == producto.nombreProducto("Manzana", 12)
        
        
        #products = Prodcutos("Manzana", 12)
        #self.assertEqual(products.name, "Manzana")