# Gestión de compras — TDD, BDD y Calidad Ágil (Python)

Módulos: proveedores, cotizaciones, órdenes de compra, inventario y roles.

## Ejecutar
```bash
pip install -r requirements.txt
pytest --cov=compras --cov-report=term-missing --cov-fail-under=80   # TDD
behave                                                               # BDD
```

## Estructura
- `src/compras/`: código de producción
- `tests/`: pruebas unitarias (pytest)
- `features/`: escenarios Gherkin (español) y `steps/`
