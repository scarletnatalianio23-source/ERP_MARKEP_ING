import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "src"))

from behave import given, when, then  # noqa: E402

from compras.excepciones import ComprasError  # noqa: E402
from compras.cotizaciones import QuotationService  # noqa: E402
from compras.inventario import InventoryService  # noqa: E402
from compras.ordenes import PurchaseOrder, PurchaseOrderService  # noqa: E402
from compras.proveedores import Supplier, SupplierService  # noqa: E402
from compras.roles import RoleService  # noqa: E402


def _intentar(context, accion):
    context.error = None
    try:
        context.resultado = accion()
    except ComprasError as e:
        context.resultado, context.error = None, e


def _respuesta(context, ok):
    return str(context.error) if context.error else ok


# ---- Proveedores
@given('que no existe un proveedor con NIT "{nit}"')
def _(context, nit):
    context.service = SupplierService()
    assert not context.service.existe_por_nit(nit)


@given('que ya existe un proveedor con NIT "{nit}"')
def _(context, nit):
    context.service = SupplierService()
    context.service.create_supplier(Supplier(nit, "Existente", "e@acme.com"))


@when('registro el proveedor con NIT "{nit}", nombre "{nombre}" y correo "{correo}"')
def _(context, nit, nombre, correo):
    _intentar(context, lambda: context.service.create_supplier(Supplier(nit, nombre, correo)))


@then('el proveedor se crea con estado "{estado}"')
def _(context, estado):
    assert context.resultado.estado == estado


@then('el sistema muestra "{mensaje}"')
def _(context, mensaje):
    assert str(context.error) == mensaje


# ---- Cotizaciones
@given('que existe una solicitud "{codigo}" en estado "{estado}"')
def _(context, codigo, estado):
    context.cot = QuotationService()
    context.cot.abrir_solicitud(codigo, estado)
    context.codigo = codigo


@when("registro una cotización por {monto:d}")
def _(context, monto):
    _intentar(context, lambda: context.cot.registrar(context.codigo, "900123456", monto))
    context.ok = "Cotización registrada"


# ---- Órdenes
@given('que el proveedor "{nombre}" tiene presupuesto disponible de {monto:d}')
def _(context, nombre, monto):
    context.prov = Supplier("900123456", nombre, "a@acme.com", presupuesto=monto)


@given('existe una orden "{codigo}" por {monto:d} en estado "{estado}"')
def _(context, codigo, monto, estado):
    context.orden = PurchaseOrder(codigo, context.prov, monto, estado)


@when("el jefe de compras aprueba la orden")
def _(context):
    _intentar(context, lambda: PurchaseOrderService().aprobar(context.orden))


@then('la orden cambia a "{estado}"')
def _(context, estado):
    assert context.orden.estado == estado


@then("el presupuesto del proveedor se reduce a {monto:d}")
def _(context, monto):
    assert context.prov.presupuesto == monto


# ---- Inventario
@given('que el producto "{codigo}" tiene stock {stock:d}')
def _(context, codigo, stock):
    context.inv = InventoryService()
    context.inv.registrar(codigo, "Insumo", stock)
    context.codigo = codigo


@when("se retiran {retiro:d} unidades")
def _(context, retiro):
    _intentar(context, lambda: context.inv.update_stock(context.codigo, -retiro))
    context.ok = "Retiro exitoso"


@then("el stock final es {final:d}")
def _(context, final):
    assert context.inv.get(context.codigo).stock == final


# ---- Roles
@given('que el usuario tiene el rol "{rol}"')
def _(context, rol):
    context.rol = rol


@when('intenta la acción "{accion}"')
def _(context, accion):
    _intentar(context, lambda: RoleService().exigir(context.rol, accion))
    context.ok = "Acceso permitido"


# ---- Compartido
@then('el sistema responde "{mensaje}"')
def _(context, mensaje):
    ok = getattr(context, "ok", "Correo válido")
    assert _respuesta(context, ok) == mensaje
