"""
El informe de diagnóstico (su entrada del rompecabezas) consiste en una lista de números binarios que, 
cuando se decodifican correctamente, pueden decirle muchas cosas útiles sobre las condiciones del submarino. 
El primer parámetro a comprobar es el consumo de energía .
Utilice los números binarios en su informe de diagnóstico para calcular la tasa gamma y la tasa épsilon, 
luego multiplíquelos. ¿Cuál es el consumo de energía del submarino? (Asegúrese de representar su respuesta en decimal, no en binario).

"""
valor_gamma= " "
epsilon= " "
with open("/Users/gabri/iCloudDrive/Universidad/Quinto Semestre/Estructura de Datos/Puntos Extra/Ejercicio/Dia3/entrada1.txt","r") as datos:
  pasos=[i.rstrip() for i in datos]

for i in range(len(pasos[0])):
    columna= [j[i] for j in pasos]
    valor_gamma += max(set(columna), key=columna.count)
    epsilon+= min(set(columna), key=columna.count)
consumo=int(valor_gamma,2)*int(epsilon,2)

print("consumo energetico:",consumo)
