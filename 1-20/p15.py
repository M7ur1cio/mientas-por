#5. Imprimir números impares: Pide al usuario un número entero positivo y muestra todos los
#números impares del 1 hasta ese número usando un ciclo for.

print ("imprimi numeros impares ")
n3= int (input ("ingrese un numero entero: "))
for i in range (1,n3,+1):
    n= n3 % 2
    print (i)
print ("esto son todos los numeros impares...")
        