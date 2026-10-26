class SupplierCreator {
  constructor(repo) { this.repo = repo; }

  async create(proveedor) {
    const correoValido = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(proveedor.correo);
    if (!correoValido) throw new Error('Correo inválido');
    return this.repo.save({ ...proveedor, estado: 'ACTIVO' });
  }
}

module.exports = { SupplierCreator };