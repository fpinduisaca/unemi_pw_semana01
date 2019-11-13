"""
8.	Un médico indica a su paciente que deberá guardar reposo por 30 días, su peso es de 70 kg,
se encuentra en reposo y desea saber cuántas calorías consume su cuerpo durante todo el tiempo
que realice una misma actividad. Las actividades que tiene permitido realizar por estos 30 días
son únicamente dormir o estar sentado en reposo. Los datos que tiene son cuantas horas ha estado durmiendo
y consumio 1.08 calorías x minuto y el tiempo de haber estado sentado en reposo que consumio 1.66 calorías por minuto,
realice las consultas necesario para determinar cómo se trasnforma esas calorías en el incremento de peso
y presente el peso que incremento en eso 30 dias, considerar que los datos expuesto son solo de ejemplo,
el algortimo que realice deberá solicitar eso datos para el calculo.
"""
actividad = input("indique la actividad del paciente:")
tiempo = input("ingrese el tiempo que toma el paciente:")
calorías = 0
if actividad == "dormir":
    calorías = 1.08 * tiempo
elif actividad == "sentado":
    calorías = 1.66 * tiempo
print(f"el paciente consume {calorías} calorías");