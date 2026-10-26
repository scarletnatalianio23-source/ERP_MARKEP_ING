namespace MyApp.Specs.Domain
{
    public class InsufficientStockException : Exception
    {
        public InsufficientStockException(string mensaje) : base(mensaje) { }
    }

    public class InventoryService
    {
        private readonly Dictionary<string, int> _stock = new();

        public void RegistrarProducto(string codigo, int stock)
        {
            _stock[codigo] = stock;
        }

        public int GetStock(string codigo)
        {
            return _stock[codigo];
        }

        public string Retirar(string codigo, int cantidad)
        {
            var actual = _stock[codigo];
            if (cantidad > actual)
            {
                throw new InsufficientStockException("Stock insuficiente");
            }
            _stock[codigo] = actual - cantidad;
            return "Retiro exitoso";
        }
    }
}