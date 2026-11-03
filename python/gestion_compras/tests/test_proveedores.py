from unittest.mock import MagicMock

import pytest

from compras.excepciones import InvalidSupplierException, SupplierHasActiveOrdersException
from compras.proveedores import Supplier, SupplierService


@pytest.fixture
def service():
    return SupplierService()


def test_crea_proveedor_valido(service):
    p = service.create_supplier(Supplier("900123456", "ACME", "a@acme.com"))
    assert p.estado == "ACTIVO"


@pytest.mark.parametrize("nit", ["123", "", None])
def test_rechaza_nit_invalido(service, nit):
    with pytest.raises(InvalidSupplierException, match="NIT inválido"):
        service.create_supplier(Supplier(nit, "ACME", "a@acme.com"))


@pytest.mark.parametrize("correo", ["sin-arroba.com", "usuario@", "", None])
def test_rechaza_correo_invalido(service, correo):
    with pytest.raises(InvalidSupplierException, match="correo"):
        service.create_supplier(Supplier("900123456", "ACME", correo))


def test_rechaza_nombre_vacio(service):
    with pytest.raises(InvalidSupplierException, match="Nombre"):
        service.create_supplier(Supplier("900123456", "  ", "a@acme.com"))


def test_rechaza_nit_duplicado(service):
    service.create_supplier(Supplier("900123456", "ACME", "a@acme.com"))
    with pytest.raises(InvalidSupplierException, match="ya está registrado"):
        service.create_supplier(Supplier("900123456", "Otro", "b@acme.com"))


def test_no_elimina_con_ordenes_activas():
    repo = MagicMock()
    repo.has_active_orders.return_value = True
    s = SupplierService(repo_ordenes=repo)
    s.create_supplier(Supplier("900123456", "ACME", "a@acme.com"))
    with pytest.raises(SupplierHasActiveOrdersException):
        s.delete_supplier("900123456")


def test_elimina_sin_ordenes_activas_pasa_a_inactivo():
    repo = MagicMock()
    repo.has_active_orders.return_value = False
    s = SupplierService(repo_ordenes=repo)
    s.create_supplier(Supplier("900123456", "ACME", "a@acme.com"))
    assert s.delete_supplier("900123456").estado == "INACTIVO"


def test_proveedor_inexistente(service):
    with pytest.raises(InvalidSupplierException, match="no encontrado"):
        service.get_supplier("999999999")
