def recopilar_datos():
    num_puntos = int(input("Ingrese el número de puntos de recolección: "))
    puntos_recoleccion = []

    for i in range(num_puntos):
        punto = input(f"Ingrese el nombre del punto de recolección {i+1}: ")
        puntos_recoleccion.append(punto)

    distancias = {}
    for i in range(num_puntos):
        for j in range(i + 1, num_puntos):
            while True:
                try:
                    entrada = input(f"Ingrese la distancia entre {puntos_recoleccion[i]} y {puntos_recoleccion[j]} (ingrese 'no_conectado' si no están conectados): ").strip()
                    if entrada.lower() == 'no_conectado':
                        distancia = None
                    else:
                        distancia = float(entrada)
                        if distancia < 0:
                            raise ValueError("La distancia no puede ser negativa.")
                    break
                except ValueError as e:
                    print(f"Entrada inválida: {e}. Por favor, ingrese un número válido o 'no_conectado'.")

            if distancia is not None:
                distancias[(puntos_recoleccion[i], puntos_recoleccion[j])] = distancia
                distancias[(puntos_recoleccion[j], puntos_recoleccion[i])] = distancia
            else:
                print(f"{puntos_recoleccion[i]} y {puntos_recoleccion[j]} no están conectados.")

    return puntos_recoleccion, distancias
