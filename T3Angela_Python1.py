# Ejercicio 1 
"""Escribir un programa que lea entre 10 a 20 números ingresados por el usuario, los 
almacene en una lista y los muestre ordenados de mayor o menor. Debe recibir el ingreso 
de números hasta que el usuario ingrese 0. Pero el 0 no se debe mostrar en pantalla."""
#Imprima el nombre y numero del ejercicio
print("Ejercicio 1: ")
print()

def main():
    numeros = []

    print("Ingresa numeros. (presiona 0 para dejar el programa): ")

    while True:

        try:
            numero = int(input("Ingresa un numero (presiona 0 para dejar el programa): "))

            #si el numero es 0, se debe romper el ciclo

            if numero == 0:
                break

            numeros.append(numero)

            if len (numeros) > 20:
                print("El ingreso de números sobrepasa los 20 números.")
                break
        except ValueError:
            print("Por favor, ingresa un numero correcto")

    if len (numeros) < 10:
        print("No has ingresado suficientes numeros. Se requiere al menos 10")
        return
    
    
    numeros.sort(reverse=True)

    print("\nNúmeros ordenados de mayor a menor: ")
    for num in numeros:
        print(num)

if __name__ == "__main__":
    main()
    


#Ejercicio 2
"""Escribir un programa que almacene palabras ingresadas por el usuario. Debe recibir 
ingreso de palabras hasta que el usuario ingrese tres asteriscos ***. Luego de esto, las 
palabras se deben mostrar por pantalla una única vez. Es decir que, si el usuario ingresó
palabras repetidas, se deben mostrar solo una vez. """

#Imprima el nombre y numero del ejercicio
print("Ejercicio 2: ")
print()
# Crear un conjunto para ingresar palabras

palabras =set()

while True:
    palabra = input ("Ingresa cualquier palabra en el programa, si deseas salir presion 3 asteriscos ***: ")

    if palabra == "***":
        break
#Se deben eliminar las palabras repetidas y se agregan al conjunto las palabras
palabras.add(palabra)
print("Las palabras ingresadas son:")
print()

#Listar las palabras individualmente
for palabra in palabras:


# Imprimir cada palabra del conjunto 
    print(palabra)
    print()


#Ejercicio 3
#Imprima el nombre y numero del ejercicio
print("Ejercicio 3: ")
print()

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


#Ejercicio 4
#Imprima el nombre y numero del ejercicio
print("Ejercicio 4: ")
print()
    # El programa debe leer palabras iguales de izquierda a derecha o al reves
# Cnstruir un programa que determine si dos palabras ingresadas por el usuario son 
# anagramas.

# Definir la funcion principal 

def esanagrama(palabra):
    #la ruta no aporto otro paso natural
    #larutanosaportootropasonatural
    palabra = palabra.lower() # la ruta nos aportó otro paso natural
    palabra = palabra.replace(" ", "") #larutanosaportootropasonatural
    palabra = palabra.replace("á","a") #larutanosaportootropasonatural
    palabra = palabra.replace("é","e") #larutanosaportootropasonatural
    palabra = palabra.replace("í","i") #larutanosaportootropasonatural
    palabra = palabra.replace("ó","o") #larutanosaportootropasonatural
    palabra = palabra.replace("ú","u") #larutanosaportootropasonatrual

    # larutanosaportootropasonatural
    # 012...
    # n = largo de la frase - 1
    # oso
    
# Utilizar un bucle for y que el retorno sea verdadedor o falso
    a = 0
    b = len(palabra) - 1

    for i in range(0, len(palabra)):
        if palabra[a] == palabra[b]:
            a += 1
            b -= 1
        else:
            return False
    
    return True

# Ingresar datos y que realice la impresión del Anagrama

palabra = input("Ingrese una palabra o una frase: ")
print(esanagrama(palabra))

if esanagrama(palabra):
    print("Es una palabra o frase Anagrama")
else:
    print("No es una palabra o frase Anagrama")


#Ejercio 5
"""Construir un programa en donde el usuario ingrese número por pantalla y el programa devuelva la suma de cada número ingresado por el usuario.
Si el usuario ingresa un carácter no numérico, debe mostrar mensaje de error y continuar solicitando números y sumando. 
El programa finaliza cuando usuario presiona enter con espacio en blanco."""

#Imprima el nombre y numero del ejercicio
print("Ejercicio 5: ")
print()

#Definir la función principal

def main():
    
    suma = 0
    
    # Iniciar un ciclo while
    while True:
        numero = input("Ingrese un numero (Presione enter para terminar): ")
        # Presionar Enter para detener el proceso
        if numero == "":
            break
        
        try:
            suma += float(numero)
        # Debe aparecer un mensaje de error si se ingresa un caracter no numérico
        except ValueError:
            print("Eso no corresponde a un número, por favor intente de nuevamente.")
    
    # Debe imprimir el valor de la suma de los números ingresados
    print(f"La suma de los números ingresados corresponde a: {suma} .")
            
# Debe llamar a la función principal del ejercicio
if __name__ == "__main__":
    main()  
