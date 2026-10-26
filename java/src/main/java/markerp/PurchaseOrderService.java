package markerp;

import java.util.HashMap;
import java.util.Map;

public class PurchaseOrderService {
    private final Map<String, Double> presupuestos = new HashMap<>();

    public void setPresupuesto(String proveedor, double valor) {
        presupuestos.put(proveedor, valor);
    }

    public double getPresupuesto(String proveedor) {
        return presupuestos.get(proveedor);
    }

    public void aprobar(String proveedor, PurchaseOrder orden) {
        if ("APROBADA".equals(orden.getEstado())) {
            throw new IllegalStateException("La orden ya está aprobada");
        }
        double disponible = presupuestos.get(proveedor);
        if (orden.getMonto() > disponible) {
            throw new IllegalStateException("Presupuesto insuficiente");
        }
        presupuestos.put(proveedor, disponible - orden.getMonto());
        orden.setEstado("APROBADA");
    }
}