# language: es
Característica: Actualización de stock de productos

  Esquema del escenario: Registrar entrada de stock
    Dado que el producto "<codigo>" tiene stock actual <stock_actual>
    Cuando se registra una entrada de <cantidad> unidades
    Entonces el stock final debe ser <stock_final>
    Y el movimiento queda registrado en el historial

    Ejemplos:
      | codigo   | stock_actual | cantidad | stock_final |
      | PROD-001 | 10           | 5        | 15          |
      | PROD-002 | 0            | 20       | 20          |
      | PROD-003 | 50           | 10       | 60          |

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
      