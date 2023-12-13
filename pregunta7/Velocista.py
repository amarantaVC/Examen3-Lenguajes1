"""
CI3641 - LENGUAJES DE PROGRAMACION I
EXAMEN3 - PREGUNTA 7
AMARANTA VILLEGAS 16-11247
Velocista.py : programa que permita calcular valores para wadefoc(n) de la forma más
eficiente posible, para valores lo más grandes posibles de n.
"""
import time
from math import log2

def wadefoc(n):
    actual = 0
    sig = 1
    for i in range(n + 1):
        temp = actual
        actual = sig
        sig = sig + temp
    return actual

# Entrada del usuario
n = int(input("n: "))

inicio = time.time()
# Calcular logaritmo en base 2 y agregar 1 para redondear hacia arriba
log_valor = log2(wadefoc(n + 1)) + 1

final = time.time()
# Imprimir el resultado
print(wadefoc(int(log_valor)))

tiempo = round(final - inicio, 6)

print("\ntiempo:" , tiempo)