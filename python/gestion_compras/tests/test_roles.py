import pytest

from compras.excepciones import InvalidRoleException, PermissionDeniedException
from compras.roles import PERMISOS, RoleService


@pytest.fixture
def svc():
    return RoleService()


def test_cuatro_roles_del_figma():
    assert set(PERMISOS) == {"Administrador", "Recursos Humanos", "Gerente", "Asesor"}


@pytest.mark.parametrize("rol", ["Administrador", "Gerente"])
def test_administrador_y_gerente_aprueban_ordenes(svc, rol):
    assert svc.puede(rol, "aprobar_orden")


@pytest.mark.parametrize("rol", ["Asesor", "Recursos Humanos"])
def test_asesor_y_rrhh_no_aprueban_ordenes(svc, rol):
    assert not svc.puede(rol, "aprobar_orden")


def test_asesor_registra_cotizaciones(svc):
    assert svc.puede("Asesor", "registrar_cotizacion")


def test_rrhh_sin_acceso_a_compras(svc):
    assert not svc.puede("Recursos Humanos", "gestionar_inventario")


def test_exigir_permitido_no_lanza(svc):
    svc.exigir("Gerente", "aprobar_orden")


def test_exigir_denegado_lanza(svc):
    with pytest.raises(PermissionDeniedException, match="Acceso denegado"):
        svc.exigir("Asesor", "aprobar_orden")


def test_rol_invalido_lanza(svc):
    with pytest.raises(InvalidRoleException, match="Rol no válido"):
        svc.puede("Invitado", "aprobar_orden")


def test_validar_rol_devuelve_rol(svc):
    assert svc.validar_rol("Gerente") == "Gerente"
