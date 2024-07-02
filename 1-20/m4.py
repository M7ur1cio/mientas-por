#4. Sumar dígitos de un número: Pide al usuario un número entero y suma sus dígitos usando
# un ciclo while.

num = int(input("Ingresa un número entero: "))
suma = 0
    while num != 0:
        ud = num % 10
        su += ud
        num //= 10
    print(f"La suma de los dígitos es: {su}")