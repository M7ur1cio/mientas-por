#9. Convertir de decimal a binario: Pide al usuario un número entero positivo y convierte ese
#número a binario usando un ciclo while.

print ('convertidor de decimal a binario')
c1= int(input ('ingrese un numero entero: '))
conver= bin(c1)
while c1 >= 0:
    print (f'en binario seria así: {conver}')
    c1= int(input ('ingrese otro numero entero: '))
    