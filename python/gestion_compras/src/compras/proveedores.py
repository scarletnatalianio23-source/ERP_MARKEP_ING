import re
from dataclasses import dataclass

from .excepciones import InvalidSupplierException, SupplierHasActiveOrdersException

_EMAIL = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


@dataclass
class Supplier:
    nit: str
    nombre: str
    correo: str
    estado: str = "ACTIVO"
    presupuesto: float = 0.0


class SupplierService:
    def __init__(self, repo_ordenes=None):
        self._proveedores = {}
        self._repo_ordenes = repo_ordenes

    @staticmethod
    def _validar_nit(nit):
        if not nit or len(nit) < 9:
            raise InvalidSupplierException("NIT inválido")

    @staticmethod
    def _validar_correo(correo):
        if not correo or not _EMAIL.match(correo):
            raise InvalidSupplierException("Formato de correo inválido")

    def existe_por_nit(self, nit):
        return nit in self._proveedores

    def create_supplier(self, supplier):
        self._validar_nit(supplier.nit)
        if not supplier.nombre or not supplier.nombre.strip():
            raise InvalidSupplierException("Nombre obligatorio")
        self._validar_correo(supplier.correo)
        if self.existe_por_nit(supplier.nit):
            raise InvalidSupplierException("El NIT ya está registrado")
        self._proveedores[supplier.nit] = supplier
        return supplier

    def get_supplier(self, nit):
        if nit not in self._proveedores:
            raise InvalidSupplierException("Proveedor no encontrado")
        return self._proveedores[nit]

    def delete_supplier(self, nit):
        proveedor = self.get_supplier(nit)
        if self._repo_ordenes and self._repo_ordenes.has_active_orders(nit):
            raise SupplierHasActiveOrdersException("Proveedor con órdenes activas")
        proveedor.estado = "INACTIVO"
        return proveedor
