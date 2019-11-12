"""
10.	Elaborar un algoritmo que a partir de dos números,  se determina cuál es mayor y cuál es menor.
"""
numero1 = float(input("Ingrese primer numero: "))
numero2 = float(input("Ingrese segundo numero: "))
if numero1 > numero2:
    print(f"Mayor: {numero1} Menor: {numero2}")
else:
    print(f"Mayor: {numero2} Menor: {numero1}")