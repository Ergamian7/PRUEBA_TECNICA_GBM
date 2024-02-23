def minimum_jumps(x):
    """
    Calcula el número mínimo de saltos necesarios para alcanzar la posición x.

    Args:
        x (int): La posición objetivo a la que se quiere llegar.

    Returns:
        int: El número mínimo de saltos necesarios.
    """
    jumps = 0
    current_position = 0
    
    # Realiza saltos hasta alcanzar o superar la posición x
    while current_position < x:
        jumps += 1
        current_position += jumps
    
    # Verifica si la posición final coincide con x
    # Si es así, devuelve el número de saltos
    # Si la diferencia entre la posición final y x es 1, se necesita un salto adicional
    # para alcanzar x exactamente
    return jumps if current_position == x else jumps + 1 if current_position - x == 1 else jumps


if __name__ == "__main__":
    # Leer la entrada desde el archivo input.txt
    with open("input.txt", "r") as file:
        lines = file.readlines()

    # Obtener el número de casos de prueba
    t = int(lines[0])

    # Procesar cada caso de prueba
    for i in range(1, t + 1):
        x = int(lines[i])
        # Calcular y mostrar el número mínimo de saltos para cada caso de prueba
        print(minimum_jumps(x))





