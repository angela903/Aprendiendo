""" Crear un programa que determine si una contraseña en segura o no. Se considera segura 
si tiene al menos una mayúscula, una minúscula y un número. Se debe utilizar funciones."""

print("Ejercicio 1 Crear una contraseña segura: ")
print()

#Definir las variables

def comprobarContrasena(password):
    largo = False
    mayus = False
    numer = False

#Utilizar condicionales
    if len(password) > 8:
        largo = True
    for i in range(len(password)):
        if password[i].isupper():
            mayus = True
        if password[i].isnumeric():
            numer = True


#Una constraseña es segura si cuenta con mayuscula y numeros

    if largo and mayus and numer:
        return True
    else:
        return False
    
#Que imprima ingresar una contraseña segura
password = input("Ingresa una contraseña segura: ")
verificacion = comprobarContrasena(password)
if verificacion:
    print("La contraseña es segura")
else:
    print("La contraseña no es segura")

""" Escribir un programa que lea números ingresados y luego devuelva el total. Se debe 
desarrollar usando recursión. No se pueden utilizar ciclos. Se ingresar números hasta que 
el usuario ingrese un espacio. Si el primer input es un espacio, entonces imprime 0. """

print("Ejercicio 2 Escribir un programa que lea números sin utilizar ciclos: ")
print()

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
    

"""Crear una clase llamada “cuenta”. Al instanciar la clase se debe proveer el número de 
cuenta, el nombre el titular, saldo inicial, tipo cuenta (ahorro, corriente, inversiones). Crear 
tres métodos depositar, retirar, obtener balance. Si en la cuenta1 hay un saldo inicial de 
10 y se hace un depósito de 20 y un retiro de 5, entonces al obtener el balance debe 
mostrar un saldo de 25. Imprimir la información con todos los datos de usuarios y 
balances"""

print("Ejercicio 3 Crear una clase llamada cuenta: ")
print()
class Cuenta:
    def __init__(self, num_cuenta, nom_titular, saldo_inicial, tipo_cuenta):
        self.num_cuenta = num_cuenta;
        self.nom_titular = nom_titular;
        self.saldo = saldo_inicial;
        self.tipo_cuenta = tipo_cuenta;

# Ingresar datos por consola
num_cuenta = input("Ingrese su número de cuenta: ");
nom_titular = input("Ingrese el nombre del titular: ");
saldo = float(input("Ingrese el saldo inicial: "));
tipo_cuenta = input("Ingrese el tipo de cuenta: ");

cuenta1 = Cuenta(num_cuenta, nom_titular, saldo, tipo_cuenta);

# Debe entregar 3 consultas, el balance, deposito, retiro
class Cajero:
    monto=2000000
    print('Bienvenido a su banco')
    def operaciones(self):
        self.opcion = int(input('''
        ------------------------------
        por favor indique que operacion desde realizar..
        1. Consultar balance
        2. Deposito a cuenta
        3. Retiro de efectivo
        4. Salir'''))

# Crear las funciones
        
        self.control=0
        while self.control==0:
            if self.opcion==1:
                self.consultabalance()
            elif self.opcion==2:
                self.depositar()
            elif self.opcion==3:
                self.retirar()
            elif self.opcion==4:
                self.control=1
                self.salir()
            else:
                print('Lo sentimos opcion no valida!, intente de nuevo.. ')
                self.operaciones()

    def consultabalance(self):
        print('Su balance disponible es: ', self.monto)
        print('Desea realizar otra operación?')
        self.operaciones()

    def depositar(self):
        self.deposito = int(input('Indique la cantidad que desea depositar..'))
        self.monto=self.monto + self.deposito
        self.consultabalance()

    def retirar(self):
        self.retiro = int(input('Indique la cantidad que desea retirar..'))
        self.control =0
        while self.control==0:
            if self.retiro > self.monto:
                print('''Usted no posee fondos suficientes para este 
                retiro por favor intente de nuevo...
                ---------------------------''')
                self.retiro = int(input('Indique la cantidad que desea retirar..'))
            elif self.retiro<= self.monto:
                self.monto=self.monto-self.retiro
        self.control=1
        print('Cantidad retirada: ', self.retiro)
        self.consultabalance()

    
def salir(self):    
    print('==========================================')
    print('Gracias por usar nuestros servicios!')
    print('==========================================')

ejecucion = Cajero()
ejecucion.operaciones()
    