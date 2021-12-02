def vocale (cadena):
    long=len(cadena)
    cont_a=0
    cont_e = 0
    cont_i = 0
    cont_o = 0
    cont_u = 0
    for x in range(long):
        if cadena[x] == "a":
            cont_a+=1
        elif cadena[x] == "e":
            cont_e += 1
        elif cadena[x] == "i":
            cont_i += 1
        elif cadena[x] == "o":
            cont_o += 1
        elif cadena[x] == "u":
            cont_u += 1
    print(f"Existen: {cont_a} a, {cont_e} e, {cont_i} i, {cont_o} o y {cont_u} u en la palabra {cadena}")

print ("Ingresa una palabra:")
cadena = input()
vocale (cadena)