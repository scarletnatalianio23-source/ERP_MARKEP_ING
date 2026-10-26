class InventoryService {
  constructor(repo) { this.repo = repo; }

  async registerProduct(producto) {
    if (await this.repo.existsByCode(producto.codigo)) {
      throw new Error('El código del producto ya existe');
    }
    return this.repo.save(producto);
  }
}

module.exports = { InventoryService };