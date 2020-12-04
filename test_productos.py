import unittest
from productos import *

class TestProductos(unittest.TestCase):

    def test_nombre(self):
        
      #  self.nombre = Productos("Panela", 9)
        
        productos = Productos()
        assert productos.nombreProducto("Manzana", 12)is None
       #producto = Prodcutos()
       #self.assertEqual producto.nombreProducto("Manzana", 12)
        
        
        #products = Productos("Manzana")
        #self.assertEqual(products, "Manzana")
