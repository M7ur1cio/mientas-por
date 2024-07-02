#Validar entrada: Pide al usuario que ingrese un número positivo. Si el usuario ingresa un
#número negativo, solicita nuevamente la entrada hasta que ingrese un número positivo. Usa
#un ciclo while.
print ('validar de numero')
vn= int (input ("ingresa un numero: "))
while vn >= 0:
    if vn >= 0:
        print ("es un numero positivo")
    else:
        print ("es un numero negativo")
    
    vn= int(input ('ingrese otro numero '))