import pandas as pd
import os

def exportar_resultados(rutas_optimas):
    # Crear un DataFrame con los resultados
    df_rutas = pd.DataFrame(rutas_optimas, columns=['Punto_Inicio', 'Punto_Destino'])

    # Solicitar el nombre del archivo al usuario
    nombre_archivo = input("Ingrese el nombre del archivo (sin extensión): ")

    # Asegurarse de que el nombre del archivo termine en .csv
    if not nombre_archivo.endswith('.csv'):
        nombre_archivo += '.csv'

    # Definir la ruta del archivo
    directorio = '../data/output'
    ruta_archivo = os.path.join(directorio, nombre_archivo)

    # Crear el directorio si no existe
    if not os.path.exists(directorio):
        os.makedirs(directorio)

    # Guardar el DataFrame en un archivo CSV
    df_rutas.to_csv(ruta_archivo, index=False)

    print(f"Los resultados se han guardado en el archivo {ruta_archivo}")
