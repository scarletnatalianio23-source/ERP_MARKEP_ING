# language: es
Característica: Gestión de proveedores
  Como administrador del sistema
  Quiero registrar proveedores con NIT y correo válidos
  Para mantener actualizada la base de aliados comerciales

  Escenario: Registrar un proveedor válido
    Dado que no existe un proveedor con NIT "900123456"
    Cuando registro el proveedor con NIT "900123456", nombre "ACME S.A.S." y correo "contacto@acme.com"
    Entonces el proveedor se crea con estado "ACTIVO"

  Escenario: Rechazar proveedor con NIT duplicado
    Dado que ya existe un proveedor con NIT "900123456"
    Cuando registro el proveedor con NIT "900123456", nombre "Otro" y correo "otro@acme.com"
    Entonces el sistema muestra "El NIT ya está registrado"

  Esquema del escenario: Validar formatos de correo
    Dado que no existe un proveedor con NIT "900123456"
    Cuando registro el proveedor con NIT "900123456", nombre "ACME" y correo "<correo>"
    Entonces el sistema responde "<resultado>"

    Ejemplos:
      | correo            | resultado                  |
      | contacto@acme.com | Correo válido              |
      | sin-arroba.com    | Formato de correo inválido |
      | usuario@          | Formato de correo inválido |
