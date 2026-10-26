package markerp;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;

import static org.junit.jupiter.api.Assertions.*;

@DisplayName("Pruebas del servicio de cotizaciones")
class QuoteServiceTest {
    private final QuoteService service = new QuoteService();

    @ParameterizedTest
    @CsvSource({
        "1000, 3, 3000",
        "250000, 2, 500000",
        "50, 10, 500"
    })
    @DisplayName("Debe calcular el total precio x cantidad")
    void deberiaCalcularTotal(double precio, int cantidad, double esperado) {
        assertEquals(esperado, service.calcularTotal(precio, cantidad));
    }

    @ParameterizedTest
    @CsvSource({
        "1000, 0",
        "5000, -1"
    })
    @DisplayName("Debe rechazar cantidad cero o negativa")
    void deberiaRechazarCantidadCeroONegativa(double precio, int cantidad) {
        IllegalArgumentException error = assertThrows(IllegalArgumentException.class,
                () -> service.calcularTotal(precio, cantidad));
        assertEquals("El monto debe ser mayor que cero", error.getMessage());
    }
}