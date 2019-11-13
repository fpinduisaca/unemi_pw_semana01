"""
14.	Un usuario de un teléfono celular, requiere un algoritmo para determinar cuánto byte se consumieron en un chat
sostenido en una aplicación de mensajería, el algoritmo para calcular su resultado considerará 3 mensajes enviados
    a.	Mensaje 1: contiene un mensajes de 350 caracteres
    b.	Mensaje 2: contiene una imagen de 3 mb
    c.	Mensaje 3: contiene un video de 2.5 Mb más un texto de 200 caracteres
El resultado será mostrado en MB y byte, considerar que para cada carácter se ocupa 1 byte
"""
mensaje1 = 350
mensaje2 = 3 * 1024 * 1024
mensaje3 = ( 2.5 * 1024 * 1025 ) + 200
almacenamiento = mensaje1 + mensaje2 + mensaje3
mbytes = almacenamiento / (1024 * 1024)
print(f"Necesita {almacenamiento} bytes de espacio de almacenamiento")
print(f"Necesita {mbytes} MB de espacio de almacenamiento")