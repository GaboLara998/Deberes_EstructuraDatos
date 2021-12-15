""" 
Hydrothermal Venture
Parte 1
¡Te encuentras con un campo de respiraderos hidrotermales en el fondo del océano! Estos respiraderos producen 
constantemente nubes grandes y opacas, por lo que sería mejor evitarlos si es posible.

En este diagrama, la esquina superior izquierda es 0,0y la esquina inferior derecha es 9,9. 
Cada posición se muestra como el número de líneas que cubren ese punto o .si ninguna línea cubre ese punto. El par de 1s de arriba a la izquierda , por ejemplo, proviene de 2,2 -> 2,1; la misma fila inferior está formada por las líneas superpuestas 0,9 -> 5,9y 0,9 -> 2,9.
Para evitar las áreas más peligrosas, debe determinar el número de puntos donde se superponen al menos dos líneas . En el ejemplo anterior, se encuentra en cualquier parte del diagrama con un 2o más grande: un total de 5puntos.
Considere solo líneas horizontales y verticales. ¿En cuántos puntos se superponen al menos dos líneas?

Parte 2
Desafortunadamente, considerar solo las líneas horizontales y verticales no le da una imagen completa; también debe considerar las líneas diagonales .

Debido a los límites del sistema de mapeo de respiraderos hidrotermales, las líneas en su lista solo serán horizontales, verticales o diagonales a exactamente 45 grados.
Aún debe determinar el número de puntos donde se superponen al menos dos líneas . En el ejemplo anterior, todavía se encuentra en cualquier parte del diagrama con un 2o más grande, ahora un total de 12puntos.

Considere todas las líneas. ¿En cuántos puntos se superponen al menos dos líneas?
"""

def solucion(ingreso):
  with open("/Users/gabri/iCloudDrive/Universidad/Quinto Semestre/Estructura de Datos/Puntos Extra/Ejercicio/Dia5/entrada.txt","r") as datos:
    pasos=[list(map(int,linea.strip().replace("->",",").split(",")))for linea in datos]
    posicion_x=max(max([(i[0],i[2]) for i in pasos]))+1
    posicion_y=max(max([(j[1],j[3]) for j in pasos]))+1

  campo=[[0 for i in range(posicion_x)]for j in range(posicion_y)]

  for eje_x1,eje_y1,eje_x2,eje_y2 in pasos:
    pos_x1,x1=min(eje_x1,eje_x2), abs(eje_x2-eje_x1)
    pos_y1,y1=min(eje_y1,eje_y2), abs(eje_y2-eje_y1)
    if eje_x1==eje_x2:
      for i in range(y1 +1):
        campo[i+pos_y1][eje_x1] += 1
    elif eje_y1== eje_y2:
      for i in range(x1+1):
        campo[eje_y1][i+pos_x1] +=1
    elif ingreso:
      pos1=1 if eje_x2>eje_x1 else -1
      pos2=1 if eje_y2>eje_y1 else -1
      for i in range(x1+1):
        campo[pos2*i+eje_y1][pos1*i + eje_x1] +=1
  return sum([1 for i in campo for j in i if j>1])

R1=solucion(0)
print("Sol1=",R1)      

R2=solucion(1)
print("Sol2=",R2)      
          