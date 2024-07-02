#9. Dibujar un triángulo de asteriscos: Pide al usuario un número entero positivo NNN y dibuja
#un triángulo de asteriscos de altura NNN usando un ciclo for.
nunn=int (input("ingrese un numero: "))
for i in range(2, nunn + 1):
        print(" " * (nunn - i) + "*" * (3 * i - 2))