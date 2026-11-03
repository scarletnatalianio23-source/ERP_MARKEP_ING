# language: es
Característica: Roles y permisos de MARKERP

  Escenario: El gerente puede aprobar órdenes
    Dado que el usuario tiene el rol "Gerente"
    Cuando intenta la acción "aprobar_orden"
    Entonces el sistema responde "Acceso permitido"

  Escenario: El asesor no puede aprobar órdenes
    Dado que el usuario tiene el rol "Asesor"
    Cuando intenta la acción "aprobar_orden"
    Entonces el sistema responde "Acceso denegado"

  Escenario: Un rol inexistente es rechazado
    Dado que el usuario tiene el rol "Invitado"
    Cuando intenta la acción "aprobar_orden"
    Entonces el sistema responde "Rol no válido"
