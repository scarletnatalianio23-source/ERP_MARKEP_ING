package markerp;

public class PurchaseOrder {
    private final String codigo;
    private final double monto;
    private String estado;

    public PurchaseOrder(String codigo, double monto, String estado) {
        this.codigo = codigo;
        this.monto = monto;
        this.estado = estado;
    }

    public String getCodigo() { return codigo; }
    public double getMonto() { return monto; }
    public String getEstado() { return estado; }
    public void setEstado(String estado) { this.estado = estado; }
}