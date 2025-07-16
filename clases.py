class Venta:
    def __init__(self, id_venta, producto, cantidad, precio_unitario, fecha):
        self.id_venta = id_venta
        self.producto = producto
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.fecha = fecha
        
    def calcular_total_venta(self):
        total = self.cantidad * self.precio_unitario
        return total
    
    def __repr__(self):
        string = (f"Venta(IDcaca={self.id_venta}, " 
                  f"Producto='{self.producto}', "
                  f"Cantidad={self.cantidad}, "
                  f"PrecioUnitario={self.precio_unitario:.2f}, "
                  f"Fecha='{self.fecha}', "
                  f"Total={self.calcular_total_venta():.2f})") 
        
        return string