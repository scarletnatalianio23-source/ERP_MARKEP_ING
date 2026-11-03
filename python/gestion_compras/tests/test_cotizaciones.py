from unittest.mock import MagicMock

import pytest

from compras.cotizaciones import QuotationService
from compras.excepciones import InvalidQuotationException


@pytest.fixture
def repo():
    return MagicMock()


@pytest.fixture
def service(repo):
    s = QuotationService(repo)
    s.abrir_solicitud("SC-001")
    return s


def test_registra_cotizacion_recibida(service, repo):
    c = service.registrar("SC-001", "900123456", 2500000)
    assert c.estado == "RECIBIDA"
    repo.save.assert_called_once_with(c)


@pytest.mark.parametrize("monto", [0, -1000, None])
def test_monto_invalido_no_guarda(service, repo, monto):
    with pytest.raises(InvalidQuotationException, match="Monto inválido"):
        service.registrar("SC-001", "900123456", monto)
    repo.save.assert_not_called()


def test_solicitud_cerrada():
    s = QuotationService()
    s.abrir_solicitud("SC-002", "CERRADA")
    with pytest.raises(InvalidQuotationException, match="no abierta"):
        s.registrar("SC-002", "900123456", 10)


def test_duplicado_mismo_proveedor(service):
    service.registrar("SC-001", "900123456", 100)
    with pytest.raises(InvalidQuotationException, match="duplicada"):
        service.registrar("SC-001", "900123456", 90)


def test_mejor_cotizacion(service):
    service.registrar("SC-001", "900000001", 300)
    service.registrar("SC-001", "900000002", 200)
    assert service.mejor_cotizacion("SC-001").nit_proveedor == "900000002"


def test_mejor_cotizacion_sin_datos(service):
    with pytest.raises(InvalidQuotationException):
        service.mejor_cotizacion("SC-001")
