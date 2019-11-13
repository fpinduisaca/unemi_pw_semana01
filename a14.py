"""
14.	Elabore un algoritmo que desarrolla una trivial de preguntas:
•	PREGUNTA 1: Indique su género (Masculino/femenino)?
•	PREGUNTA 2: Indique su edad?
•	PREGUNTA 3: Indique si le gusta desvelarse por la madrugada(Si/No)?
	PREGUNTA1	PREGUNTA2	PEGUNTA3
MENSAJE	                        MASCULINO	FEMENINO	EDAD	SI	NO
Eres un Maestro!!	            X		                >18	    X
Eres una Maestra!!		                    X	        >18	    X
Eres un hijito de Mamá	        X		                <18		    X
Eres una hijita de Mamá		                X	        <18		    X
Eres una criatura de la noche	X	        X	        >18	    X
Cuídate mucho	                X	        X	        <18	    X

"""
genero = input("Indique su género (Masculino/femenino)? ")
edad = int(input("Indique su edad? "))
desvelarse = input("Indique si le gusta desvelarse por la madrugada(S/N)?")
mensaje = ""
if genero == "m" and edad > 18 and desvelarse == "s":
    mensaje = "Eres un maestro"
elif genero == "f" and edad > 18 and desvelarse == "s":
    mensaje = "Eres una maestra"
elif genero == "m" and edad < 18 and desvelarse == "n":
    mensaje = "Eres un hijito de mama"
elif genero == "f" and edad < 18 and desvelarse == "n":
    mensaje = "Eres una hijita de mama"
print(mensaje)
if desvelarse == "s":
    if edad > 18:
        mensaje = "Eres una criatura de la noche"
    else:
        mensaje = "Cuidate mucho"
print(mensaje)