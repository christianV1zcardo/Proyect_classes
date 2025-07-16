import pytest
import clases

def test_calcular_total_venta_basico():
    """
    Verifica que calcular_total_venta haga la suma correctamente
    """
    
    venta = clases.Venta(id_venta=1, producto="Manzana", cantidad=5, 
                         precio_unitario=2.50, fecha="2024-07-15")
    
    total_calculado = venta.calcular_total_venta()
    assert total_calculado == pytest.approx(12.5)
    
    # escribir el resto de tewst