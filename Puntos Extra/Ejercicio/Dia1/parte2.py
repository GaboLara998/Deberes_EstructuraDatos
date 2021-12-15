#Parte dos
"""
considere las sumas de una ventana deslizante de tres medidas . Nuevamente considerando el ejemplo anterior:
Empiece por comparar la primera y la segunda ventana de tres mediciones. Las mediciones en la primera ventana 
están marcados A( 199, 200, 208); su suma es 199 + 200 + 208 = 607. La segunda ventana se marca B( 200, 208, 210); 
su suma es 618. La suma de las medidas en la segunda ventana es mayor que la suma de la primera, por lo que esta 
primera comparación aumentó 
Contar el número de veces que la suma de medidas en esta ventana deslizante aumenta con respecto a la suma 
anterior. Entonces, compare Acon B, luego compare Bcon C, luego Ccon D, y así sucesivamente. 
Deténgase cuando no queden suficientes medidas para crear una nueva suma de tres medidas.

"""

ingresar_valores=[]
contador=0

with open("/Users/gabri/iCloudDrive/Universidad/Quinto Semestre/Estructura de Datos/Puntos Extra/Ejercicio/Dia1/datos.txt","r") as datos:
    for i in datos.readlines():
            ingresar_valores.append(int(i.rstrip("\n")))

for i in range(len(ingresar_valores)):
    if sum(ingresar_valores[i:i+3]) < sum(ingresar_valores[i+1:i+4]):
        contador+=1

print("sumas son mayores que la suma anterior ", contador)