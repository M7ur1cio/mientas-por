#6. Mostrar múltiplos de un número: Pide al usuario un número entero positivo y muestra sus
#múltiplos del 1 al 10 usando un ciclo while
print ('multipos')
n1= int (input('ingrese un numero:'))
n2= 1
while n2 <= 10:
    ml = n1*n2
    n2 += 1
    print (f'resultado de multiplo {n1} es {ml}')
