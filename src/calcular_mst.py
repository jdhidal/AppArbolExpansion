import networkx as nx

def calcular_mst(puntos_recoleccion, distancias):
    G = nx.Graph()

    # Agregar nodos
    for punto in puntos_recoleccion:
        G.add_node(punto)

    # Agregar aristas con sus pesos (distancias)
    for (i, j), dist in distancias.items():
        G.add_edge(i, j, weight=dist)

    # Calcular el Árbol de Expansión Mínima usando el algoritmo de Kruskal
    mst = nx.minimum_spanning_tree(G, algorithm='kruskal')

    # Obtener las aristas del MST y calcular la distancia total
    rutas_optimas = list(mst.edges(data=False))
    distancia_total = sum(G[i][j]['weight'] for i, j in rutas_optimas)

    return rutas_optimas, distancia_total
