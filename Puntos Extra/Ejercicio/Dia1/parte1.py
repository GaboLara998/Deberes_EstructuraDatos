"""
1. La primera orden del día es averiguar qué tan rápido aumenta la profundidad, solo para saber con qué está lidiando: nunca se sabe si las llaves serán llevadas a aguas más profundas por una corriente oceánica o un pez o algo así.
Para hacer esto, cuente el número de veces que una medición de profundidad aumenta con respecto a la medición anterior. (No hay medición antes de la primera medición). En el ejemplo anterior, los cambios son los siguientes:

199 (N/A - no previous measurement)
200 (increased)
208 (increased)
210 (increased)
200 (decreased)
207 (increased)
240 (increased)
269 (increased)
260 (decreased)
263 (increased)

En este ejemplo, hay 7 medidas que son más grandes que la medida anterior
"""
almacenar_valores = []
medidas_mayores = 0

with open("/Users/gabri/iCloudDrive/Universidad/Quinto Semestre/Estructura de Datos/Puntos Extra/Ejercicio/Dia1/datos.txt","r") as datos:
    for i in datos.readlines():
            almacenar_valores.append(int(i.rstrip("\n")))
            
for i in range(len(almacenar_valores)):
    if almacenar_valores[i-1] < almacenar_valores[i]:
        medidas_mayores=medidas_mayores+1

print("medidas mas grandes que la medida anterior: ", medidas_mayores)
