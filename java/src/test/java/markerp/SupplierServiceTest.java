package markerp;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

@DisplayName("Pruebas del servicio de proveedores")
class SupplierServiceTest {
    private SupplierService service;

    @BeforeEach
    void setUp() {
        service = new SupplierService(nit -> false);
    }

    @Test
    @DisplayName("Debe rechazar un NIT duplicado")
    void deberiaRechazarNitDuplicado() {
        service.createSupplier(new Supplier("900123456", "ACME S.A.S.", "contacto@acme.com"));
        Supplier duplicado = new Supplier("900123456", "Otra", "otra@acme.com");

        InvalidSupplierException error = assertThrows(InvalidSupplierException.class,
                () -> service.createSupplier(duplicado));
        assertEquals("El NIT ya está registrado", error.getMessage());
    }

    @Test
    @DisplayName("Debe desactivar un proveedor sin órdenes activas")
    void deberiaDesactivarProveedorSinOrdenesActivas() {
        Supplier proveedor = new Supplier("900123456", "ACME", "a@acme.com");
        service.createSupplier(proveedor);

        String mensaje = service.deleteSupplier("900123456");

        assertEquals("INACTIVO", proveedor.getEstado());
        assertEquals("Proveedor desactivado", mensaje);
    }

    @Test
    @DisplayName("No debe eliminar un proveedor con órdenes activas")
    void noDeberiaEliminarProveedorConOrdenesActivas() {
        SupplierService conOrdenes = new SupplierService(nit -> true);
        conOrdenes.createSupplier(new Supplier("900123456", "ACME", "a@acme.com"));

        assertThrows(SupplierHasActiveOrdersException.class,
                () -> conOrdenes.deleteSupplier("900123456"));
    }
}