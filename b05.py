"""
5.	Se requiere elaborar un algortimo que permita presentar como resultado el perímetro de un terreno cuadro,
en donde se ingresa la medida de 2 de sus lados
"""
lado1 = float(input("Ingrese el valor del primer lado: "))
lado2 = float(input("Ingrese el valor del segundo lado: "))
perimetro = 2 * (lado1 + lado2)
print(f"El perimetro del terreno es: {perimetro}")