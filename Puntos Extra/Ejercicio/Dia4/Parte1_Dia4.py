"""  
El bingo se juega en un conjunto de tableros, cada uno de los cuales consta de una cuadrícula de números de 5x5. 
Los números se eligen al azar y el número elegido se marca en todos los tableros en los que aparece. 
(Es posible que los números no aparezcan en todos los tableros). Si se marcan todos los números de cualquier fila o columna de un tablero, ese tablero gana .
En este punto, el tercer tablero gana porque tiene al menos una fila o columna completa de números marcados (en este caso, toda la fila superior está marcada:) 14 21 17 24 4.
La puntuación de la junta ganando ahora se puede calcular. Empiece por encontrar la suma de todos los números sin marcar en ese tablero; en este caso, la suma es 188. 
A continuación, se multiplica esa cantidad por el número que acaba de ser llamado cuando la junta ganó, 24para obtener la puntuación final, .188 * 24 = 4512
Para garantizar la victoria contra el calamar gigante, averigüe qué tablero ganará primero. ¿Cuál será tu puntuación final si eliges esa tabla?
"""
ingreso="/Users/gabri/iCloudDrive/Universidad/Quinto Semestre/Estructura de Datos/Puntos Extra/Ejercicio/Dia4/entrada.txt" 

def transformar_ingreso(ingreso):
    datos = open(ingreso, "r")
    pasos = datos.readlines()
    datos.close()
    for i in range(len(pasos)):
        pasos[i] = pasos[i].rstrip("\n")
    return pasos

def agregar_numero(tabla, valor):
    for i in range(5):
        for j in range(5):
            if tabla[i][j][0] == valor:
                tabla[i][j] = (valor, True)
                return tabla
    return tabla

def comprobar_bingo(tabla):
    for i in range(5):
        ganador = True
        for j in range(5):
            if tabla[i][j][1] == False:
                ganador = False
        if ganador:
            return True
    for j in range(5):
        ganador = True
        for i in range(5):
            if tabla[i][j][1] == False:
                ganador = False
        if ganador:
            return True
    return False

def contador_puntos(tabla,valores):
    contador = 0
    for i in range(5):
        for j in range(5):
            if not tabla[i][j][1]:
                contador+= int(tabla[i][j][0])
    return contador * int(valores)

def puntuacion_final(ingreso):
    valores = ingreso[0].split(',')
    tablas = []
    recorido = ingreso[2:]
    for i in range(0, len(recorido), 6):
        tabla = [[(val, False) for val in line.split() ] for line in recorido[i:i+5]]
        tablas.append(tabla)
    for num in valores:
        for x in range(len(tablas)):
            tablas[x] = agregar_numero(tablas[x], num)
            if comprobar_bingo(tablas[x]):
                return contador_puntos(tablas[x], num)
    return 0
 

print("puntuacion final1:",puntuacion_final(transformar_ingreso(ingreso)))