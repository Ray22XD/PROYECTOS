grados = int(input("INGRESE GRADOS:"))
if grados == 0:print("nulo")
elif grados == 90: print("RECTO")
elif grados == 180: print("LLANO")
elif grados == 360: print("COMPLETO")
else:
    if (grados > 0) & (grados < 90): print("AGUDO")
    elif (grados > 90) & (grados < 180): print("OBTUSO")
    elif (grados > 180) & (grados < 360): print("CONCAVO")