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


    