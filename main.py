import os


def calcular(x, y):
    # Variable no usada (Code Smell)
    z = 10

    # Comparación inútil (Bug)
    if x == x:
        print("Siempre es verdad")

    # Contraseña hardcodeada (Vulnerabilidad de seguridad)
    password = "admin123"

    return x + y


def loop_infinito():
    # Loop infinito potencial (Bug)
    while True:
        print("Esto no para")


print(calcular(5, 5))
