from math import pi

radio = float(input('Escriba el radio del cilindro: '))
altura = float(input('Escriba la altura del cilindro: '))

area_total = 2 * pi * radio ** 2 + 2 * pi * radio * altura

volumen = pi * radio ** 2 * altura

print('El área total del cilindro es: ', area_total)
print('El volumen del cilindro es: ',volumen)
