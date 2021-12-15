""" 
En el ejemplo anterior, el segundo tablero es el último en ganar, 
lo que sucede después de 13que finalmente se llama y su columna central está completamente marcada. 
Si siguiera jugando hasta este punto, el segundo tablero tendría una suma de números sin marcar igual a 148
para una puntuación final de .148 * 13 = 1924
Averigua qué tabla ganará en último lugar. Una vez que gane, ¿cuál sería su puntuación final?

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
    valores=ingreso[0].split(",")
    tablas=[]
    recorrido=ingreso[2:]
    rep={}
    for i in range(0,len(recorrido),6):
        tabla=[[(valor,False) for valor in pos.split()]for pos in recorrido[i:i+5]]
        rep[int(i/6)]=(0,0)
        tablas.append(tabla)
    aux1=0
    for j in valores:
        for k in range(len(tablas)):
            tablas[k]=agregar_numero(tablas[k],j)
            if comprobar_bingo(tablas[k]):
                if rep[k]==(0,0):
                    aux1 +=1
                    rep[k]=(aux1,contador_puntos(tablas[k],j))
    return max(rep.values())[1]

print("puntuacion final2:",puntuacion_final(transformar_ingreso(ingreso)))