"""  
Los sensores indican un enorme sistema de cuevas subterráneas justo más allá de donde apuntan.
Rápidamente haces una lista de la posición horizontal de cada cangrejo (tu entrada del rompecabezas). Los submarinos cangrejo tienen combustible limitado, 
por lo que debe encontrar una manera de hacer que todas sus posiciones horizontales coincidan mientras requieren que gasten la menor cantidad de combustible posible.

Por ejemplo, considere las siguientes posiciones horizontales:

16,1,2,0,4,2,7,1,2,14
Esto significa que hay un cangrejo en posición horizontal 16, un cangrejo en posición horizontal 1, etc

Cada cambio de 1 paso en la posición horizontal de un solo cangrejo cuesta 1 combustible. 
Puede elegir cualquier posición horizontal para alinearlos todos, pero la que cuesta menos combustible es la posición horizontal 2:

Mover de 16a 2: 14combustible
Mover de 1a 2: 1combustible
Mover de 2a 2: 0combustible
Mover de 0a 2: 2combustible
Mover de 4a 2: 2combustible
Mover de 2a 2: 0combustible
Mover de 7a 2: 5combustible
Mover de 1a 2: 1combustible
Mover de 2a 2: 0combustible
Mover de 14a 2: 12combustible
Esto cuesta un total de 37combustible. Este es el resultado más económico posible; 
Los resultados más costosos incluyen la alineación en la posición 1( 41combustible), la posición 3( 39combustible) o la posición 10( 71combustible).

Determina la posición horizontal en la que los cangrejos pueden alinearse usando la menor cantidad de combustible posible. 
¿Cuánto combustible deben gastar para alinearse en esa posición?

Parte 2:
Resulta que los motores de los submarinos cangrejo no queman combustible a un ritmo constante . 
En cambio, cada cambio de 1 paso en la posición horizontal cuesta 1 unidad más de combustible que el último: 
el primer paso cuesta 1, el segundo paso cuesta 2, el tercer paso cuesta 3, etc.

A medida que cada cangrejo se mueve, moverse más lejos se vuelve más costoso. 
Esto cambia la mejor posición horizontal para alinearlos todos; en el ejemplo anterior, esto se convierte en 5:

Mover de 16a 5: 66combustible
Mover de 1a 5: 10combustible
Mover de 2a 5: 6combustible
Mover de 0a 5: 15combustible
Mover de 4a 5: 1combustible
Mover de 2a 5: 6combustible
Mover de 7a 5: 3combustible
Mover de 1a 5: 10combustible
Mover de 2a 5: 6combustible
Mover de 14a 5: 45combustible

Esto cuesta un total de 168combustible. Este es el nuevo resultado más económico posible; la posición de alineación anterior ( 2) ahora cuesta 206combustible.

¡Determina la posición horizontal en la que los cangrejos pueden alinearse usando la menor cantidad de combustible posible para que puedan convertirte en una ruta de escape! 
¿Cuánto combustible deben gastar para alinearse en esa posición?
"""
import math
parte1 = float(math.inf)
parte2 = float(math.inf)
with open("/Users/gabri/iCloudDrive/Universidad/Quinto Semestre/Estructura de Datos/Puntos Extra/Ejercicio/Dia7/entrada.txt","r") as datos:
    pasos = [int(x) for x in datos.read().strip().split(',')]
    
for y in range(min(pasos),max(pasos)):
    parte1 = min(parte1,sum([abs(x-y) for x in pasos]))
print(parte1)

for y in range(min(pasos),max(pasos)):
    parte2 = min(parte2,sum([(abs(x-y)*(abs(x-y)+1)//2) for x in pasos]))
print(parte2)