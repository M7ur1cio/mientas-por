#10.Simular un cajero automático: Escribe un programa que simule un cajero automático. Pide
#al usuario que ingrese su PIN y permite tres intentos para ingresarlo correctamente. Si no lo
#hace en tres intentos, muestra un mensaje de bloqueo. Usa un ciclo while

print ('cajero automatico.com \n')
contra=12345
con2= int(input('ingrese el PIN: '))
contac= 1

while contac <= 3:
    contac += 1
    if con2 == contra:
        print ('PIN correcto')
    elif con2 != contra:
        print('error de PIN')
        con2=int(input("ingrese PIN: "))
        
print ('demasiado intento')