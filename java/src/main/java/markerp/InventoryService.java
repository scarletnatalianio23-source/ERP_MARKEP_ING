package markerp;

import java.util.HashMap;
import java.util.Map;

public class InventoryService {
    private final Map<String, Integer> stock = new HashMap<>();

    public void registrarProducto(String codigo, int stockInicial) {
        if (stockInicial < 0) {
            throw new IllegalArgumentException("El stock inicial no puede ser negativo");
        }
        stock.put(codigo, stockInicial);
    }

    public int getStock(String codigo) {
        return stock.get(codigo);
    }

    public String retirar(String codigo, int cantidad) {
        int actual = stock.get(codigo);
        if (cantidad > actual) {
            throw new InsufficientStockException("Stock insuficiente");
        }
        stock.put(codigo, actual - cantidad);
        return "Retiro exitoso";
    }
}