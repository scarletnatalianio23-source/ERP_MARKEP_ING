# language: es
Característica: Gestión de proveedores
  Como administrador del sistema
  Quiero registrar y eliminar proveedores
  Para mantener actualizada la base de aliados comerciales

  Antecedentes:
    Dado que el usuario administrador ha iniciado sesión

  Escenario: Registrar un proveedor válido
    Dado que no existe un proveedor con NIT "900123456"
    Cuando registro el proveedor con NIT "900123456", nombre "ACME S.A.S." y correo "contacto@acme.com"
    Entonces el proveedor se crea con estado "ACTIVO"
    Y el sistema muestra el mensaje "Proveedor registrado exitosamente"

  Escenario: Rechazar proveedor con NIT duplicado
    Dado que ya existe un proveedor con NIT "900123456"
    Cuando intento registrar otro proveedor con el mismo NIT
    Entonces el sistema muestra "El NIT ya está registrado"
    Y no se crea un nuevo proveedor

  Escenario: Eliminar proveedor sin órdenes de compra activas
    Dado que existe un proveedor "ACME" sin órdenes de compra activas
    Cuando solicito eliminar el proveedor
    Entonces el proveedor cambia a estado "INACTIVO"
    Y el sistema confirma "Proveedor desactivado"