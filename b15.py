"""
15.	Elabore un algoritmo que permita a partir de la estatura, peso y género,
calcular el peso ideal que debería tener la persona, realizar la investigación para establecer este cálculo,
si en su investigación requiere un dato adicional de ingreso, el mismo lo puede considerar como entrada
"""
peso = float(input("Ingrese su peso (Kg): "))
estatura = float(input("Ingrese su estatura (mts): "))
genero = input("Ingrese genero (m = masculino; f = femenino): ")
if estatura == 0:
    print("Estatura no puede ser cero.")
else:
    imc = peso / (estatura ** 2)
    if imc < 18.5:
        print("Bajo peso")
    elif imc < 25:
        print("Peso normal")
    elif imc < 30:
        print("Sobrepeso")
    elif imc < 35:
        print("Obesidad grado I")
    elif imc < 40:
        print("Obesidad grado II")
    else:
        print("Obesidad mórbida")