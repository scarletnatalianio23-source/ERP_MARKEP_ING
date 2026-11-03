class ComprasError(Exception):
    """Base de errores de dominio."""


class InvalidSupplierException(ComprasError):
    pass


class SupplierHasActiveOrdersException(ComprasError):
    pass


class InvalidQuotationException(ComprasError):
    pass


class InvalidOrderException(ComprasError):
    pass


class InsufficientBudgetException(ComprasError):
    pass


class InvalidProductException(ComprasError):
    pass


class InsufficientStockException(ComprasError):
    pass


class PermissionDeniedException(ComprasError):
    pass


class InvalidRoleException(ComprasError):
    pass
