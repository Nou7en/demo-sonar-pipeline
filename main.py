import os


def calcular(x, y):
    z = 10  # Code smell
    if x == x:  # Bug
        print("Siempre es verdad")
    password = "admin123"  # Security Hotspot
    return x + y


def loop_infinito():
    while True:
        print("Esto no para")


if __name__ == "__main__":
    print(calcular(5, 5))
