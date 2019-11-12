"""
6.	Un usuario requiere un algoritmo para determinar cuánto espacio ocuparan 3 videos
que se encuentran almacenados en 3 dispositivos distintos,
    a.	Para el primer video, el dispositivo presenta la información de almacenamiento en Kbyte
    b.	Para el según video, el dispositivo presenta la información de almacenamiento en Mbyte
    c.	Para el tercer video, el dispositivo presenta la información de almacenamiento en byte
    Cuanto es el total de espacio que ocuparían estos archivos video medidos en Kbyte, Mbyte y byte  
"""
video1 = float(input("Almacenamiento del primer video (Kbyte): "))
video2 = float(input("Almacenamiento del segundo video (Mbyte): "))
video3 = float(input("Almacenamiento del tercer video (byte): "))
bytes = (video1 * 1024) + (video2 * 1024 * 1024) + video3
kbytes = bytes / 1024
mbytes = kbytes / 1024
print(f"Espacio ocupado en bytes: {bytes}")
print(f"Espacio ocupado en Kbytes: {kbytes}")
print(f"Espacio ocupado en Mbytes: {mbytes}")