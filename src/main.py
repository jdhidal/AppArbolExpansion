import networkx as nx
from recopilar_datos import recopilar_datos
from calcular_mst import calcular_mst
from exportar_resultados import exportar_resultados
from visualizar_grafo import visualizar_grafo
from calcular_ruta_mas_corta import calcular_ruta_mas_corta

def main():
    # Recopilar datos
    puntos_recoleccion, distancias = recopilar_datos()

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
    G = nx.Graph()
    for (i, j), dist in distancias.items():
        G.add_edge(i, j, weight=dist)

    punto_inicio = input("Ingrese el punto de inicio para la ruta más corta: ")
    punto_destino = input("Ingrese el punto de destino para la ruta más corta: ")

    ruta_corta, distancia_corta = calcular_ruta_mas_corta(G, punto_inicio, punto_destino)
    if ruta_corta:
        print(f"La ruta más corta de {punto_inicio} a {punto_destino} es: {ruta_corta} con una distancia de {distancia_corta} km")
    else:
        print(f"No hay ruta disponible de {punto_inicio} a {punto_destino}")

    visualizar_grafo(puntos_recoleccion, distancias, rutas_optimas, distancia_total, ruta_corta, distancia_corta)

if __name__ == "__main__":
    main()
