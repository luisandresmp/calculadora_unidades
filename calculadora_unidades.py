menu = """
*************************************
Bienvenido al convertidor de unidades
************************************* 

¿Que operación quieres realizar? 

[1] Kilos -> Gramos 
[2] Gramos -> Kilos 
[3] Mililitros -> Kilos 

Operación: 
"""
consulta = int(input(menu))

if consulta == 1:
    unidad = float(input('¿Cuantos Kilogramos quieres convertir? '))
    gramo = 1000
    result = unidad * gramo
    result = round(result,2)
    print('Son ' + str(result) + ' gramos.')

elif consulta == 2:
    unidad = float(input('¿Cuantos Gramos quieres convertir? '))
    gramo = 1000
    result = unidad / gramo
    result = round(result,2)
    print('Son ' + str(result) + ' kilogramos.')

elif consulta == 3:
    unidad = float(input('¿Cuantos milimitros quieres convertir? '))
    gramo = 1000
    result = unidad / gramo
    result = round(result,2)
    print('Son ' + str(result) + ' kilogramos.')

else:
    print('No permitido')

