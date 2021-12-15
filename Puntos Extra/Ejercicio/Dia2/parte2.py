"""
el objetivo , que también comienza en 0. Los comandos también significan algo completamente diferente de lo que pensaba al principio:

down X aumenta tu puntería por Xunidades.
up X disminuye tu puntería por Xunidades.
forward X hace dos cosas:
Aumenta tu posición horizontal en Xunidades.
Aumenta tu profundidad por tu puntería multiplicada por X .

forward 5agrega 5a su posición horizontal, un total de 5. Porque tu objetivo es 0, tu profundidad no cambia.
down 5se suma 5a su objetivo, lo que da como resultado un valor de 5.
forward 8agrega 8a su posición horizontal, un total de 13. Porque tu objetivo es 5, tu profundidad aumenta en 8*5=40.
up 3disminuye su puntería en 3, lo que da como resultado un valor de 2.
down 8se suma 8a su objetivo, lo que da como resultado un valor de 10.
forward 2agrega 2a su posición horizontal, un total de 15. Debido a que su objetivo es 10, su profundidad aumenta 2*10=20hasta un total de 60.

Después de seguir estas nuevas instrucciones, tendrá una posición horizontal 15y una profundidad de 60. (Multiplicar estos produce 900).
Con esta nueva interpretación de los comandos, calcule la posición horizontal y la profundidad que tendría después de seguir el rumbo planificado. 
¿Qué obtienes si multiplicas tu posición horizontal final por tu profundidad final?

"""

pos_Horizontal=0
profundidad=0
temp1=0

with open("/Users/gabri/iCloudDrive/Universidad/Quinto Semestre/Estructura de Datos/Puntos Extra/Ejercicio/Dia2/input1.txt","r") as datos:
  pasos=[i.rstrip() for i in datos]
  
for i in pasos:
    direccion,distancia=i.split(" ")
    distancia=int(distancia)
    if direccion=="forward":
        pos_Horizontal+=distancia
        profundidad+=temp1*distancia
    elif direccion == "up":
        temp1-=distancia
    elif direccion == "down":
        temp1+=distancia
print("pos horizontal final:", pos_Horizontal*profundidad)            