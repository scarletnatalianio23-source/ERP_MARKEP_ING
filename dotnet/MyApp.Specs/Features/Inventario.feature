# language: es
Característica: Control de inventario

  Escenario: Rechazar retiro con stock insuficiente
    Dado que el producto "PROD-003" tiene stock 2
    Cuando se retiran 5 unidades
    Entonces se lanza la excepción InsufficientStockException
    Y el stock final es 2