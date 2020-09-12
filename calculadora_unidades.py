##unidad = input("¿Que unidad quieres convertir?: ")

unidad = input("¿Cuantos kilos quieres transformar en gramos?: ")
unidad = float(unidad)

gramo = 1000

result = unidad * gramo
result = round(result, -1)
print("Son " + str(result) + " gramos.")