from math import pi

radio = float(input('Escriba el radio del cilindro: '))
altura = float(input('Escriba la altura del cilindro: '))

area_base = pi * radio ** 2

area_lateral = 2 * pi * radio * altura

area_total = 2 * area_base * area_lateral

print('El área base del cilindro es: ', area_base)
print('El área lateral del cilindro es: ',area_lateral)
print('El área total del cilindro es: ',area_total)
