
"""
A continuación, debe verificar la clasificación de soporte vital , 
que se puede determinar multiplicando la clasificación del generador de oxígeno por la clasificación del depurador de CO2 .
Mantenga solo los números seleccionados por los criterios de bit para el tipo de valor de clasificación que está buscando. 
Descarte los números que no coincidan con los criterios de bits.
Si solo le queda un número, deténgase; este es el valor de clasificación que está buscando.
De lo contrario, repita el proceso, considerando el siguiente bit a la derecha.
Para encontrar la clasificación del generador de oxígeno , determine el valor más común ( 0o 1) en la posición actual del bit y mantenga solo los números con ese bit en esa posición. 
Si 0y 1son igualmente comunes, mantenga los valores con a 1en la posición que se está considerando.
Para encontrar la clasificación del depurador de CO2 , determine el valor mínimo común ( 0o 1) en la posición actual del bit y mantenga solo los números con ese bit en esa posición. 
Si 0y 1son igualmente comunes, mantenga los valores con a 0en la posición que se está considerando.

Utilice los números binarios en su informe de diagnóstico para calcular la clasificación del generador de oxígeno y la clasificación del depurador de CO2, luego multiplíquelos.
¿Cuál es la clasificación de soporte vital del submarino? (Asegúrese de representar su respuesta en decimal, no en binario).


"""

with open("/Users/gabri/iCloudDrive/Universidad/Quinto Semestre/Estructura de Datos/Puntos Extra/Ejercicio/Dia3/entrada1.txt","r") as datos:
  pasos=[i.rstrip() for i in datos]
  
def clasificacion(valores, val_max, pos_actual):
    for n in range(len(valores[0])):
        columna = [row[n] for row in valores]
        valor_gamma = epsilon = ""
        valor_gamma += max(set(columna), key=columna.count)
        epsilon += min(set(columna), key=columna.count)
        match = valor_gamma if val_max else epsilon
        if valor_gamma != epsilon:
            valores = [x for x in valores if x[n] == match]
        else:
            valores = [x for x in valores if x[n] == pos_actual]
        if len(valores) == 1:
            return "".join(valores)


oxigeno = clasificacion(pasos, True, "1")
co2 = clasificacion(pasos, False, "0")
soporte_vital = int(oxigeno, 2) * int(co2, 2)
print("Clasificacion:", soporte_vital)
