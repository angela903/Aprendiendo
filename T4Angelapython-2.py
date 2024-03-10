""" Escribir un programa que lea números ingresados y luego devuelva el total. Se debe 
desarrollar usando recursión. No se pueden utilizar ciclos. Se ingresar números hasta que 
el usuario ingrese un espacio. Si el primer input es un espacio, entonces imprime 0. """

#función recursiva que recibe numeros y los suma, al presionar la tecla entre entregue un resultado
"""def suma_recursiva():
    #entrada de usuario para los numeros
    entrada = input("Ingrese un número para sumar, y un enter para totalizar y salir del sistema: ");

    # Al ingresar la tecla enter que retorne un 0.
   
    if entrada == "":  
        return 0;
    else:
        try:
            #número a float, por si ingresan un decimal (un decimal es un número)
            numero = float(entrada);
            #retorna el numero y se llama a si misma para seguir sumando la entrada a número
            return numero + suma_recursiva();
        except ValueError: # si no ingresa un número, valida que la suma no funciono y se vuelve a llamar a si misma
            print("Entrada inválida. Ingrese un número válido.");
            return suma_recursiva();

#asigno el valor de la suma recursiva al total
total = suma_recursiva();
#imprimo el total por consola
print("La suma total es:", total);"""

#Fibonacci

def Fibonacci(numero):
    if(numero == 0 or numero == 1):
        return 1
    
    else:
        return Fibonacci(numero - 1) + Fibonacci(numero - 2)
    
while True:
        n = int(input("Ingrese un numero: "))

        if(n >= 1):
            break

for i in range(n):
    print(Fibonacci(i))
    


    

