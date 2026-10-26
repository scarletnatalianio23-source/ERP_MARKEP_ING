package markerp;

import java.util.HashMap;
import java.util.Map;

public class SupplierService {
    private final Map<String, Supplier> proveedores = new HashMap<>();
    private final OrderRepository ordenes;

    public SupplierService(OrderRepository ordenes) {
        this.ordenes = ordenes;
    }

    public Supplier createSupplier(Supplier proveedor) {
        if (proveedores.containsKey(proveedor.getNit())) {
            throw new InvalidSupplierException("El NIT ya está registrado");
        }
        proveedores.put(proveedor.getNit(), proveedor);
        return proveedor;
    }

    public String registrar(Supplier proveedor) {
        createSupplier(proveedor);
        return "Proveedor registrado exitosamente";
    }

    public String deleteSupplier(String nit) {
        if (ordenes.hasActiveOrders(nit)) {
            throw new SupplierHasActiveOrdersException("El proveedor tiene órdenes activas");
        }
        proveedores.get(nit).setEstado("INACTIVO");
        return "Proveedor desactivado";
    }
}