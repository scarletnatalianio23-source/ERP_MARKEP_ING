Característica: Aprobación de órdenes de compra

  Escenario: Aprobar orden dentro del presupuesto
    Dado que el proveedor "ACME" tiene presupuesto disponible de $10.000.000
    Y existe una orden "OC-100" por $5.000.000 en estado "PENDIENTE"
    Cuando el jefe de compras aprueba la orden
    Entonces la orden cambia a "APROBADA"
    Y el presupuesto del proveedor se reduce a $5.000.000

  Escenario: Rechazar orden que excede el presupuesto
    Dado que el proveedor "ACME" tiene presupuesto disponible de $10.000.000
    Y existe una orden "OC-101" por $15.000.000 en estado "PENDIENTE"
    Cuando el jefe de compras aprueba la orden
    Entonces el sistema muestra "Presupuesto insuficiente"

  Escenario: No re-aprobar una orden ya aprobada
    Dado que existe una orden "OC-102" en estado "APROBADA"
    Cuando el jefe de compras intenta aprobarla de nuevo
    Entonces el sistema muestra "La orden ya está aprobada"