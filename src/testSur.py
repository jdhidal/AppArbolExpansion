from calcular_mst import calcular_mst
from exportar_resultados import exportar_resultados
from visualizar_grafo import visualizar_grafo

def test_main():
    puntos_recoleccion = [
        'Terminal Terrestre Quitumbe', 'Plaza Quitumbe', 'Parque Las Cuadras', 'Mercado Las Cuadras',
        'Feria Las Cuadras', 'Fundeporte', 'Quicentro Sur', 'Estadio Gonzalo Pozo', 
        'Parque Cultural Turubamba', 'Mercado Mayorista', 'Parque de los Tubos', 
        'Liga Barrial Quito Sur', 'Parque El Calzado', 'C.C. El Recreo', 'Concha Acústica'
    ]

    distancias_lista = [
        ('Terminal Terrestre Quitumbe', 'Plaza Quitumbe', 1.2),
        ('Plaza Quitumbe', 'Parque Las Cuadras', 2.3),
        ('Parque Las Cuadras', 'Mercado Las Cuadras', 0.2),
        ('Mercado Las Cuadras', 'Feria Las Cuadras', 0.1),
        ('Mercado Las Cuadras', 'Fundeporte', 0.3),
        ('Fundeporte', 'Quicentro Sur', 0.7),
        ('Fundeporte', 'Estadio Gonzalo Pozo', 1.2),
        ('Estadio Gonzalo Pozo', 'Parque Cultural Turubamba', 0.5),
        ('Parque Cultural Turubamba', 'Mercado Mayorista', 0.5),
        ('Mercado Mayorista', 'Parque de los Tubos', 0.5),
        ('Parque de los Tubos', 'Liga Barrial Quito Sur', 0.5),
        ('Liga Barrial Quito Sur', 'Parque El Calzado', 0.5),
        ('Parque El Calzado', 'C.C. El Recreo', 1.0),
        ('C.C. El Recreo', 'Concha Acústica', 0.5)
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
