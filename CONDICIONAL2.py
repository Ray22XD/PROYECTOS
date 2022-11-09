import os

os.system("cls")

unidades = float(input("unidades : "))
preunit=20

IMPORTEDECOMPRA= (preunit*unidades)
descuento=(IMPORTEDECOMPRA * 0.14)*IMPORTEDECOMPRA
descuento = ( 0.12 if IMPORTEDECOMPRA <= 500 else 0.14) * IMPORTEDECOMPRA

if IMPORTEDECOMPRA >= 700 : descuento= 0.16* IMPORTEDECOMPRA
CARAMELO = 10
if unidades <= 50 : CARAMELO= 5
elif unidades >100  : CARAMELO = 15 

print ( f"IMPORTEDECOMPRA = {IMPORTEDECOMPRA}\n" )
print ( f"DESCUENTO = {descuento}\n" )
print ( f"TOTAL A PAGAR = {IMPORTEDECOMPRA - descuento}\n")
print ( f"CARAMELO = {CARAMELO}\n" )
