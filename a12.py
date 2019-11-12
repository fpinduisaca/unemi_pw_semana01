"""
12.	Un comerciante requiere calcular el valor a pagar por sus clientes, considerando
que se conoce el valor a pagar y se debe de calcular el 3% de descuento de compras mayores a $2000
"""
valor_pagar = float(input("Ingrese valor pagar: "))
descuento = 0
if valor_pagar > 2000:
    descuento = valor_pagar * 3 / 100
total_pagar = valor_pagar - descuento
print(f"Descuento realizado: {descuento}")
print(f"Total a pagar es: {total_pagar}")