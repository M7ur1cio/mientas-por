#Adivinar un número: Escribe un programa que elija un número aleatorio entre 1 y 10 y
#permita al usuario adivinarlo, dándole pistas de "mayor" o "menor" hasta que acierte. Usa un
#ciclo while.
import random
n= random.randint (1,10)
print ('adivina un numero')
nu= int (input('ingresa un numero '))
while nu != n:
    if nu < n:
        print ('es mayor')
    else:
        print ('es muy menor')
    nu= int (input('de nuevo '))
print ('ese es el numero corrector',nu)
        