package markerp.steps;

import io.cucumber.java.es.Cuando;
import io.cucumber.java.es.Dado;
import io.cucumber.java.es.Entonces;

import markerp.PurchaseOrder;
import markerp.PurchaseOrderService;
import markerp.QuoteService;
import markerp.Supplier;
import markerp.SupplierService;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class MarkerpSteps {
    private final SupplierService supplierService = new SupplierService(nit -> false);
    private final QuoteService quoteService = new QuoteService();
    private final PurchaseOrderService ordenService = new PurchaseOrderService();

    private Supplier proveedor;
    private PurchaseOrder orden;
    private String proveedorActual;
    private String mensaje;

    private double aNumero(String texto) {
        return Double.parseDouble(texto.replace(".", ""));
    }

    // ---------- Proveedores ----------
    @Dado("que no existe un proveedor con NIT {string}")
    public void queNoExisteProveedor(String nit) {
        // Servicio nuevo en cada escenario: no hay proveedores registrados
    }

    @Cuando("registro el proveedor con NIT {string}, nombre {string} y correo {string}")
    public void registroProveedor(String nit, String nombre, String correo) {
        proveedor = new Supplier(nit, nombre, correo);
        mensaje = supplierService.registrar(proveedor);
    }

    @Entonces("el proveedor se crea con estado {string}")
    public void proveedorConEstado(String estado) {
        assertEquals(estado, proveedor.getEstado());
    }

    @Entonces("el sistema muestra el mensaje {string}")
    public void sistemaMuestraMensaje(String esperado) {
        assertEquals(esperado, mensaje);
    }

    // ---------- Cotizaciones ----------
    @Dado("que existe una solicitud {string} en estado {string}")
    public void existeSolicitud(String codigo, String estado) {
        assertEquals("ABIERTA", estado);
    }

    @Cuando("registro una cotización por {int}")
    public void registroCotizacion(int monto) {
        try {
            mensaje = quoteService.registrar(monto);
        } catch (IllegalArgumentException e) {
            mensaje = e.getMessage();
        }
    }

    @Entonces("el sistema responde {string}")
    public void sistemaResponde(String esperado) {
        assertEquals(esperado, mensaje);
    }

    // ---------- Órdenes de compra ----------
    @Dado("^que el proveedor \"([^\"]*)\" tiene presupuesto disponible de \\$([\\d.]+)$")
    public void proveedorConPresupuesto(String nombre, String valor) {
        proveedorActual = nombre;
        ordenService.setPresupuesto(nombre, aNumero(valor));
    }

    @Dado("^existe una orden \"([^\"]*)\" por \\$([\\d.]+) en estado \"([^\"]*)\"$")
    public void existeOrden(String codigo, String monto, String estado) {
        orden = new PurchaseOrder(codigo, aNumero(monto), estado);
    }

    @Cuando("el jefe de compras aprueba la orden")
    public void jefeApruebaOrden() {
        ordenService.aprobar(proveedorActual, orden);
    }

    @Entonces("la orden cambia a {string}")
    public void ordenCambiaA(String estado) {
        assertEquals(estado, orden.getEstado());
    }

    @Entonces("^el presupuesto del proveedor se reduce a \\$([\\d.]+)$")
    public void presupuestoSeReduce(String valor) {
        assertEquals(aNumero(valor), ordenService.getPresupuesto(proveedorActual));
    }
}