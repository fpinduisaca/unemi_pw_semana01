"""
13.	Se ingresa la edad y el género de un usuario, se requiere un algoritmo que permita presentar un mensaje
considerando la siguiente combinación de valores según las variables ingresadas:
GENERO
MASCULINO	FEMENINO	EDAD	MENSAJE
X	        	        >18	    YA ERES UN SEÑOR
X		                <18	    AUN ERES UN HIJITO DE MAMÁ
	        X	        >18	    YA ERES UN ADULTO
	        X	        <18	    AUN ERES UNA HIJITA DE MAMÁ

"""
edad = int(input("Ingrese edad: "))
genero = input("Ingrese genero (m = Masculino, f = femenino)")
if genero == "m":
    if edad > 18:
        print("Ya eres un señor")
    else:
        print("Aun eres un hijo de mama")
else:
    if edad > 18:
        print("Ya eres un adulto")
    else:
        print("Aun eres una hijita de mama")