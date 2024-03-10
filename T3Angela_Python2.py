"""Escribir un programa que almacene palabras ingresadas por el usuario. Debe recibir 
ingreso de palabras hasta que el usuario ingrese tres asteriscos ***. Luego de esto, las 
palabras se deben mostrar por pantalla una única vez. Es decir que, si el usuario ingresó
palabras repetidas, se deben mostrar solo una vez. """

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

