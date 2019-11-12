"""
9.	Un productor de leche lleva el registro de lo que produce en litros, pero cuando entrega el producto le pagan en galones.
Realice un algoritmo, que ayude al productor a saber cuánto recibirá por la entrega de su producción de un día
(1 galón = 3.785 litros).
"""
litros = float(input("Total litros producidos:"))
galones = litros / 3.785
print(f"Galones producidos: {galones}")
