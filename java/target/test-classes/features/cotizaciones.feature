# language: es
Característica: Solicitud de cotizaciones

  Escenario: Registrar cotización válida
    Dado que existe una solicitud "SC-001" en estado "ABIERTA"
    Cuando registro una cotización por 2500000
    Entonces el sistema responde "Cotización registrada"

  Escenario: Rechazar cotización con monto cero
    Dado que existe una solicitud "SC-001" en estado "ABIERTA"
    Cuando registro una cotización por 0
    Entonces el sistema responde "El monto debe ser mayor que cero"