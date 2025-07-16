import pandas as pd

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
    
    
class AnalizadorVentas:
     
    # Almacenará todas las instancias de venta 
    _todas_las_ventas = []
    
    def __init__(self):
        print("Instancia creada")

        
    @staticmethod
    def _procesar_dataframe_ventas(df):
        """
        Itera en cada fila del df, por cada fila crea una instancia de Venta
        y retorna una lista con todos los objetos Venta

        Args:
            df (DataFrame): El dataframe a iterar

        Returns:
            list: lista con todos los objetos Venta
        """
        
        lista = [] 
        
        for i, row in df.iterrows():  # itero y extraigo valores por fila
            id_venta = row['id_venta']
            producto = row['producto']
            cantidad = row['cantidad']
            precio_unitario = row['precio_unitario']
            fecha = row['fecha']
            
            try:        
                # Creo la instancia de la venta con los valores extraidos
                inst = Venta(id_venta, producto, cantidad, precio_unitario, fecha)
                lista.append(inst)
            
            except (TypeError, ValueError) as e:
                print(f"Datos inválidos en la fila {i+1}: {e}")
            
            except KeyError as e:
                print(f"Error, falta una columna en la fila {i+1}: {e}")

            except Exception as e:
                print(f"Error en la fila {i+1}: {e}")
        
        return lista
            
            
    @classmethod
    def cargar_datos_desde_csv(cls, ruta_archivo, separador=',', 
                               codificacion='latin-1'):
        
        # Verifico que el .csv inputado sea del formato correcto
        if not isinstance(ruta_archivo, str):
            raise TypeError('La ruta del archivo debe ser un str .csv')
        
        cls._todas_las_ventas.clear()  # Deja limpio el atributo
        
        try:
            # Lee el csv
            df = pd.read_csv(ruta_archivo, sep=separador, encoding=codificacion)
            # Iteración y creación de lista de objetos Venta
            lista_ventas = cls._procesar_dataframe_ventas(df)
            # Asignación de lista de objetos Venta a atributo de clase
            cls._todas_las_ventas = lista_ventas.copy()

        except FileNotFoundError:
            print("El archivo CSV no se encuentra en la ruta especificada")
            
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
           
           
    def obtener_total_ventas(self):
        suma_ventas = 0  # Lista para almacenar la suma de ventas
        # Itero entre todos los objetos Venta y sumo su total
        for venta in self.__class__._todas_las_ventas:
            suma_ventas += venta.calcular_total_venta()
        
        return suma_ventas
    
    
    def obtener_venta_promedio(self):
        # Si la lista está vacía retorna 0 e imprime el mensaje en la consola
        if not self.__class__._todas_las_ventas:
            print("La lista de ventas se encuentra vacía.")
            return 0
    
        tot_ventas =  self.obtener_total_ventas()
        cant_ventas = len(self.__class__._todas_las_ventas)
        
        return round((tot_ventas / cant_ventas), 2)
    
    
    def obtener_ventas_por_producto(self):
        
        resultado = {}
        
        for venta in self.__class__._todas_las_ventas:
            
            if venta.producto not in resultado:
                resultado[venta.producto] = 0
            
            resultado[venta.producto] += venta.calcular_total_venta()
        
        resultado = pd.Series(resultado).sort_values(ascending=False)

        return resultado