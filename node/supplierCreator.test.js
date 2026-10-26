const { SupplierCreator } = require('./supplierCreator');

describe('SupplierCreator', () => {
  let repo, service;

  beforeEach(() => {
    repo = { save: jest.fn().mockResolvedValue(true) };
    service = new SupplierCreator(repo);
  });

  it('deberiaCrearProveedorConCorreoValido', async () => {
    await service.create({ nit: '900123456', nombre: 'ACME', correo: 'contacto@acme.com' });

    expect(repo.save).toHaveBeenCalledTimes(1);
    expect(repo.save).toHaveBeenCalledWith(
      expect.objectContaining({ nit: '900123456', estado: 'ACTIVO' })
    );
  });

  it('rechaza un proveedor con correo inválido', async () => {
    await expect(service.create({ nit: '900123456', nombre: 'ACME', correo: 'correo-malo' }))
      .rejects.toThrow('Correo inválido');
    expect(repo.save).not.toHaveBeenCalled();
  });
});