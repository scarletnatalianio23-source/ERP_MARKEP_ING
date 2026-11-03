from dataclasses import dataclass

from .excepciones import InvalidQuotationException


@dataclass
class Quotation:
    solicitud: str
    nit_proveedor: str
    monto: float
    estado: str = "RECIBIDA"


class QuotationService:
    def __init__(self, repo=None):
        self._repo = repo
        self._solicitudes = {}
        self._cotizaciones = []

    def abrir_solicitud(self, codigo, estado="ABIERTA"):
        self._solicitudes[codigo] = estado

    def registrar(self, solicitud, nit_proveedor, monto):
        if self._solicitudes.get(solicitud) != "ABIERTA":
            raise InvalidQuotationException("Solicitud no abierta")
        if monto is None or monto <= 0:
            raise InvalidQuotationException("Monto inválido")
        if any(c.solicitud == solicitud and c.nit_proveedor == nit_proveedor
               for c in self._cotizaciones):
            raise InvalidQuotationException("Cotización duplicada")
        cot = Quotation(solicitud, nit_proveedor, monto)
        self._cotizaciones.append(cot)
        if self._repo:
            self._repo.save(cot)
        return cot

    def mejor_cotizacion(self, solicitud):
        candidatas = [c for c in self._cotizaciones if c.solicitud == solicitud]
        if not candidatas:
            raise InvalidQuotationException("Sin cotizaciones")
        return min(candidatas, key=lambda c: c.monto)
