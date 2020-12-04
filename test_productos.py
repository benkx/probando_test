import unittest
from productos import Productos

class TestProductos(unittest.TestCase):

    def test_nombre(self):
        
        self.nombre = Productos("Panela", 9)

       #producto = Prodcutos()
       #self.assertEqual producto.nombreProducto("Manzana", 12)
        
        
        #products = Productos("Manzana")
        #self.assertEqual(products, "Manzana")