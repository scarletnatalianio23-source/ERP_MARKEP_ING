using FluentAssertions;
using MyApp.Specs.Domain;
using TechTalk.SpecFlow;

namespace MyApp.Specs.Steps
{
    [Binding]
    public class InventarioSteps
    {
        private readonly InventoryService _inventario = new InventoryService();
        private string _codigo = "";
        private Exception? _error;

        [Given(@"que el producto ""(.*)"" tiene stock (\d+)")]
        public void DadoQueElProductoTieneStock(string codigo, int stock)
        {
            _codigo = codigo;
            _inventario.RegistrarProducto(codigo, stock);
        }

        [When(@"se retiran (\d+) unidades")]
        public void CuandoSeRetiranUnidades(int cantidad)
        {
            try
            {
                _inventario.Retirar(_codigo, cantidad);
            }
            catch (Exception ex)
            {
                _error = ex;
            }
        }

        [Then(@"se lanza la excepción InsufficientStockException")]
        public void EntoncesSeLanzaLaExcepcion()
        {
            _error.Should().BeOfType<InsufficientStockException>();
        }

        [Then(@"el stock final es (\d+)")]
        public void EntoncesElStockFinalEs(int esperado)
        {
            _inventario.GetStock(_codigo).Should().Be(esperado);
        }
    }
}