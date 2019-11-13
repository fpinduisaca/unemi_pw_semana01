"""
9.	Se requiere elaborar un algoritmo que permita determinar las horas asignadas de estudio
para los días LUNES, MARTES, MIÉRCOLES, JUEVES Y VIERNES, para cada día se asigna 7 horas de estudio
excepto para dos 2 días que son destinados para: descanso 2 horas menos de las planificadas de estudio,
el estudiante indicara en que días aplicara el descanso, y 3 horas a la semana menos destinadas
para realizar actividad física, el estudiante debe de indicar el día que va aplicar la actividad física,
a partir del ingreso de que días realizar estas actividades, presente cuantas horas tendrá asignado por cada día de la semana
"""
lunes = 7
martes = 7
miercoles = 7
jueves = 7
viernes = 7
descanso = int(input("Dia para descanso (1-5): "))
fisica = int(input("Dia para actividad fisica (1-5): "))
dias_descanso = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
dias_fisica = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
dias_descanso[descanso] = 2
dias_fisica[fisica] = 3
lunes -= (dias_descanso.get(1, 0) + dias_fisica.get(1, 0))
martes -= (dias_descanso.get(2, 0) + dias_fisica.get(2, 0))
miercoles -= (dias_descanso.get(3, 0) + dias_fisica.get(3, 0))
jueves -= (dias_descanso.get(4, 0) + dias_fisica.get(4, 0))
viernes -= (dias_descanso.get(5, 0) + dias_fisica.get(5, 0))
print(f"Lunes: {lunes}")
print(f"Martes: {martes}")
print(f"Miercoles: {miercoles}")
print(f"Jueves: {jueves}")
print(f"Viernes: {viernes}")