#6. Sumar los primeros N números naturales: Pide al usuario un número entero positivo NNN y
#suma los primeros NNN números naturales usando un ciclo for.

print ("sumador de numeros")
na=int (input("ingrese 3 numeros:"))
r= 0
for i in range (1,na,+1):
    r += 1
    print (r)
print ("eso es toda la suma de los numeros")