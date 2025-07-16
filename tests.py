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
    
# def test_calcular_total_venta_cantidad_0():
#     """
#     Verifica el total cuando la cantidad es cero
#     """
    
#     venta = clases.Venta(id_venta=1, producto="Manzana", cantidad=0, 
#                          precio_unitario=2.50, fecha="2024-07-15")
#     total_calculado = venta.calcular_total_venta()
#     assert total_calculado == pytest.approx(0)
    
# def test_calcular_total_venta_precio_0():
#     """
#     Verifica el total cuando el precio_unitario es cero
#     """
    
#     venta = clases.Venta(id_venta=1, producto="Manzana", cantidad=5, 
#                          precio_unitario=0, fecha="2024-07-15")
    
#     total_calculado = venta.calcular_total_venta()
    
#     assert total_calculado == pytest.approx(0)

def test_calcular_total_venta_cantidad_0():
    """
    Verifica que cantidad 0 bote un ValueError
    """
    
    with pytest.raises(ValueError):
        clases.Venta(id_venta=1, producto="Manzana", cantidad=0, 
                         precio_unitario=2.50, fecha="2024-07-15")
        
def test_calcular_total_venta_precio_0():
    """
    Verifica que precio 0 bote un ValueError
    """

    with pytest.raises(ValueError):
        clases.Venta(id_venta=1, producto="Manzana", cantidad=4, 
                         precio_unitario=0, fecha="2024-07-15")