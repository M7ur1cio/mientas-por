#1. Tabla de multiplicar: Pide al usuario un número entero positivo y muestra su tabla de
#multiplicar del 1 al 10 usando un ciclo for.
print ('tabla de multiplicación')
nn= int (input("ingrese un numero entero: "))
for i in [1,2,3,4,5,6,7,8,9,10]:
    por=nn*i
    print (f"multiplicacion de {nn} * {i} = {por}")
print ("eso es todo...")