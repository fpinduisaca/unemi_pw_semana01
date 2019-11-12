"""
8.	Elaborar un algoritmo que a partir de ingreso del nombre del usuario y el género, presente un mensaje según la siguiente tabla
Genero 	    Mensaje
Masculino	Saludos <<NOMBRE>>
Femenino	Buenos días <<NOMBRE>>

"""
nombre = input("Ingrese su nombre: ")
genero = input("Ingrese su genero (m = Masculino; f = Femenino): ")
if genero == "m":
    print(f"Saludos {nombre}")
elif genero == "f":
    print(f"Buenos dias {nombre}")
else:
    print("Genero ingresado incorrecto.")