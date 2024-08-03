import networkx as nx

def calcular_ruta_mas_corta(G, punto_inicio, punto_destino):
    try:
        ruta_mas_corta = nx.shortest_path(G, source=punto_inicio, target=punto_destino, weight='weight')
        distancia_total = nx.shortest_path_length(G, source=punto_inicio, target=punto_destino, weight='weight')
        return ruta_mas_corta, distancia_total
    except nx.NetworkXNoPath:
        return None, float('inf')

# Ejemplo de uso:
# G es el grafo que ya hemos creado con las distancias
# punto_inicio = 'Cumbaya'
# punto_destino = 'Pifo'
# ruta, distancia = calcular_ruta_mas_corta(G, punto_inicio, punto_destino)
# print(f"La ruta más corta de {punto_inicio} a {punto_destino} es: {ruta} con una distancia de {distancia} km")
