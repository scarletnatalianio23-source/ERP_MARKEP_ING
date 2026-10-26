const { InventoryService } = require('./inventoryService');

describe('InventoryService.registerProduct', () => {
  let repo, service;

  beforeEach(() => {
    repo = {
      existsByCode: jest.fn(),
      save: jest.fn().mockResolvedValue(true)
    };
    service = new InventoryService(repo);
  });

  it('rechaza un código de producto duplicado', async () => {
    repo.existsByCode.mockResolvedValue(true);

    await expect(service.registerProduct({ codigo: 'PROD-001', nombre: 'Tornillo' }))
      .rejects.toThrow('El código del producto ya existe');
    expect(repo.save).not.toHaveBeenCalled();
  });

  it('guarda una sola vez un producto válido', async () => {
    repo.existsByCode.mockResolvedValue(false);

    await service.registerProduct({ codigo: 'PROD-004', nombre: 'Tuerca' });

    expect(repo.save).toHaveBeenCalledTimes(1);
  });
});