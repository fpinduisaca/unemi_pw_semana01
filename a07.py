"""
7.	Realizar un algoritmo que permita calcular el valor a pagar a un empleado, considerando que
para el cálculo se requiere el número de horas trabajadas, que no podrán ser mayor a 40 horas semanales,
por lo que se ingresará el número de horas trabajadas por cada semana y que corresponde a 4 semanas  de trabajo,
por cada hora trabajada se le paga $4, además se establecerá el cálculo de horas extras que no podrá superar a 15 horas semanales
por las 4 semanas de trabajo, para ello se conocerá cuantas horas extras realizo en las 4 semanas de trabajo mensual,
por cada hora extra se cancelara $3
"""
horas_laboradas = float(input("Ingrese numero de horas laboradas en el mes: "))
horas_extras = float(input("Ingrese numero de horas extras laboradas en el mes: "))

if horas_laboradas > 160:
    horas_laboradas = 160
if horas_extras > 60:
    horas_extras = 60
sueldo_base = horas_laboradas * 4
sueldo_extra = horas_extras * 3
sueldo = sueldo_base + sueldo_extra
print(f"Sueldo base: {sueldo_base}")
print(f"Sueldo extra: {sueldo_extra}")
print(f"Sueldo a recibir: {sueldo}")