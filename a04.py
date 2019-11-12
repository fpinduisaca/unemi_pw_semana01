"""
4.	Realice un algoritmo para calcular el valor a pagar por una factura,
en donde  el consumo sea mayor a $100 tendrá un descuento del 2%
"""
cantidad = input("Cantidad: ")
precio = input("Precio unitario: ")
parcial = float(cantidad) * float(precio)
descuento = 0
if(parcial > 100):
    descuento = parcial * 2 / 100;
total = parcial - descuento
print(f"Parcial: {parcial}")
print(f"Descuento: {descuento}")
print(f"Total a pagar: {total}")