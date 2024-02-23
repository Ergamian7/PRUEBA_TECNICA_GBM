def calcular_campeon(resultados, sistema_puntuacion):
    """
    Calcula al campeón o campeones basado en los resultados de carreras y un sistema de puntuación dado.

    Args:
        resultados (list): Una lista de listas que representa los resultados de las carreras. 
            Cada sublista representa una carrera y contiene las posiciones de los competidores.
        sistema_puntuacion (list): Una lista que define el sistema de puntuación a aplicar. 
            La posición i en esta lista representa la puntuación asignada a un competidor que 
            termina en la posición i + 1.

    Returns:
        list: Una lista que contiene los índices de los competidores que tienen la puntuación más alta
            según el sistema de puntuación dado.

    """
    # Inicializa una lista de puntajes con ceros, con una longitud igual al número de posiciones posibles en una carrera
    puntajes = [0] * len(resultados[0])

    # Itera sobre cada carrera en resultados y cada posición dentro de esa carrera
    for carrera in resultados:
        for i, posicion in enumerate(carrera):
            # Suma la puntuación correspondiente según el sistema de puntuación dado
            puntajes[i] += sistema_puntuacion[posicion - 1]

    # Encuentra el puntaje máximo
    max_puntaje = max(puntajes)
    
    # Encuentra los índices de los competidores que tienen el puntaje máximo
    campeones = [i + 1 for i, puntaje in enumerate(puntajes) if puntaje == max_puntaje]
    
    return campeones


def main():
    """
    Función principal que maneja la lectura del archivo de entrada y la impresión de los campeones calculados.
    """
    with open('input.txt', 'r') as f:
        while True:
            # Lee las dimensiones G (número de carreras) y P (número de posiciones) desde la primera línea
            G, P = map(int, f.readline().split())
            
            # Si ambos G y P son cero, termina el bucle
            if G == 0 and P == 0:
                break
            
            # Lee los resultados de las carreras
            resultados = [list(map(int, f.readline().split())) for _ in range(G)]
            
            # Lee el número de sistemas de puntuación
            S = int(f.readline())
            
            # Para cada sistema de puntuación
            for _ in range(S):
                # Lee la longitud del sistema de puntuación y los valores de puntuación
                K, *sistema_puntuacion = map(int, f.readline().split())
                
                # Asegura que el sistema de puntuación tenga la longitud adecuada llenando con ceros si es necesario
                sistema_puntuacion.extend([0] * (P - len(sistema_puntuacion)))
                
                # Calcula al campeón o campeones y los imprime
                campeon = calcular_campeon(resultados, sistema_puntuacion)
                print(*campeon)


if __name__ == "__main__":
    main()


