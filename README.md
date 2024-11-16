
# Dashboard de Ventas con Dash en Python

Este proyecto implementa un **dashboard interactivo** utilizando la biblioteca Dash de Python. El dashboard presenta datos sintéticos sobre ventas de productos, permitiendo visualizar información categorizada y por ciudad.

## ¿Qué es un Dashboard?

Un **dashboard** es una herramienta de visualización de datos que permite a los usuarios monitorear, analizar y extraer insights clave de la información en un formato visual interactivo. Los dashboards suelen incluir gráficos, tablas y filtros para facilitar la comprensión de los datos y la toma de decisiones.

### Características de un Dashboard:
1. **Interactividad:** Permite a los usuarios explorar datos mediante filtros y selecciones dinámicas.
2. **Visualización:** Presenta gráficos claros y significativos como barras, líneas, pastel, etc.
3. **Análisis en Tiempo Real:** Los datos pueden actualizarse dinámicamente para reflejar cambios en tiempo real.
4. **Accesibilidad:** Los dashboards se pueden integrar en aplicaciones web para que sean accesibles desde cualquier lugar.

## Descripción del Proyecto

Este proyecto genera un dashboard que visualiza las ventas de productos categorizados. Los datos sintéticos se crean con las bibliotecas `Pandas` y `Numpy`, y se visualizan usando gráficos interactivos de la biblioteca `Plotly`.

### Funcionalidades:
- Selección de categoría mediante un **Dropdown**.
- Gráfico de barras interactivo para mostrar las ventas mensuales.
- Gráfico de pastel que visualiza las ventas distribuidas por ciudad.

### Tecnologías Utilizadas:
- **Dash**: Para construir el dashboard interactivo.
- **Plotly**: Para generar gráficos.
- **Pandas** y **Numpy**: Para manejar y generar datos sintéticos.

## Requisitos Previos

Antes de ejecutar este proyecto, asegúrate de tener instalado lo siguiente:
- Python 3.x
- Bibliotecas necesarias: Dash, Pandas, Numpy, Plotly.

Instala las dependencias usando:
```bash
pip install dash pandas numpy plotly
```

## Cómo Ejecutar el Proyecto

1. Descarga o clona este repositorio.
2. Ejecuta el archivo Python que contiene el código del dashboard:
   ```bash
   python dashboard.py
   ```
3. Abre un navegador web y ve a `http://127.0.0.1:8050/`.

### Código Principal

El código utilizado en este proyecto se encuentra en el archivo `dashboard.py`. A continuación, se presenta un resumen de la lógica implementada:

1. **Generación de Datos Sintéticos:**
   Se crean ventas aleatorias asociadas a categorías, ciudades y meses.

2. **Componentes del Dashboard:**
   - Dropdown para seleccionar una categoría.
   - Gráfico de barras para mostrar las ventas mensuales.
   - Gráfico de pastel para mostrar la distribución de ventas por ciudad.

3. **Callbacks:**
   Los callbacks de Dash permiten actualizar los gráficos dinámicamente según la categoría seleccionada.

## Visualización del Dashboard

### Gráfico de Barras:
Muestra el total de ventas por mes según la categoría seleccionada.

### Gráfico de Pastel:
Muestra la distribución de las ventas por ciudad según la categoría seleccionada.

## Contribución

Si deseas mejorar este proyecto, ¡no dudes en hacer un fork y enviarnos tus sugerencias!

## Licencia

Este proyecto es de uso libre y se puede modificar según las necesidades.
