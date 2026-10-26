const { SupplierService, QuoteService, PurchaseOrderService } = require('./services');

describe('Proveedores', () => {
  it('desactiva un proveedor sin órdenes activas', async () => {
    const repo = {
      hasActiveOrders: jest.fn().mockResolvedValue(false),
      findByNit: jest.fn().mockResolvedValue({ nit: '900123456', nombre: 'ACME', estado: 'ACTIVO' }),
      save: jest.fn().mockResolvedValue(true)
    };
    const service = new SupplierService(repo);

    const resultado = await service.deactivate('900123456');

    expect(resultado.proveedor.estado).toBe('INACTIVO');
    expect(resultado.mensaje).toBe('Proveedor desactivado');
    expect(repo.save).toHaveBeenCalledTimes(1);
  });
});

describe('Cotizaciones', () => {
  let repo, service;
  beforeEach(() => {
    repo = { save: jest.fn().mockResolvedValue(true) };
    service = new QuoteService(repo);
  });

  it('registra una cotización válida', async () => {
    const mensaje = await service.register('SC-001', 2500000);
    expect(mensaje).toBe('Cotización registrada');
    expect(repo.save).toHaveBeenCalledTimes(1);
  });

  it.each([[0], [-1000]])('rechaza el monto %i', async (monto) => {
    await expect(service.register('SC-001', monto)).rejects.toThrow('Monto inválido');
    expect(repo.save).not.toHaveBeenCalled();
  });
});

describe('Órdenes de compra', () => {
  let repo, service;
  beforeEach(() => {
    repo = {
      findById: jest.fn(),
      getBudget: jest.fn(),
      save: jest.fn().mockImplementation(async (o) => o)
    };
    service = new PurchaseOrderService(repo);
  });

  it('rechaza una orden que excede el presupuesto', async () => {
    repo.findById.mockResolvedValue({ id: 101, monto: 15000000, estado: 'PENDIENTE', proveedorId: 1 });
    repo.getBudget.mockResolvedValue(10000000);

    await expect(service.approve(101)).rejects.toThrow('Presupuesto insuficiente');
    expect(repo.save).not.toHaveBeenCalled();
  });

  it('no re-aprueba una orden ya aprobada', async () => {
    repo.findById.mockResolvedValue({ id: 102, monto: 1000000, estado: 'APROBADA', proveedorId: 1 });

    await expect(service.approve(102)).rejects.toThrow('La orden ya está aprobada');
  });

  it('aprueba una orden dentro del presupuesto', async () => {
    repo.findById.mockResolvedValue({ id: 100, monto: 5000000, estado: 'PENDIENTE', proveedorId: 1 });
    repo.getBudget.mockResolvedValue(10000000);

    const orden = await service.approve(100);

    expect(orden.estado).toBe('APROBADA');
    expect(repo.save).toHaveBeenCalledTimes(1);
  });
});