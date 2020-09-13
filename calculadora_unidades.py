def operacion_multi(unidad, valor, obtienes):
    und = float(input('¿Cuantos ' + unidad + ' quieres convertir? '))
    result = und * valor
    result = round(result,2)
    print('Son ' + str(result) + obtienes +'. ')

def operacion_div(unidad, valor, obtienes):
    und = float(input('¿Cuantos ' + unidad + ' quieres convertir? '))
    result = und / valor
    result = round(result,2)
    print('Son ' + str(result) + ' ' +obtienes +'. ')    

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
    operacion_multi('Kilogramos', 1000, 'gramos')

elif consulta == 2:
    operacion_div('Gramos', 1000, 'kilogramos')
    
elif consulta == 3:
    operacion_div('mililitros', 1000, 'kilogramos')
else:
    print('No permitido')

