import networkx as nx
import matplotlib.pyplot as plt

def visualizar_grafo(puntos_recoleccion, distancias, rutas_optimas, distancia_total, ruta_corta=None, distancia_corta=None):
    # Crear un grafo con todas las distancias
    G_original = nx.Graph()

    # Agregar aristas con sus pesos al grafo original
    for (i, j), dist in distancias.items():
        G_original.add_edge(i, j, weight=dist)

    # Crear el grafo para el MST
    G_mst = nx.Graph()

    # Agregar aristas del MST al grafo
    for ruta in rutas_optimas:
        i, j = ruta
        G_mst.add_edge(i, j, weight=distancias[(i, j)] if (i, j) in distancias else distancias[(j, i)])

    # Configuración para dibujar los grafos
    fig, axes = plt.subplots(1, 2, figsize=(18, 9))
    
    # Grafo Original y MST
    pos_original = nx.spring_layout(G_original)
    nx.draw(G_original, pos_original, with_labels=True, node_size=3000, node_color="lightgray", font_size=10, font_weight="bold", ax=axes[0])
    edge_labels_original = {(i, j): f"{G_original[i][j]['weight']} km" for i, j in G_original.edges}
    nx.draw_networkx_edge_labels(G_original, pos_original, edge_labels=edge_labels_original, font_color='black', ax=axes[0])
    # Dibuja el MST en el mismo gráfico
    nx.draw(G_mst, pos_original, with_labels=True, node_size=3000, node_color="lightblue", edge_color='red', width=2, font_size=10, font_weight="bold", ax=axes[0])
    edge_labels_mst = {(i, j): f"{G_mst[i][j]['weight']} km" for i, j in G_mst.edges}
    nx.draw_networkx_edge_labels(G_mst, pos_original, edge_labels=edge_labels_mst, font_color='red', ax=axes[0])
    axes[0].set_title(f'Grafo Original y Árbol de Expansión Mínima (MST)\nDistancia total del MST: {distancia_total:.2f} Kilómetros')

    # Grafo Original y Ruta más corta
    if ruta_corta:
        path_edges = list(zip(ruta_corta, ruta_corta[1:]))
        nx.draw(G_original, pos_original, with_labels=True, node_size=3000, node_color="lightgray", font_size=10, font_weight="bold", ax=axes[1])
        nx.draw_networkx_edges(G_original, pos_original, edgelist=path_edges, edge_color='blue', width=2.5, ax=axes[1])
        edge_labels_path = {(i, j): f"{G_original[i][j]['weight']} km" for i, j in path_edges}
        nx.draw_networkx_edge_labels(G_original, pos_original, edge_labels=edge_labels_original, font_color='black', ax=axes[1])
        nx.draw_networkx_edge_labels(G_original, pos_original, edge_labels=edge_labels_path, font_color='blue', ax=axes[1])
        axes[1].set_title(f'Grafo Original y Ruta más corta\n{ruta_corta[0]} a {ruta_corta[-1]}: {distancia_corta:.2f} Km')

    plt.tight_layout()
    plt.show()

