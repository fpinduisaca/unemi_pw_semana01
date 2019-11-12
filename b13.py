"""
13.	Pinturas “La brocha gorda” requiere determinar cuánto cobrar por trabajos de pintura.
Considere que se cobra por m2, el usuario ingresa los metros cuadrados del trabajo que va a realizar y el valor por m2,
realice un algoritmo que le permita al local elaborar unos presupuestos para cada cliente.
"""
valor_m2 = float(input("Ingrese valor del m2: "))
area = float(input("Ingrese area a pintar (m2): "))
costo = valor_m2 * area
print(f"El valor a cobrar es: {costo}")