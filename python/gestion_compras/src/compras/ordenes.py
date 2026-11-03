from dataclasses import dataclass

from .excepciones import InsufficientBudgetException, InvalidOrderException


@dataclass
class PurchaseOrder:
    codigo: str
    proveedor: object
    monto: float
    estado: str = "PENDIENTE"


class PurchaseOrderService:
    def aprobar(self, orden):
        if orden.estado == "APROBADA":
            raise InvalidOrderException("La orden ya fue aprobada")
        if orden.estado != "PENDIENTE":
            raise InvalidOrderException("Estado de orden inválido")
        if orden.monto > orden.proveedor.presupuesto:
            raise InsufficientBudgetException("Presupuesto insuficiente")
        orden.proveedor.presupuesto -= orden.monto
        orden.estado = "APROBADA"
        return orden
