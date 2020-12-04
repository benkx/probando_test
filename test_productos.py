import unittest
from productos import *

class TestProductos(unittest.TestCase):

    def test_nombre(self):
        
      #  self.nombre = Productos("Panela", 9)
        
        productos = Productos()
        assert productos.nombreProducto("Manzana", 12)is None
       #producto = Prodcutos()
       #self.assertEqual producto.nombreProducto("Manzana", 12)
        
    def test_precio(self):   
        productos = Productos()
        assert  5 == productos.listarPrecio(5)
