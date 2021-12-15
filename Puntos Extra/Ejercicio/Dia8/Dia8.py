""" 
A medida que su submarino avanza lentamente a través del sistema de cuevas, se da cuenta de que las pantallas de siete segmentos de cuatro dígitos 
de su submarino no funcionan correctamente; deben haber sido dañados durante la fuga. Te meterás en muchos problemas sin ellos, así que será mejor que averigües qué está mal.

Cada dígito de una pantalla de siete segmentos se representa activando o desactivando cualquiera de los siete segmentos nombrados amediante g

El problema es que las señales que controlan los segmentos se han mezclado en cada pantalla. El submarino todavía está tratando de mostrar números produciendo una salida a 
através de cables de señal g, pero esos cables están conectados a segmentos al azar . 
Peor aún, las conexiones de cable / segmento se mezclan por separado para cada pantalla de cuatro dígitos. 
(Sin embargo, todos los dígitos dentro de una pantalla usan las mismas conexiones).

Por lo tanto, es posible que sepa que solo los cables de señal by gestán encendidos, pero eso no significa segmentos b y gestán encendidos: 
el único dígito que usa dos segmentos es 1, por lo que debe significar segmentos cy festán destinados a estar encendidos. 
Con solo esa información, aún no puede saber qué cable ( b/ g) va a qué segmento ( c/ f). Para eso, necesitará recopilar más información.

Para cada pantalla, observa las señales cambiantes durante un tiempo, toma nota de los diez patrones de señal únicos que ve y luego escribe 
un solo valor de salida de cuatro dígitos (su entrada de rompecabezas). Usando los patrones de señal, debería poder determinar qué patrón corresponde a qué dígito.

Cada entrada consta de diez patrones de señal únicos , un |delimitador y, finalmente, el valor de salida de cuatro dígitos . 
Dentro de una entrada, se utilizan las mismas conexiones de cable / segmento (pero no sabe cuáles son realmente las conexiones). 
Los patrones de señal únicos corresponden a las diez formas diferentes en que el submarino intenta representar un dígito utilizando las conexiones de cable / segmento actuales. 
Debido a que 7es el único dígito que utiliza tres segmentos, daben los medios de ejemplo anteriores se desprende que para rendir una 7, líneas de señal d, ay bson sobre. 
Debido a que 4es el único dígito que utiliza cuatro segmentos, eafbsignifica que para hacer Un 4, líneas de señales e, a, f, y bestán encendidas.

Con esta información, debería poder determinar qué combinación de cables de señal corresponde a cada uno de los diez dígitos. 
Luego, puede decodificar el valor de salida de cuatro dígitos. Desafortunadamente, en el ejemplo anterior, todos los dígitos del valor de salida 
( cdfeb fcadb cdfeb cdbaf) usan cinco segmentos y son más difíciles de deducir.

Por ahora, céntrese en los dígitos fáciles . Considere este ejemplo más grande:

Debido a que los dígitos 1, 4, 7, y 8 cada uso de un único número de segmentos, que debe ser capaz de decir qué combinaciones de señales corresponden a esos dígitos. 
Contando solo dígitos en los valores de salida (la parte después |de cada línea), en el ejemplo anterior, hay 26casos de dígitos que usan un número único de segmentos (resaltados arriba).

En los valores de salida, ¿cuántas veces dígitos 1, 4, 7, o 8aparecerá?
"""

with open("/Users/gabri/iCloudDrive/Universidad/Quinto Semestre/Estructura de Datos/Puntos Extra/Ejercicio/Dia8/entrada.txt","r") as datos:
    pasos = [[set(x) for x in digitos.split()] for digitos in datos.read().split("\n")]


def Solucion1():
    contador=0
    for i in pasos:
        contador += sum(len(digito) in (2,3,4,7) for digito in i[-4:])
    return contador    

print("valores 1,4,7,8 repetidos:",Solucion1())