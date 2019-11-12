"""
11.	Elaborar un algoritmo que a partir de tres números,  se determina cual es mayor, intermedio y menos de ellos
"""
numero1 = float(input("Ingrese primer numero: "))
numero2 = float(input("Ingrese segundo numero: "))
numero3 = float(input("Ingrese tercer numero: "))
temporal = 0
if(numero1 > numero2):
    temporal = numero1
    numero1 = numero2
    numero2 = temporal

if(numero1 > numero3):
    temporal = numero1
    numero1 = numero3
    numero3 = temporal

if(numero2 > numero3):
    temporal = numero2
    numero2 = numero3
    numero3 = temporal

print(f"Numero menor: {numero1}")
print(f"Numero medio: {numero2}")
print(f"Numero mayor: {numero3}")