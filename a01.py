"""
1.	Elaborar un algoritmo que permita determinar si una persona es mayor de edad
o no a partir del ingreso de la edad, se presentar como resultado el mensaje respectivo
"""
edad = input("Ingrese edad: ")
if(float(edad) >= 18):
    print("Eres mayor de edad")
else:
    print("No eres mayor de edad")