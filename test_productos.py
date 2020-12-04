import unittest
from productos import Prodcutos

class TestProductos(unittest.TestCase):

    def test_nombre(self):
       
       #producto = Prodcutos()
       #self.assertEqual producto.nombreProducto("Manzana", 12)
        
        
        products = Prodcutos()
        self.assertEqual(products.name, "Manzana")