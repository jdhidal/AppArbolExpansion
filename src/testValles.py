import networkx as nx
from calcular_mst import calcular_mst
from exportar_resultados import exportar_resultados
from visualizar_grafo import visualizar_grafo
from calcular_ruta_mas_corta import calcular_ruta_mas_corta

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

    # Calcular la ruta más corta entre dos puntos específicos
    punto_inicio = 'Cumbaya'
    punto_fin = 'Pifo'

    # Crear un grafo con todas las distancias
    G = nx.Graph()
    for (i, j), dist in distancias.items():
        G.add_edge(i, j, weight=dist)

    ruta_corta, distancia_corta = calcular_ruta_mas_corta(G, punto_inicio, punto_fin)

    # Mostrar resultados de la ruta más corta
    print(f"Ruta más corta de {punto_inicio} a {punto_fin}: {ruta_corta}")
    print(f"Distancia de la ruta más corta: {distancia_corta} Kilómetros")

    # Visualizar grafo de rutas óptimas
    visualizar_grafo(puntos_recoleccion, distancias, rutas_optimas, distancia_total, ruta_corta, distancia_corta)

if __name__ == "__main__":
    test_main()
