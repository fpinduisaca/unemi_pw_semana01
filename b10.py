"""
10.	Se requiere determinar el sueldo semanal de un trabajador con base en las horas que trabaja y el pago por hora que recibe.
Realice un algoritmo de solución correspondiente.
"""
horas_laboradas = float(input("Ingrese las horas laboradas: "))
pago_hora = float(input("Ingrese el pago por hora: "))
sueldo = horas_laboradas * pago_hora
print(f"Su sueldo es: {sueldo}")