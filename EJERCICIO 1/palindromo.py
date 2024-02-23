def es_palindromo(frase):
    """
    Función que verifica si una cadena es un palíndromo.
    
    Parámetros:
    frase (str): La cadena que se desea verificar si es un palíndromo.
    
    Retorna:
    bool: True si la cadena es un palíndromo, False de lo contrario.
    """
    return frase == frase[::-1]

if __name__ == "__main__":
    # Solicita al usuario que ingrese una palabra o frase y la convierte a minúsculas
    palabra = input("Ingrese una palabra o frase: ").lower()
    
    # Verifica si la palabra o frase ingresada es un palíndromo y muestra un mensaje apropiado
    if es_palindromo(palabra):
        print("Es un palíndromo.")
    else:
        print("No es un palíndromo.")


