# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("ESCRIBA SU ESTATURA (ft y pulgadas);")
PIE = float(input("INGRESE ESTATURA PIE: "))
PULGADAS = float(input("INGRESE ESTATURA PULGADAS: "))
CM = PIE *30.48
CM += PULGADAS *2.54
print("su estatura en Centimentros es {} CM" .format(CM))