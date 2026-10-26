package markerp;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;

import static org.junit.jupiter.api.Assertions.*;

@DisplayName("Pruebas del servicio de inventario")
class InventoryServiceTest {
    private InventoryService service;

    @BeforeEach
    void setUp() {
        service = new InventoryService();
    }

    @ParameterizedTest
    @CsvSource({
        "PROD-001, 10, 3, 7, Retiro exitoso",
        "PROD-002, 5, 5, 0, Retiro exitoso",
        "PROD-003, 2, 5, 2, Stock insuficiente"
    })
    @DisplayName("Debe retirar stock o rechazar si es insuficiente")
    void deberiaRetirarORechazar(String codigo, int stock, int retiro, int stockFinal, String mensajeEsperado) {
        service.registrarProducto(codigo, stock);
        String mensaje;
        try {
            mensaje = service.retirar(codigo, retiro);
        } catch (InsufficientStockException e) {
            mensaje = e.getMessage();
        }
        assertEquals(stockFinal, service.getStock(codigo));
        assertEquals(mensajeEsperado, mensaje);
    }
}