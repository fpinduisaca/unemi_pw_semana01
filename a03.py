"""
3.	Realice un algoritmo que permita calificar una nota,
considerando que si la nota es menor a 69 suspenso, caso contrario aprobado
"""
nota = input("Ingrese nota: ")
if(float(nota) < 69):
    print("Suspenso")
else:
    print("Aprobado")