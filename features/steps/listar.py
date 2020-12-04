from behave import *
from productos import *

@given('{nombre}  para listar los productos')
def implemetacion(context, nombre):
    context.productos = Prodcutos()
    context.name = nombre
   
@when('se lista los productos')
def implementacion(context):
    context.list = context.productos.listar(context.nombre)

@then('el {precio} del producto es correcto')
def implementacion(context, precio):
    assert context.listar == precio