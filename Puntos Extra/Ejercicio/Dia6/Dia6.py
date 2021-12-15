"""
parte1:
demás, razona, un nuevo pez linterna seguramente necesitaría un poco más de tiempo antes de que sea capaz de producir más peces linterna: dos días más para su primer ciclo.

Entonces, suponga que tiene un pez linterna con un valor de temporizador interno de 3:

Después de un día, su temporizador interno se convertiría en 2.
Después de otro día, su temporizador interno se convertiría en 1.
Después de otro día, su temporizador interno se convertiría en 0.
Después de otro día, su temporizador interno se restablecería 6y crearía un nuevo pez linterna con un temporizador interno de 8.
Después de otro día, el primer pez linterna tendría un temporizador interno de 5y el segundo pez linterna tendría un temporizador interno de 7.

Cada día, a se 0convierte en 6ay agrega uno nuevo 8al final de la lista, mientras que cada uno de los otros números disminuye en 1 si estaba presente al comienzo del día.

En este ejemplo, después de 18 días, hay un total de 26peces. Después de 80 días, habría un total de 5934.

Encuentra una manera de simular un pez linterna. ¿Cuántos peces linterna habría después de 80 días?



parte2:

Suppose the lanternfish live forever and have unlimited food and space. Would they take over the entire ocean?

After 256 days in the example above, there would be a total of 26984457539 lanternfish!

How many lanternfish would there be after 256 days?
"""

  
with open("/Users/gabri/iCloudDrive/Universidad/Quinto Semestre/Estructura de Datos/Puntos Extra/Ejercicio/Dia6/entrada.txt","r") as datos:
  pasos=list(map(int, datos.read().split(",")))
  
def peces_linterna(days):
    crecimiento = [[int(k.strip()) for k in open("/Users/gabri/iCloudDrive/Universidad/Quinto Semestre/Estructura de Datos/Puntos Extra/Ejercicio/Dia6/entrada.txt").readline().split(",")].count(i) for i in range(9)]
    for _ in range(days):
        crecimiento.append(crecimiento.pop(0))
        crecimiento[6]+=crecimiento[-1]
    print(sum(crecimiento))

x1=peces_linterna(80)
x2=peces_linterna(256)


