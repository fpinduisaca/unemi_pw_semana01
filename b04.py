"""
4.	Elabore un algoritmo que permita ingresar dos números y calcule su división, presentando el resultado
"""
numero1 = float(input("Ingrese primer numero: "))
numero2 = float(input("Ingrese segundo numero: "))
if numero2 == 0:
    print("No se puede realizar la division por cero.")
else:
    division = numero1 / numero2
    print(f"La division de los numeros es: {division}")