import pytest

from compras.excepciones import InsufficientBudgetException, InvalidOrderException
from compras.ordenes import PurchaseOrder, PurchaseOrderService
from compras.proveedores import Supplier


@pytest.fixture
def proveedor():
    return Supplier("900123456", "ACME", "a@acme.com", presupuesto=10_000_000)


def test_aprueba_dentro_del_presupuesto(proveedor):
    o = PurchaseOrderService().aprobar(PurchaseOrder("OC-100", proveedor, 5_000_000))
    assert o.estado == "APROBADA"
    assert proveedor.presupuesto == 5_000_000


def test_rechaza_exceso_de_presupuesto(proveedor):
    o = PurchaseOrder("OC-101", proveedor, 20_000_000)
    with pytest.raises(InsufficientBudgetException):
        PurchaseOrderService().aprobar(o)
    assert o.estado == "PENDIENTE" and proveedor.presupuesto == 10_000_000


def test_no_reaprueba(proveedor):
    svc = PurchaseOrderService()
    o = svc.aprobar(PurchaseOrder("OC-102", proveedor, 1))
    with pytest.raises(InvalidOrderException, match="ya fue aprobada"):
        svc.aprobar(o)


def test_estado_invalido(proveedor):
    with pytest.raises(InvalidOrderException, match="Estado"):
        PurchaseOrderService().aprobar(PurchaseOrder("OC-103", proveedor, 1, "ANULADA"))
