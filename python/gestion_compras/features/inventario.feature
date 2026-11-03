# language: es
Característica: Retiros de inventario

  Esquema del escenario: Retiro de inventario
    Dado que el producto "<codigo>" tiene stock <stock>
    Cuando se retiran <retiro> unidades
    Entonces el stock final es <final>
    Y el sistema responde "<mensaje>"

    Ejemplos:
      | codigo   | stock | retiro | final | mensaje            |
      | PROD-001 | 10    | 3      | 7     | Retiro exitoso     |
      | PROD-002 | 5     | 5      | 0     | Retiro exitoso     |
      | PROD-003 | 2     | 5      | 2     | Stock insuficiente |
