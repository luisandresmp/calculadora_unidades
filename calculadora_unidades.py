consulta = int(input('¿Que unidad quieres convertir? [1] Kilos -> Gramos [2] Gramos -> Kilos '))


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

else:
    print('No permitido')

