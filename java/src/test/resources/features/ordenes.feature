# language: es
Característica: Aprobación de órdenes de compra

  Escenario: Aprobar orden dentro del presupuesto
    Dado que el proveedor "ACME" tiene presupuesto disponible de $10.000.000
    Y existe una orden "OC-100" por $5.000.000 en estado "PENDIENTE"
    Cuando el jefe de compras aprueba la orden
    Entonces la orden cambia a "APROBADA"
    Y el presupuesto del proveedor se reduce a $5.000.000