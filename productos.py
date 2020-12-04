class Productos:
    def nombreProducto(self,name,price):
        self.name = name
        self.price = price
    
    def __str__(self):
        return self.name