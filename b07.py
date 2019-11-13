"""
7.	Una arquitecto requiere un algortimo para calcular cual el área  de una pared que  requiere ser pintada,
para esto tiene 3 mediciones realizadas por 3 pintores diferentes, Jose  uno de los pintores tomo como medida 70 m2,
Pedro en su medición  tomo un valor de  1500 cm2 y Juan tomo la medida de 2000 pulgadas2, presentar la respuesta en m2 y cm2
"""
medida1 = 70 #m2
medida2 = 1500 #cm2
medida3 = 2000 #pulgadas2
m1 = medida1
m2 = medida2 / 10000
m3 = medida3 / 1550
cm1 = medida1 * 10000
cm2 = medida2
cm3 = medida3 * 6.4516
print(f"m2 =  {m1} | {m2} | {m3}")
print(f"cm2 =  {cm1} | {cm2} | {cm3}")