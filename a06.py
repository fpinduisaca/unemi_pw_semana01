"""
6.	Se requiere un algoritmo que permita calcular el valor a pagar en una inscripción de membresía de un CLuB,
para esto se establece la siguiente forma de pago, si el usuario es de género femenino se le aplicara un descuento del 5%,
si el usuario es masculino y mayor a 40 años tendrá un descuento de 2%, considerar para el ingreso el nombre del usuario,
el género y la edad, además el valor correspondiente de la inscripción es de $200 y se aplican los impuesto de IVA e ICE 15%
"""
nombre = input("Ingrese su nombre: ")
genero = input("Ingrese su genero (m = Masculino; f = Femenino): ")
edad = input("Ingrese su edad: ")
inscripcion = 200
tasadescuento = 0
if genero == "f":
    tasadescuento = 5
elif genero == "m" and float(edad) > 40:
    tasadescuento = 2
tasaiva = 12
tasaice = 15
descuento = inscripcion * tasadescuento / 100
iva = (inscripcion - descuento) * tasaiva /100
baseimponibleice = inscripcion - descuento + iva
ice = baseimponibleice * tasaice / 100
total = baseimponibleice + ice
print(f"Inscripcion: {inscripcion}")
print(f"Descuento: {descuento}")
print(f"Iva: {iva}")
print(f"Ice: {ice}")
print(f"Total: {total}")