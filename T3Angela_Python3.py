""" ¡Juguemos Scrabble!
Construir un diccionario con los siguientes valores. Luego, el usuario ingresa una palabra 
por pantalla, y el programa devuelve el puntaje.
"""

print("¡Empezar a jugar Scrabble!")
print()

#Define la funcion para dar puntaje a las palabras

def obtiene_puntuacion(palabra):

# Construye un diccionario como el del ejemplo dando y putuacion a cada letra

    valores = {

        1: [ 'A', 'E', 'I', 'L', 'N', 'O', 'R', 'S', 'T', 'U'],

        2: ['D', 'G'],

        3: ['B', 'C', 'M', 'P'],

        4: ['F', 'H', 'V', 'W', 'Y'],

        5: ['K'],

        8: ['J', 'X'],

        10: ['Q', 'Z']}

    # Crea el diccionario que muestre la puntuacion que corresponde a cada letra
    diccionario_scrabble = {letra: puntuacion for puntuacion, letras in valores.items () for letra in letras}
    
    puntuacion = sum(diccionario_scrabble.get(letra.upper(), 0) for letra in palabra)
    return puntuacion

#Definir la función principal

def main ():

    palabra = input("ingrese una palabra: ")

    puntuacion = obtiene_puntuacion(palabra)

    print(f"La puntuacion para '{palabra}' es: {puntuacion}" )


# Debe llamar a la funcion principal
if __name__ == "__main__":
    main()
    print()


