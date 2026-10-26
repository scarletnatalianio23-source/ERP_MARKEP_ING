class SupplierService {
  constructor(repo) { this.repo = repo; }

  async deactivate(nit) {
    if (await this.repo.hasActiveOrders(nit)) {
      throw new Error('El proveedor tiene órdenes activas');
    }
    const proveedor = await this.repo.findByNit(nit);
    proveedor.estado = 'INACTIVO';
    await this.repo.save(proveedor);
    return { proveedor, mensaje: 'Proveedor desactivado' };
  }
}

class QuoteService {
  constructor(repo) { this.repo = repo; }

  async register(solicitudId, monto) {
    if (monto <= 0) throw new Error('Monto inválido');
    await this.repo.save({ solicitudId, monto });
    return 'Cotización registrada';
  }
}

class PurchaseOrderService {
  constructor(repo) { this.repo = repo; }

  async approve(id) {
    const orden = await this.repo.findById(id);
    if (orden.estado === 'APROBADA') throw new Error('La orden ya está aprobada');
    const presupuesto = await this.repo.getBudget(orden.proveedorId);
    if (orden.monto > presupuesto) throw new Error('Presupuesto insuficiente');
    orden.estado = 'APROBADA';
    return this.repo.save(orden);
  }
}

module.exports = { SupplierService, QuoteService, PurchaseOrderService };