# Analizador de Datos de Ventas Simples

Este proyecto Python implementa un sistema básico de análisis de datos de ventas utilizando los principios de la Programación Orientada a Objetos (POO). Permite cargar datos de ventas desde un archivo CSV, validar su integridad y realizar análisis fundamentales sobre las transacciones.

---

## 📊 Descripción del Proyecto

El objetivo principal de este proyecto es demostrar la aplicación de clases y objetos para estructurar y gestionar datos de manera eficiente. Se enfoca en la creación de dos clases principales: `Venta` para representar transacciones individuales y `AnalizadorVentas` para gestionar la colección de ventas y realizar operaciones de análisis sobre ellas. Se ha puesto un énfasis particular en la robustez del código mediante la validación de entradas y el manejo de errores, así como en la calidad a través de pruebas unitarias exhaustivas.

---

## ✨ Características Principales

### Clase `Venta`
Representa una transacción de venta individual con las siguientes características:
* **Atributos:** `id_venta`, `producto`, `cantidad`, `precio_unitario`, `fecha`.
* **Validación Robusta:** El constructor (`__init__`) valida rigurosamente los tipos y valores de los datos de entrada, lanzando `TypeError` o `ValueError` para datos inválidos (ej. cantidades negativas, productos vacíos).
* **Método `calcular_total_venta()`:** Calcula el valor monetario total de la venta (`cantidad * precio_unitario`).
* **Representación (`__repr__`)**: Proporciona una representación legible del objeto para facilitar la depuración.

### Clase `AnalizadorVentas`
Actúa como el gestor central de las ventas y el motor de análisis:
* **Atributo de Clase `_todas_las_ventas`:** Almacena todas las instancias de `Venta` cargadas, compartidas por todas las instancias del analizador.
* **Método de Clase `cargar_datos_desde_csv()` (`@classmethod`):**
    * Lee un archivo CSV (con soporte para separadores y codificaciones específicas como `latin-1`).
    * Procesa cada fila del CSV, intentando crear un objeto `Venta` validado.
    * Maneja `FileNotFoundError` si el archivo no existe.
    * Maneja errores de validación de `Venta` (TypeError, ValueError) y `KeyError` (columnas faltantes) por fila, imprimiendo advertencias y continuando el procesamiento sin detener la carga completa.
    * Utiliza un método estático auxiliar (`_procesar_dataframe_ventas`) para la lógica de procesamiento fila por fila, mejorando la modularidad.
* **Métodos de Instancia para Análisis:**
    * **`obtener_total_ventas()`:** Calcula la suma total del valor de todas las ventas.
    * **`obtener_venta_promedio()`:** Calcula el valor promedio por transacción, manejando el caso de lista de ventas vacía.
    * **`obtener_ventas_por_producto()`:** Agrupa las ventas por nombre de producto y suma sus valores monetarios totales, devolviendo una `pd.Series` ordenada.

---

## 🧑‍💻 Autor

[Christian Vizcardo]
[www.linkedin.com/in/christian-vizcardo]