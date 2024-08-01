from calcular_mst import calcular_mst
from exportar_resultados import exportar_resultados
from visualizar_grafo import visualizar_grafo

def test_main():
    puntos_recoleccion = [
        'Cumbaya', 'Barrio la primavera', 'Scala Shopping', 'Pasea San Francisco', 
        'La Cerámica', 'Sector de la Esperanza', 'Mercado Central de Tumbaco',
        'Plaza de Puembo', 'Parque de Puembo', 'Pifo'
    ]

    distancias_lista = [
        ('Cumbaya', 'Barrio la primavera', 2.4),
        ('Cumbaya', 'Scala Shopping', 3.5),
        ('Cumbaya', 'Pasea San Francisco', 2.4),
        ('Barrio la primavera', 'Scala Shopping', 2.4),
        ('Pasea San Francisco', 'Scala Shopping', 1.2),
        ('La Cerámica', 'Sector de la Esperanza', 6.4),
        ('Scala Shopping', 'Mercado Central de Tumbaco', 4.6),
        ('Mercado Central de Tumbaco', 'La Cerámica', 2.0),
        ('Mercado Central de Tumbaco', 'Sector de la Esperanza', 1.8),
        ('La Cerámica', 'Plaza de Puembo', 5.8),
        ('Sector de la Esperanza', 'Plaza de Puembo', 5.5),
        ('Plaza de Puembo', 'Parque de Puembo', 3.8),
        ('Plaza de Puembo', 'Pifo', 5.7),
        ('Parque de Puembo', 'Pifo', 8.6),
        ('Barrio la primavera', 'La Cerámica', 5.9)
    ]

    distancias = {}
    for inicio, destino, distancia in distancias_lista:
        distancias[(inicio, destino)] = distancia
        distancias[(destino, inicio)] = distancia

    # Calcular el Árbol de Expansión Mínima
    rutas_optimas, distancia_total = calcular_mst(puntos_recoleccion, distancias)

    # Mostrar resultados
    print("Rutas óptimas (MST):")
    for ruta in rutas_optimas:
        print(ruta)
    print(f"Distancia total recorrida: {distancia_total} Kilómetros")

    # Exportar resultados
    exportar_resultados(rutas_optimas)

    # Visualizar grafo de rutas óptimas
    visualizar_grafo(puntos_recoleccion, distancias, rutas_optimas, distancia_total)

if __name__ == "__main__":
    test_main()
