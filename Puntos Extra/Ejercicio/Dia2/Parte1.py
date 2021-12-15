"""
Parece que el submarino puede tomar una serie de comandos como forward 1, down 2o up 3:

forward Xaumenta la posición horizontal en Xunidades.
down X aumenta la profundidad en Xunidades.
up X disminuye la profundidad en Xunidades.

Su posición horizontal y profundidad comienzan en 0. Los pasos anteriores los modificarían de la siguiente manera:

forward 5agrega 5a su posición horizontal, un total de 5.
down 5agrega 5a su profundidad, resultando en un valor de 5.
forward 8agrega 8a su posición horizontal, un total de 13.
up 3disminuye la profundidad en 3, lo que da como resultado un valor de 2.
down 8agrega 8a su profundidad, resultando en un valor de 10.
forward 2agrega 2a su posición horizontal, un total de 15.

Calcula la posición horizontal y la profundidad que tendrías después de seguir el rumbo planificado. 
¿Qué obtienes si multiplicas tu posición horizontal final por tu profundidad final?

"""
pos_Horizontal=0
profundidad=0


with open("/Users/gabri/iCloudDrive/Universidad/Quinto Semestre/Estructura de Datos/Puntos Extra/Ejercicio/Dia2/input1.txt","r") as datos:
  pasos=[i.rstrip() for i in datos]
    
for i in pasos:
    direccion,distancia=i.split(" ")
    distancia=int(distancia)
    if direccion=="forward":
        pos_Horizontal+=distancia
    elif direccion== "up":
        profundidad-=distancia
    elif direccion== "down":
        profundidad+=distancia
        
print("profundidad",pos_Horizontal*profundidad)        