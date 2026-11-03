from .excepciones import InvalidRoleException, PermissionDeniedException

# Roles del selector de MARKERP (Figma). Los permisos por rol son una
# propuesta del equipo: deben validarse con el Product Owner.
PERMISOS = {
    "Administrador": {"gestionar_proveedores", "registrar_cotizacion",
                      "aprobar_orden", "gestionar_inventario"},
    "Gerente": {"gestionar_proveedores", "registrar_cotizacion",
                "aprobar_orden", "gestionar_inventario"},
    "Asesor": {"registrar_cotizacion", "gestionar_inventario"},
    "Recursos Humanos": set(),
}


class RoleService:
    def validar_rol(self, rol):
        if rol not in PERMISOS:
            raise InvalidRoleException("Rol no válido")
        return rol

    def puede(self, rol, accion):
        self.validar_rol(rol)
        return accion in PERMISOS[rol]

    def exigir(self, rol, accion):
        if not self.puede(rol, accion):
            raise PermissionDeniedException("Acceso denegado")
