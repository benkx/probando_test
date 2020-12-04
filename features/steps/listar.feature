Feature: listar los proctuctos productos

    Scenario Outline: listar
    Given <nombre> para listar los productos
    When se lista los productos
    #Then el <precio> del producto es correcto

    Examples:
        | name | price|
        |Manzana  | 12  |