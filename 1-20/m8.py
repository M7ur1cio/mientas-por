#8. Contador de dígitos: Pide al usuario un número entero y cuenta cuántos dígitos tiene usando
#un ciclo while.
print ('contador de digitos')
n= int (input ('ingresa un numero entero: '))
r= len(str(n))

while n >= 0:
    print ('el numero que ingreso tiene un digito de ',r )
    n= int (input ('ingresa un numero entero: '))