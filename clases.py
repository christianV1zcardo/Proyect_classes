class Venta:
    def __init__(self, id_venta, producto, cantidad, precio_unitario, fecha):
        
        if not isinstance(id_venta, int):
            raise TypeError("El ID debe ser un int")
        if id_venta <= 0:
            raise ValueError("El ID debe ser mayor que 0")
        
        
        if not isinstance(producto, str):
            raise TypeError("El producto debe ser un str")
        if not producto.strip():
            raise ValueError("El producto no puede ser un str vacío")
        
        
        if not isinstance(cantidad, (int, float)):
            raise TypeError("La cantidad debe ser int o float")
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que 0")
        
        
        if not isinstance(precio_unitario, (int, float)):
            raise TypeError("El precio_unitario deber ser un int o float")
        if precio_unitario <= 0:
            raise ValueError("El precio_unitario debe ser mayor que 0")
        
        
        if not isinstance(fecha, str):
            raise TypeError("La fecha debe ser un str")
        if not fecha.strip():
            raise ValueError("La fecha no puede ser un str vacío")
        
        
        self.id_venta = id_venta
        self.producto = producto
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.fecha = fecha
        
    def calcular_total_venta(self):
        total = self.cantidad * self.precio_unitario
        return total
    
    def __repr__(self):
        string = (f"Venta(ID={self.id_venta}, " 
                  f"Producto='{self.producto}', "
                  f"Cantidad={self.cantidad}, "
                  f"PrecioUnitario={self.precio_unitario:.2f}, "
                  f"Fecha='{self.fecha}', "
                  f"Total={self.calcular_total_venta():.2f})") 
        
        return string