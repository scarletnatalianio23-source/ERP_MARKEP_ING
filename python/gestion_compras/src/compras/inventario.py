from dataclasses import dataclass

from .excepciones import InsufficientStockException, InvalidProductException


@dataclass
class Product:
    codigo: str
    categoria: str
    stock: int = 0


class InventoryService:
    def __init__(self):
        self._productos = {}

    def registrar(self, codigo, categoria, stock=0):
        if not codigo or codigo in self._productos:
            raise InvalidProductException("Código inválido o duplicado")
        if not categoria:
            raise InvalidProductException("Categoría obligatoria")
        if stock < 0:
            raise InvalidProductException("Stock inicial inválido")
        self._productos[codigo] = Product(codigo, categoria, stock)
        return self._productos[codigo]

    def get(self, codigo):
        if codigo not in self._productos:
            raise InvalidProductException("Producto no encontrado")
        return self._productos[codigo]

    def update_stock(self, codigo, cantidad):
        producto = self.get(codigo)
        if producto.stock + cantidad < 0:
            raise InsufficientStockException("Stock insuficiente")
        producto.stock += cantidad
        return producto.stock
