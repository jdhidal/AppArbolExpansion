# Optimización de la Gestión de Residuos Urbanos

Este proyecto tiene como objetivo mejorar la eficiencia del sistema de recolección de residuos urbanos en una ciudad de tamaño medio, reduciendo costos operativos y mejorando el servicio a los ciudadanos.

## Estructura del Proyecto

- **data/**: Carpeta para archivos de datos.
  - **output/**: Archivos de salida.
- **src/**: Carpeta para el código fuente.
  - **calcular_mst.py**: Módulo para el análisis de árbol de expansión.
  - **recopilar_datos.py**: Módulo para la recopilación de datos.
  - **exportar_resultados.py**: Módulo para exportar los resultados.
  - **main.py**: Módulo principal para ejecutar el programa.
- **.gitignore**: Archivos y carpetas a ignorar por Git.
- **README.md**: Documentación del proyecto.

## Cómo Ejecutar el Programa

1. Instalar las dependencias:
   ```sh
   pip install pandas networkx matplotlib

2. Ejecutar
   ```sh
   cd src
   python main.py