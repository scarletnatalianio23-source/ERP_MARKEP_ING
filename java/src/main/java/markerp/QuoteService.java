package markerp;

public class QuoteService {
    public double calcularTotal(double precioUnitario, int cantidad) {
        if (cantidad <= 0) {
            throw new IllegalArgumentException("El monto debe ser mayor que cero");
        }
        return precioUnitario * cantidad;
    }

    public String registrar(double monto) {
        if (monto <= 0) {
            throw new IllegalArgumentException("El monto debe ser mayor que cero");
        }
        return "Cotización registrada";
    }
}