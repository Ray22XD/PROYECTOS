import os
os.system("cls")

practica1 = (float(input("INGRESE NOTA DE PRACTICA 1:")))
practica2 = (float(input("INGRESE NOTA DE PRACTICA 2:")))
practica3 = (float(input("INGRESE NOTA DE PRACTICA 3:")))
if practica3 >= 10 : practica3 = (practica3 + 2)
PROMEDIOFINAL = (practica1 + practica2 + practica3) / 3
print("PROMEDIO FINAL", repr(PROMEDIOFINAL))
