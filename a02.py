"""
2.	Realice un algoritmo que calcule la suma de dos números positivos,
aplicar la validación que ambos números sean positivos, caso contrario
no se puede realizar la suma
"""
num1 = input("Ingrese primer numero: ")
num2 = input("Ingrese segundo numero: ")
if(float(num1) > 0 and float(num2) > 0):
    print(f"La suma de los dos numeros es: {float(num1) + float(num2)}")
else:
    print("Los dos numeros ingresados deben ser positivos.")