Característica: Solicitud de cotizaciones

  Esquema del escenario: Validar monto de cotización
    Dado que existe una solicitud "SC-001" en estado "ABIERTA"
    Cuando registro una cotización por <monto>
    Entonces el sistema responde "<resultado>"

    Ejemplos:
      | monto   | resultado             |
      | 2500000 | Cotización registrada |
      | 0       | Monto inválido        |
      | -1000   | Monto inválido        |