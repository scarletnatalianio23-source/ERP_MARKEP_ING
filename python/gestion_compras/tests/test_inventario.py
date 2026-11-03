import pytest

from compras.excepciones import InsufficientStockException, InvalidProductException
from compras.inventario import InventoryService


@pytest.fixture
def inv():
    return InventoryService()


def test_registra_producto(inv):
    assert inv.registrar("PROD-001", "Insumo", 5).stock == 5


@pytest.mark.parametrize("codigo,cat,stock", [("", "X", 0), ("P", "", 0), ("P", "X", -1)])
def test_registro_invalido(inv, codigo, cat, stock):
    with pytest.raises(InvalidProductException):
        inv.registrar(codigo, cat, stock)


def test_codigo_duplicado(inv):
    inv.registrar("P1", "X")
    with pytest.raises(InvalidProductException):
        inv.registrar("P1", "X")


@pytest.mark.parametrize("stock,retiro,final", [(10, 3, 7), (5, 5, 0)])
def test_retiro_exitoso(inv, stock, retiro, final):
    inv.registrar("P", "X", stock)
    assert inv.update_stock("P", -retiro) == final


def test_retiro_excesivo_mantiene_stock(inv):
    inv.registrar("P", "X", 2)
    with pytest.raises(InsufficientStockException, match="Stock insuficiente"):
        inv.update_stock("P", -5)
    assert inv.get("P").stock == 2


def test_entrada_aumenta_stock(inv):
    inv.registrar("P", "X", 1)
    assert inv.update_stock("P", 4) == 5


def test_producto_inexistente(inv):
    with pytest.raises(InvalidProductException):
        inv.get("NOPE")
