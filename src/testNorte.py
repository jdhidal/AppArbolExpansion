from calcular_mst import calcular_mst
from exportar_resultados import exportar_resultados
from visualizar_grafo import visualizar_grafo

def test_main():
    puntos_recoleccion = [
        'La Luz', 'Rumiñahui', 'San Carlos', 'Cotocollao',
        'La Ofelia', 'Santa Lucia Alta', 'La Bota', 'Comite del Pueblo', 
        'Ponceano Alto', 'Condado', 'Llano Grande', 
        'Carapungo', 'Carcelén', 'San José de Moran', 'Hospital Docente Calderón', 'Marianita',
        'Carcelén Bajo'
    ]

    distancias_lista = [
        ('La Luz', 'Rumiñahui', 2.8),
        ('La Luz', 'La Bota', 1.9),
        ('Rumiñahui', 'Santa Lucia Alta', 2.1),
        ('Rumiñahui', 'San Carlos', 3.7),
        ('Rumiñahui', 'La Ofelia', 3.5),
        ('San Carlos', 'Cotocollao', 3.5),
        ('San Carlos', 'La Ofelia', 3.2),
        ('Cotocollao', 'La Ofelia', 3.1),
        ('Cotocollao', 'Condado', 2.8),
        ('La Ofelia', 'Condado', 2.4),
        ('La Ofelia', 'Ponceano Alto', 2.7),
        ('La Ofelia', 'Comite del Pueblo', 3.0),
        ('Santa Lucia Alta', 'La Bota', 1.8),
        ('Santa Lucia Alta', 'Comite del Pueblo', 2.4),
        ('Condado', 'Ponceano Alto', 2.9),
        ('La Bota', 'Llano Grande', 3.3),
        ('La Bota', 'Carapungo', 4.1),
        ('La Bota', 'Comite del Pueblo', 3.0),
        ('Comite del Pueblo', 'Ponceano Alto', 3.2),
        ('Comite del Pueblo', 'Carapungo', 4.2),
        ('Comite del Pueblo', 'Carcelén', 2.2),
        ('Ponceano Alto', 'Carcelén', 2.9),
        ('Ponceano Alto', 'Carapungo', 3.8),
        ('Llano Grande', 'Carapungo', 4.0),
        ('Llano Grande', 'Hospital Docente Calderón', 3.6),
        ('Llano Grande', 'Marianita', 4.6),
        ('Carapungo', 'Carcelén', 3.9),
        ('Carapungo', 'Hospital Docente Calderón', 3.5),
        ('Carapungo', 'San José de Moran', 6.1),
        ('Carcelén', 'Hospital Docente Calderón', 2.8),
        ('Carcelén', 'San José de Moran', 4.7),
        ('Carcelén', 'Carcelén Bajo', 1.5),
        ('Hospital Docente Calderón', 'Carcelén Bajo', 2.9),
        ('Hospital Docente Calderón', 'Marianita', 5.4),
        ('Hospital Docente Calderón', 'San José de Moran', 6.0),
        ('San José de Moran', 'Carcelén Bajo', 3.5),
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
