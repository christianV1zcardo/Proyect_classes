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

# TypeEerrors
def test_tipo_id():
    """
    Verifica que se lance un TypeError en id_venta si no se usa un int
    """
    with pytest.raises(TypeError):
        clases.Venta(id_venta="test", producto="Manzana", cantidad=3, 
                         precio_unitario=2.50, fecha="2024-07-15")
        
def test_tipo_producto():
    """
    Verifica que se lance un TypeError en producto si no es un str
    """
    with pytest.raises(TypeError):
        clases.Venta(id_venta=1, producto=65, cantidad=0, 
                         precio_unitario=2.50, fecha="2024-07-15")
        
def test_tipo_cantidad():
    """
    Verifica que se lance un TypeError en cantidad si no es un int o float
    """
    with pytest.raises(TypeError):
        clases.Venta(id_venta=1, producto="Manzana", cantidad="test", 
                         precio_unitario=2.50, fecha="2024-07-15")
        
def test_tipo_precio_unitario():
    """
    Verifica que se lance un TypeError en precio_unitario si no es un int 
    o float
    """
    with pytest.raises(TypeError):
        clases.Venta(id_venta=1, producto="Manzana", cantidad=4, 
                         precio_unitario="2.50 test", fecha="2024-07-15")
        
def test_tipo_fecha():
    """
    Verifica que se lance un TypeError en fecha si no es un str
    """
    with pytest.raises(TypeError):
        clases.Venta(id_venta=1, producto="Manzana", cantidad=4, 
                         precio_unitario=2.50, fecha=2024-7-15)

# ValueErrors
def test_value_id():
    """
    Verifica que se lance un ValueError en id_venta si es menor o igual a 0
    """

    with pytest.raises(ValueError):
        clases.Venta(id_venta=0, producto="Manzana", cantidad=5, 
                         precio_unitario=2.50, fecha="2024-07-15")

def test_value_producto():
    """
    Verifica que se lance un ValueError en producto si es una cadena vacía
    """

    with pytest.raises(ValueError):
        clases.Venta(id_venta=1, producto="   ", cantidad=4, 
                         precio_unitario=2.50, fecha="2024-07-15")

def test_value_cantidad():
    """
    Verifica que cantidad 0 bote un ValueError
    """
    
    with pytest.raises(ValueError):
        clases.Venta(id_venta=1, producto="Manzana", cantidad=0, 
                         precio_unitario=2.50, fecha="2024-07-15")
        
def test_value_precio_unitario():
    """
    Verifica que precio 0 bote un ValueError
    """

    with pytest.raises(ValueError):
        clases.Venta(id_venta=1, producto="Manzana", cantidad=4, 
                         precio_unitario=0, fecha="2024-07-15")
        
def test_value_fecha():
    """
    Verifica que fecha no sea una cadena vacía y bote un ValueError
    """
    
    with pytest.raises(ValueError):
        clases.Venta(id_venta=1, producto="Manzana", cantidad=4, 
                         precio_unitario=2.50, fecha="     ")
        
# AnalizadorVentas
def test_value_cargar_datos_desde_csv():
    """
    Verifica que ruta_archivo sea un str
    """
    with pytest.raises(TypeError):
        clases.AnalizadorVentas.cargar_datos_desde_csv(123)