# language: es
Característica: Gestión de proveedores

  Escenario: Registrar un proveedor válido
    Dado que no existe un proveedor con NIT "900123456"
    Cuando registro el proveedor con NIT "900123456", nombre "ACME S.A.S." y correo "contacto@acme.com"
    Entonces el proveedor se crea con estado "ACTIVO"
    Y el sistema muestra el mensaje "Proveedor registrado exitosamente"