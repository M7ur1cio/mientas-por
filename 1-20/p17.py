#7. Determinar si un número es primo: Pide al usuario un número entero positivo y determina si
#es primo usando un ciclo for.
print ("Numero primo")
nu=int(input("ingrese el numero:"))
nu2= (nu**0.5)+1
for i in range(nu) :
    if nu % i == 0:
        print(f"El número {nu} es primo")
    else:
        print(f"El número no es primo")