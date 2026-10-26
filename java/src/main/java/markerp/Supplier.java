package markerp;

public class Supplier {
    private final String nit;
    private final String nombre;
    private final String correo;
    private String estado = "ACTIVO";

    public Supplier(String nit, String nombre, String correo) {
        this.nit = nit;
        this.nombre = nombre;
        this.correo = correo;
    }

    public String getNit() { return nit; }
    public String getNombre() { return nombre; }
    public String getCorreo() { return correo; }
    public String getEstado() { return estado; }
    public void setEstado(String estado) { this.estado = estado; }
}